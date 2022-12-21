from rest_framework.response import Response
from rest_framework import views
from .serializers import (
    Talaba_Qushish_serializer,
    Talabaga_homiy_qushish_serializer,
    Talaba_data_Read_Only_serializer,
)
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from .models import Talaba_qushish
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import rest_framework as filter_dj
from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request

# Create your views here.


class Talaba_qushish_view(ModelViewSet):
    # serializer_class = Talaba_Qushish_serializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["^Talaba_ismi", "talabalik_turi"]
    ordering_fields = ("sana",)

    def get_queryset(self):
        if self.action == "add":
            return []
        return Talaba_qushish.objects.all()

    def retrieve(self, request, pk=None):
        talaba = get_object_or_404(Talaba_qushish.objects.all(), pk=pk)
        serializer = Talaba_Qushish_serializer(talaba, context={"request": request})
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action in ["get", "retrieve"]:
            return Talaba_Qushish_serializer
        if self.action in ["add_homiy"]:
            return Talabaga_homiy_qushish_serializer
        return Talaba_Qushish_serializer

    @action(
        detail=False,
        methods=["post", "get"],
        serializer_class=Talaba_Qushish_serializer,
    )
    def add(self, request):
        """
        Siz bu yerda talaba qushishingiz mumkin

        """

        if request.method == "GET":
            queryset = self.get_queryset()
            seril = self.get_serializer(queryset, many=True)
            return Response(seril.data)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data qushildi": serializer.data})
        return Response(serializer.data)

    @action(
        detail=True,
        methods=["post", "get"],
        serializer_class=Talabaga_homiy_qushish_serializer,
    )
    def add_homiy(self, request, pk=None):
   
        """ 
        Talabga homiy qushish uchun extra action

        """
        if request.method == "GET":
            queryset = get_object_or_404(Talaba_qushish.objects.all(), pk=pk)
            return Response(
                Talaba_data_Read_Only_serializer(
                    queryset, many=False, context={"request": request}
                ).data
            )

        serializer_of_homiy = self.get_serializer(data=request.data, context={"pk": pk})
        if serializer_of_homiy.is_valid():
            serializer_of_homiy.save()
            return Response(serializer_of_homiy.data)
        return Response(serializer_of_homiy.errors)

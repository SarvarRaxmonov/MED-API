from rest_framework.response import Response
from rest_framework import views  
from .serializers import Talaba_Qushish_serializer
from rest_framework import status
from .models import Talaba_qushish
# Create your views here.


class Talaba_qushish_view(views.APIView):
    serializer_class = Talaba_Qushish_serializer
    def get(self,request):
        instance = Talaba_qushish.objects.all()
        serializer = Talaba_Qushish_serializer(instance,many=True,context={"request": request})
        return Response({'Data':serializer.data})
         
      
    def post(self,request):
        serializer = Talaba_Qushish_serializer(data=request.data)
        if serializer.is_valid():    
            serializer.save()
            obj = Talaba_qushish.talaba_kontrakti_tulanganlar()
            return Response({'Data':serializer.data,'data':obj})
        return Response(serializer.errors, status=status.HTTP_200_OK)
          
    @classmethod
    def get_extra_actions(cls):
        return []
    
    
    
    
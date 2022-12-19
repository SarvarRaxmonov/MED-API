from rest_framework.response import Response
from med_apps.homiy.models import HomiyArizasi
from med_apps.talaba.models import Talaba_qushish
from django.db.models import Sum
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.db.models import Count
# Create your views here.



class AdminPanel(ReadOnlyModelViewSet):

      queryset = HomiyArizasi.objects.all()
      def list(self,request):
            
          homiylar_tulagan_summa = HomiyArizasi.objects.aggregate(Sum('Sarflangan_summa'))
          talabalar_jammi_kontrakti = Talaba_qushish.objects.aggregate(Sum('Kontrakt_summa'))
          talablarga_tulanishi_kerak_summa =  abs(talabalar_jammi_kontrakti.get('Kontrakt_summa__sum') - homiylar_tulagan_summa.get('Sarflangan_summa__sum'))

         
          return Response({'Tulangan summa':homiylar_tulagan_summa,'Ummumiy suralgan summa':talabalar_jammi_kontrakti.get('Kontrakt_summa__sum'),
                           'Tulanishi kerak bulgan summa':talablarga_tulanishi_kerak_summa})
         
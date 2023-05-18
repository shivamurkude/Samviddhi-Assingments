from django.shortcuts import render
from .serializer import TAserializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TA
from rest_framework import status
# Create your views here.

class TAView(APIView):
    def post(self,request):
        try: 
            data=request.data
            data["created_by"]=request.user.id

            ser=TAserializer(data=data)
            if ser.is_valid():
               
                ser.save()
                return Response({'TA':ser.data})
            return Response({'error':ser.errors})
        except Exception as e:
            return Response({'error':str(e)})
    
    def patch(self, request, *args, **kwargs):
        data = request.data
        ta = TA.objects.get(ta_id=request.GET.get('ta_id',''))
        if not ta:
            return Response({
                "error": "Invalid TA ID"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            
            ser = TAserializer(ta, data=data, partial=True)
            if ser.is_valid():
                ser.save()
                resp = Response({
                    "status": "success",
                    "data":ser.data
                }, status=status.HTTP_200_OK)
                
            else:
                resp = Response({
                    "errors": ser.errors
                }, status=status.HTTP_200_OK)
                
            return resp
        except Exception as ve:
            
            return Response({
                "error": str(ve)
            }, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        try: 
            ta = TA.objects.get(ta_id=request.GET.get('ta_id',''))
            serializer = TAserializer(ta)
            return Response({"data": serializer.data})
        except Exception as ve:
            return Response({
                "error": str(ve)
            }, status=status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        try: 
            ta = TA.objects.get(ta_id=request.GET.get('ta_id',''))
            ta.delete()
            return Response({
                "status": "success"
            }, status=status.HTTP_200_OK)
        except Exception as ve:
            
            return Response({
                "error": str(ve)
            }, status=status.HTTP_200_OK)

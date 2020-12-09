from django.shortcuts import render
from .models import Business,Review,ContactInfo,Media
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Business
from .serializer import BizSerializer
from rest_framework import status

# Create your views here.
def index(request):
    return render(request,'index.html')

class bizList(APIView):
    def get(self,requset,format=None):
        all_businesses = Business.objects.all()
        serializers = BizSerializer(all_businesses, many = True)
        return Response(serializers.data)

    def post(self, request,format=None):
        serializers =BizSerializer(data=request.data)
        if serializers.is_valid():
            serializer.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
            
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

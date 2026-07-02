from django.shortcuts import render
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import User_serializer
class UserView(APIView):
    serializer_class=User_serializer
    def get(self,request):
        user=request.user
        serializer=User_serializer(user)
        return Response(serializer.data,status=200)
    def put(self,request):
        serializer=User_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
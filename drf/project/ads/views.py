from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Ad
from .serializer import AdSerializer
#from .permission import IsPublisherOrReadOnly
from .pagination import StandardResultsSetPagination
from django.db.models import Q

class AdListView(APIView, StandardResultsSetPagination):
#    permission_classes = [IsPublisherOrReadOnly]
    serializer_class = AdSerializer

    def get(self, request):
        queryset = Ad.objects.filter(is_public=True)
        result = self.paginate_queryset(queryset, request)
        serializer = AdSerializer(result, many=True)
        return self.get_paginated_response(serializer.data)

class creat_ad_post(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AdSerializer
    parser_classes = [MultiPartParser]

    def post(self, request):
        serializer = AdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['publisher'] = self.request.user
            serializer.save()
            return Response(serializer.data, status=200)
class detail_ad(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class=AdSerializer
    parser_classes = [MultiPartParser]
    def get(self,request,pk):
        instance=Ad.objects.get(pk=pk)
        serializer=AdSerializer(instance=instance)
        return Response(serializer.data,status=200)
    def put(self,request,pk):
        instance=Ad.objects.get(pk=pk)
        serializer=AdSerializer(instance,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors,status=400)
    def delete(self,request,pk):
        instance=Ad.objects.get(pk=pk)
        instance.delete()
        return Response({'response':'is deleted'},status=200)
class ad_search(APIView,StandardResultsSetPagination):
    serializer_class=AdSerializer
    def get(self,request):
        q=request.GET.get('q')
        queryset = Ad.objects.filter(Q(title__icontains=q) | Q(caption__icontains=q))
        result = self.paginate_queryset(queryset,request)
        serializer=AdSerializer(instance=result,many=True)
        return self.get_paginated_response(serializer.data)
    
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UrlSerializer
from rest_framework import status
from .models import UrlModel
from django.shortcuts import redirect
from django.utils import timezone
# Create your views here.
class ViewHandler(APIView):
    def get(self, request,pk):
        if request.method == 'GET':
            if request.headers.get('json') == "true":
                try:
                    url = UrlModel.objects.get(short_url = pk)
                    url.clicks += 1
                    url.save()
                    url.last_clicked = timezone.now()
                    serialized_data = UrlSerializer(url)
                    return Response(data=serialized_data.data , status=status.HTTP_200_OK)
                except Exception as e:
                    return Response({'error': 'Invalid URL'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                try:
                    url = UrlModel.objects.get(short_url = pk)
                    url.clicks += 1
                    url.save()
                    return redirect(url.url)
                except Exception as e:
                    return Response({'error': 'Invalid URL'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        if request.method == 'POST':
            serialised_data = UrlSerializer(data=request.data , many=True  ,partial=True)
            if serialised_data.is_valid():
                serialised_data.save()
                return Response(serialised_data.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serialised_data.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)
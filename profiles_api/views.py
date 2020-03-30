from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):

    def get(self, request, format=None):
        an_apiview = [
        'uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to Traditional Django view',
        'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})



# Create your views here.

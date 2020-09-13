from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class HelloApiView(APIView):

    def get(self, request, format=None):
        """Returns a list of APIview features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional django view',
            'Gives you the controlover application logic',
            'Is mapped manuaclly to URLs',
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})
        

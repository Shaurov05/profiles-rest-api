from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from . serializers import HelloSerializer
# Create your views here.


class HelloApiView(APIView):

    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIview features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional django view',
            'Gives you the controlover application logic',
            'Is mapped manuaclly to URLs',
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data['name']
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ Update an object """
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """ handle partial update of an object"""
        return Response({'method': 'Patch'})

    def delete(self, request, pk=None):
        return Response({"method": 'DELETE'})











        #

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import viewsets

from rest_framework import status
from . serializers import HelloSerializer
from . import models
from . import serializers
from rest_framework.authentication import TokenAuthentication
from . import permissions

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



class HelloViewSet(viewsets.ViewSet):

    serializer_class = HelloSerializer

    def list(self, request):
        """Return a hellow message"""
        a_viewset = [
            'uses action (list, createm retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'provides more functionality with less code',
        ]
        return Response({'message':"Hello", 'a_viewset':a_viewset})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name} from ViewSet'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_404_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        return Response({"http_method":"Get"})

    def update(self, request, pk=None):
        return Response({"http_method":"put"})

    def partial_update(self, request, pk=None):
        return Response({"http_method":"Patch"})

    def destroy(self, request, pk=None):
        return Response({"http_method":"delete"})



class UserProfileViewSet(viewsets.ModelViewSet):
    """ handle creating and updating profiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)

    search_fields = ('name', 'email', )



from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES







        #

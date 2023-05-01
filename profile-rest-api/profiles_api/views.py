from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from profiles_api import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request , format=None):
        an_apiview =[
            'Uses HTTP method as function (get , post ,patch ,put ,delete)',
            'is similar to traditional Django view',
            'Gives you the most control over your applicatiin logic ',
            'Is mapped manually to URLS',
        ]
        return Response({'message':'hello','an_apiview':an_apiview})
    
    def post(self,request,format=None):
        serializer =self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST
                            )
        
    def put(self,request,pk=None):
        return Response({'method':'PUT'})
    
    def patch(self, request,pk=None):
        return Response({'method':'PATCH'})
    
    def delete(self,request,pk=None):
        return Response({'method':'DELETE'})
    
class HelloViewSet(viewsets.ViewSet):
    'Test API ViewSet'
    def list(self,request):
        'return a hello message'

        a_viewset =[
            'User action ( list , create , retrieve , update ,partial_update)'
            'Automatically map to urls using router',
            'provides more funcationality with less code',
        ]
        return Response({'message':'Hello','a_viewset':a_viewset}) 
    


class UserProfileViewSet(viewsets.ModelViewSet):
    'handle creating and updating profile'
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes= (permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
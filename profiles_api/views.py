from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication  
#generates a random token string when the user logs in, then for every API request thereafter, this token string is added to the request which works as a password to authenticate requests

from profiles_api import serializers, models, permissions


class HelloApiView(APIView):
    '''Test API View'''
    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None): #typically used to retrieve an object/list of objects
        '''Returns a list of APIView features'''
        an_apiview= [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'is similar to a traditional django view',
            'gives you most control over your application logic',
            'is mapped manually to URLs',
            ]
        # Response converts a list/dictionary of objects into JSON format
        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        '''Create a hello message with our name'''
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk=None):
        '''Handle updating an object'''
        return Response({'method':'PUT'})
    
    def patch(self,request,pk=None):
        '''Handle a partial update of an object'''
        return Response({'method':'PATCH'})
    
    def delete(self,request,pk=None):
        '''Delete an object'''
        return Response({'method':'DELETE'})
    
class HelloViewSet(viewsets.ViewSet):
    '''Test API viewset'''
    serializer_class= serializers.HelloSerializer
    def list(self,request):
        '''return a hello message'''
        a_viewset=[
            'Uses actions (list, create, retrieve, update, partial_update)',
                   'Automatically maps to URLS Routers',
                   'Provides more functionality with less code',
                   ]
        return Response({'message':'Hello!', 'a_viewset':a_viewset})
    
    def create(self,request):
        '''Create a new hello message'''
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid:
            name=serializer.validated_data.get('name')
            message=f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request,pk=None):
        '''Handle getting an object by its ID'''
        return Response({'http_method':'GET'})
    
    def update(self,request,pk=None):
        '''Handle updating an object'''
        return Response({'http_method':'PUT'})
    
    def partial_update(self,request,pk=None):
        '''Handle updating some fields of an object'''
        return Response({'http_method':'PATCH'})
    
    def destroy(self,request,pk=None):
        '''Handle removing an object'''
        return Response({'http_method':'DELETE'})
    
class UserProfileViewSet(viewsets.ModelViewSet):
    '''Handle creating and updating profiles'''
    serializer_class = serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)

    
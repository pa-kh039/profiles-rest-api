from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    '''Test API View'''
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

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class Helloworldview(APIView):
    #get mehod to handle get requests
    def get(self,request):
        context = {
            'message' : 'hello!',
        }
        return Response(context)
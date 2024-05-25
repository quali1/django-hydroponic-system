from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication


class HomePage(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

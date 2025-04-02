from django.contrib.auth import authenticate, get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication



User = get_user_model() 

class LoginView(APIView):

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password) 

        if user:
            refresh = RefreshToken.for_user(user)  
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "role": user.role  
            }, status=status.HTTP_200_OK)

        return Response({"error": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)


class UserDetailView(APIView):
    """
    Vista para obtener detalles del usuario autenticado.
    """
    authentication_classes = [JWTAuthentication]  
    permission_classes = [IsAuthenticated]  

    def get(self, request):
        user = request.user
        return Response({
            "email": user.email,
            "role": user.role
        }, status=status.HTTP_200_OK)
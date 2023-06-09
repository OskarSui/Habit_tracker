from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from social_core.exceptions import AuthForbidden
from social_django.utils import psa

from users.models import User
from users.serializers import UserSerializer, HabitSerializer


class UserApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):

        data = request.data
        User.auth_user(data=data)
        instance = User.create_from_post(data)
        serializer = UserSerializer(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SocialLoginView(TokenObtainPairView):
    @api_view(['POST'])
    @permission_classes([AllowAny])
    @psa('social:complete')
    def SocialLoginView(request, backend):
        try:
            user = request.backend.do_auth(request.data.get('access_token'))
        except AuthForbidden as e:
            return Response({'error': 'Не удалось авторизоваться через Google'}, status=status.HTTP_400_BAD_REQUEST)

        if user:
            access_token = AccessToken.for_user(user)
            refresh_token = RefreshToken.for_user(user)

            jwt_token = {
                'access': str(access_token),
                'refresh': str(refresh_token),
            }

            return Response(jwt_token, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Не удалось авторизоваться через Google'}, status=status.HTTP_400_BAD_REQUEST)
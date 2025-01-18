import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from .serializers import TodoSerializer
from .models import Todo
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.jwt_auth import set_jwt_access_cookie, set_jwt_refresh_cookie


class TodoListView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'postmessage'
    client_class = OAuth2Client


class GoogleCodeExchangeView(APIView):
    def post(self, request):
        code = request.data.get('code')
        print(f"code: {code}")
        url = "http://127.0.0.1:8000/api/v1/dj-rest-auth/google/"
        google_res = requests.post(url, json={'code': code})
        if google_res.status_code == status.HTTP_200_OK:
            access_token = google_res.json()["access"]
            refresh_token = google_res.json()["refresh"]
            res =Response(
                {
                    "detail": "able to get the tokens"
                },
                status=status.HTTP_200_OK
            )
            set_jwt_access_cookie(res, access_token)
            set_jwt_refresh_cookie(res, refresh_token)

            return res

        return Response(
                {
                    "detail": "Error, bad request exchange token with google"
                },
                status=status.HTTP_400_BAD_REQUEST
            )


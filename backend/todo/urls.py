from django.urls import path
from .views import TodoListView, GoogleLogin, GoogleCodeExchangeView


urlpatterns = [
    path("todo/", TodoListView.as_view(), name="todo_list"),
    path('dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('google-code-exchange/', GoogleCodeExchangeView.as_view(), name="google_code_exchange"),
]

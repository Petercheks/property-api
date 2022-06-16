from django.urls import path, include

from api.views import SignIn , SignOut

urlpatterns = [
    path('u-v1/', include('users.urls')),
    path('auth/sign-in/', SignIn.as_view()),
    path('auth/sign-out/', SignOut.as_view()),
]
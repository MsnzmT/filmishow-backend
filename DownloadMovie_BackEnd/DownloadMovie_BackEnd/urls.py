"""DownloadMovie_BackEnd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from backend.views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignUp.as_view()),
    # path('login/', obtain_auth_token),
    # path('logout/', LogOut.as_view()),
    path('home/', AllFilms.as_view()),
    path('upload-film/', UploadFilm.as_view()),
    path('comment/<int:film_id>/', AddComment.as_view()),
    path('category/horror/', FilterFilms.as_view()),
    path('category/drum/', FilterFilms.as_view()),
    path('category/fantasy/', FilterFilms.as_view()),
    path('category/action/', FilterFilms.as_view()),
    path('category/comedy/', FilterFilms.as_view()),
    path('search/', SearchFilmName.as_view()),
    path('film/<int:film_id>/', SearchFilmId.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/logout/', LogoutJWT.as_view()),
    path('arrival/', Arrival.as_view()),
    path('like/<int:film_id>/', LikeComment.as_view()),
    path('email/', EmailVerification.as_view()),
    path('email/validation/', CodeValidate.as_view())
]

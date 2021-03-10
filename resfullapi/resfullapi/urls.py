from django.contrib import admin
from django.urls import path,include
from .router import router
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView #In this we have to download simplejwt
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)), #it will be getting all the request from router files and fetch them
    path('',TokenObtainPairView.as_view()),#to get tokens both access and refresh
    path('token/refresh/',TokenRefreshView.as_view()) #to get new access token if our toekn is expired

]
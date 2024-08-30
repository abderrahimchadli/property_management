from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 
from .views import RegisterView ,CustomTokenObtainPairView ,LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),


]

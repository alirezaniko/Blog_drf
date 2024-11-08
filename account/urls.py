from django.urls import path
from . import views
from .views import RegisterUserView, UserProfileView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
app_name = "account"
urlpatterns = [
    path("login", views.login_user, name="login"),
    path("register", views.user_register, name="signup"),
    path("logout", views.user_logout, name="logout"),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

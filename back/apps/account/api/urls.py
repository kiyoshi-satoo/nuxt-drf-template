
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    # path('auth/', include('djoser.urls')),
    # JWT AUTH
    # path('auth/register/', RegisterApi.as_view(), name='register'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_view'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh_view'),
    # path('logout/blacklist/', BlacklistTokenUpdateView.as_view(), name='blacklist')
]

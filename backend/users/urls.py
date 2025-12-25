
from django.urls import path,include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt import views as jwt_views
from users import views

app_name='users'

router=SimpleRouter()
router.register('register',views.RegisterAPIView)

urlpatterns = [
path('',include(router.urls)),
path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
path('logout/',views.LogoutAPIView.as_view(),name='logout')
]

from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    # Your URLs...
    path('api/token/', obtain_auth_token, name='token_obtain_pair'),
    #path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('admin/', admin.site.urls),
    path('user/',include('user_app.urls')),
    path('tree/',include('tree_app.urls')),
    path('log/',include('log_app.urls'))
]

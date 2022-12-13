from django.contrib import admin
from django.urls import path, include
from user import views as user_view

urlpatterns = [

	path('admin/', admin.site.urls),
	##### user related path##########################
	path('', include('user.urls')),
    path("accounts/", include('allauth.urls'))
]
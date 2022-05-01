from django.contrib import admin
from django.urls import path, include
from user import views as user_view
from django.contrib.auth import views as auth

urlpatterns = [

	path('admin/', admin.site.urls),

	##### user related path##########################
	path('', include('user.urls')),
	path('login/', user_view.Login, name ='login'),
	path('logout/', auth.LogoutView.as_view(template_name ='user/index.html'), name ='logout'),
	path('register/', user_view.register, name ='register'),
    path('diagnostic/', user_view.diagnostic, name ='diagnostic'),
    path('database/', user_view.database, name ='database'),
    path('veterinary/', user_view.veterinary, name ='veterinary'),
    path('indices/', user_view.indices, name ='indices'),
    path("prediction/", user_view.prediction, name="prediction"),
    path("accounts/", include('allauth.urls'))
]
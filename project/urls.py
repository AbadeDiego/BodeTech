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
    path('historico/', user_view.historico, name ='historico'),
    path('clientes/', user_view.clientes, name ='clientes'),
    path('publication/', user_view.publication, name ='publication'),
    path('card/', user_view.card, name ='card'),
    path("posts/", user_view.posts, name="posts"),
    path("beneficios/", user_view.beneficios, name="beneficios"),
    path("accounts/", include('allauth.urls'))
]
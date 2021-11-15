from django.urls import path
from . import views
app_name = "accounts"
urlpatterns = [
      path('signup/', views.signup_view, name='SignUp'),
      path('login/', views.login_view, name='Login'),
      path('logout/', views.logout_view, name='Logout')



]

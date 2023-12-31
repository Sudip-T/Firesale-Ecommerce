from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
# from .views import CustomLoginView

app_name = 'authentication'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'),name='login'),
    # path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='authentication:login'), name='logout'),
]
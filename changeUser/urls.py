from django.urls import path
from .views import *


urlpatterns = [
    path('g/', get_cookie_view),
    path('d/', delete_cookie_view),
    path('t/', test_cookie_view),
    path('s/', set_cookie_view),
    path('home/', home, name='home'),
    path('create/', create_record, name='create_record'),
    path('reg/', register),
    path('login/', log_in),
    path('logout/', log_out),
    path('change/', change_password),
]
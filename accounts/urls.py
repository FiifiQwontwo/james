from django.urls import path
from accounts.views import login_user, register_user

app_name = 'accounts'

urlpatterns = [
    path('login/', login_user, name='user_login'),
    path('signup/', register_user, name='user_sign_up'),

]

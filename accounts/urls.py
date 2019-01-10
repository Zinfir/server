from django.urls import path

from accounts.views import login_view, logout_view, registration, account_update, profile


app_name = 'accounts'

urlpatterns = [
    path('', login_view, name='login'),
    path('profile/<int:pk>/', profile, name='profile'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', registration, name='registration'),
    path('update/<int:pk>/', account_update, name='update'),
]
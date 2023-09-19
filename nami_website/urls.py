from django.urls import path
from authentication import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # URL for login
    path('signup/', views.signup_view, name='signup'),  # URL for signup
    path('logout/', views.logout_view, name='logout'),  # URL for logout
    # Add other URL patterns as needed
]

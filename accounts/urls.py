from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('', views.dashboard, name='dashboard'),
    path('products/', views.products, name='products'),
    path('customers/<str:pk>/', views.customers, name='customers'),

    path('orders/create/', views.create_order, name='create-order'),
    path('orders/update/<str:pk>/', views.update_order, name='update-order'),
    path('orders/delete/<str:pk>/', views.delete_order, name='delete-order'),

    path('user/', views.user_view, name='user-page'),
    path('user/profile-setting/', views.profile_setting, name='profile-setting'),

    # path('reset-password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


        path("password-reset/",auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password-reset/done/",auth_views.PasswordResetDoneView.as_view(),
         name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),

]


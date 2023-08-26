from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
    path('user/profile-setting/', views.profile_setting, name='profile-setting')
]


urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.home, name='home'),
    path('user/', views.userPage, name='user-page'),

    path('account/', views.accountSettings, name='account'),

    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customer, name='customer'),

    path('create_order/<str:pk>/', views.createOrder, name='create_order'),
    path('update_order/<str:pk>/', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),

    path('reset_password/', auth_views.PasswordResetView.as_view()),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view()),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view()),
    path('reset_password/complete/', auth_views.PasswordResetCompleteView.as_view()),
]

'''
1 - Submit email form                           //PasswordResetView.as_view()
2 - Email sent success message                  //PasswordResetDoneView.as_view()
3 - Link to Password Reset form in email        //PasswordResetConfirmView.as_view()
4 - Password successfully changed message       //PasswordResetCompleteView.as_view()
'''
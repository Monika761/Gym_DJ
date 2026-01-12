from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('members/', views.members_list, name='members'),
    path('add-member/', views.add_member, name='add_member'),
    path('payments/', views.payments_list, name='payments'),
    path('attendance/', views.attendance_page, name='attendance'),
    path('admin-login/', views.admin_login, name='admin-login'),  # <- custom login
]

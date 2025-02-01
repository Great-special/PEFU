from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('new-convert-list/', views.new_convert_list, name='new_convert_list'),
    path('new-convert-detail/<int:pk>/', views.new_convert_detail, name='new_convert_detail'),
    path('new-convert-create/', views.new_convert_create, name='new_convert_create'),
    path('new-convert-update/<int:pk>/', views.new_convert_update, name='new_convert_update'),
    path('new-convert-delete/<int:pk>/', views.new_convert_delete, name='new_convert_delete'),
    path('task-list/', views.task_list, name='task_list'),
    path('task-detail/<int:pk>/', views.task_detail, name='task_detail'),
    path('task-create/', views.task_create, name='task_create'),
    path('task-update/<int:pk>/', views.task_update, name='task_update'),
    path('task-delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('task-members-create/', views.task_members_create, name='task_members_create'),
    path('task-members-delete/<int:pk>/', views.task_members_delete, name='task_members_delete'),
    path('team-member-list/', views.evangelism_team_member_list, name='team_member_list'),
    path('team-member-create/', views.evangelism_team_member_create, name='team_member_create'),
    path('team-member-detail/<int:pk>/', views.evangelism_team_member_detail, name='team_member_detail'),
    path('team-member-update/<int:pk>/', views.evangelism_team_member_update, name='team_member_update'),
    path('team-member-delete/<int:pk>/', views.evangelism_team_member_delete, name='team_member_delete'),
    
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    
    # Profile URLs
    path('profile/update/', views.profile_update, name='profile_update'),
    path('profile/change-password/', views.change_password, name='change_password'),
    
    # Password Reset URLs
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', 
        views.CustomPasswordResetConfirmView.as_view(), 
         name='password_reset_confirm'),
    path('password_reset/complete/', 
        views.CustomPasswordResetCompleteView.as_view(), 
         name='password_reset_complete'),
]




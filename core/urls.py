from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('team-member-list/', views.evangelism_team_member_list, name='team_member_list'),
    path('team-member-create/', views.evangelism_team_member_create, name='team_member_create'),
    path('team-member-detail/<int:pk>/', views.evangelism_team_member_detail, name='team_member_detail'),
    path('team-member-update/<int:pk>/', views.evangelism_team_member_update, name='team_member_update'),
    path('team-member-delete/<int:pk>/', views.evangelism_team_member_delete, name='team_member_delete'),
    path('new-convert-list/', views.new_convert_list, name='new_convert_list'),
    path('new-convert-detail/<int:pk>/', views.new_convert_detail, name='new_convert_detail'),
]




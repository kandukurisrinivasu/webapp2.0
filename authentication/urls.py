# -*- encoding: utf-8 -*-
"""
MIT License
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import CalendarView,calendar_test, create_event,event_details, login_view, register_user,  edituser, import_xls, update,asset_search, asset_search_dispaly, add_asset, export_xls,export_pdf
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

#app_name = 'authentication'

urlpatterns = [
    path('login/', login_view, name="login"),   
    path('register/', register_user, name="register"),
    path('edituser/', edituser, name="edituser"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("update/<str:username>/", update, name="update"),
    path("asset_search/", asset_search, name="asset_search"),
    path("asset_search_dispaly/", asset_search_dispaly, name="asset_search_dispaly"),
    path("add_asset/", add_asset, name="add_asset"),
    path('export', export_xls, name='export'),
    path('export_pdf', export_pdf, name='export_pdf'),
    path('import_xls', import_xls, name='import_xls'),
    path('calendar_test', calendar_test, name='calendar_test'),
    path('event/new/', create_event, name='event_new'),
    path('event/<int:event_id>/details/', event_details, name='event-detail'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    #path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="account/core/password/password_reset_confirm.html"), name='password_reset_confirm'),
    #path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='account/core/password/password_reset_complete.html'), name='password_reset_complete'),      
    #path('calendar_test', CalendarView.as_view(), name='calcalendar_testendar'),
    #calendar

    #path('', views.home, name="home"),
    #path('login/', views.login_user, name='login'),
    #path('logout/', views.logout_user, name='logout'),
    #path('register/', views.register_user, name='register'),
    #path('edit_profile/', views.edit_profile, name='edit_profile'),
    #path('change_password', views.change_password, name='change_password'),
    #path('add_data', views.add_data, name='add_data'),
    #path('data_search', views.data_search, name='data_search'),
    #path('display', views.display, name='display'),
    #path('about', views.about, name='about'),
    #path('import', views.import_xls, name='import'),
    #path('contact', views.contact, name='contact'),
    #path("password_reset/", password_reset, name="password_reset"),
    #path("^password_reset/", auth_views.password_reset, name="password_reset"),
    #path("^password_reset/done/", auth_views.password_reset_done, name="password_reset_done"),
    #path("^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/", 
    # auth_views.password_reset_confirm, name='password_reset_confirm'),
    #path("^reset/done", auth_views.password_reset_complete, name='password_reset_complete'),
    
]

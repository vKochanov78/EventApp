from django.urls import path
from .views import (
    index_view,
    dashboard_view,

    event_create_view,
    event_details_view,
    event_edit_view,
    event_delete_view,

    profile_create_view,
    profile_details_view,
    profile_edit_view,
    profile_delete_view,
)


urlpatterns = [
    path('', index_view, name='index'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('create/', event_create_view, name='event_create'),
    path('details/<int:id>/', event_details_view, name='event_details'),
    path('edit/<int:id>/', event_edit_view, name='event_edit'),
    path('delete/<int:id>/', event_delete_view, name='event_delete'),
    path('profile/create/', profile_create_view, name='profile_create'),
    path('profile/details/', profile_details_view, name='profile_details'),
    path('profile/edit/', profile_edit_view, name='profile_edit'),
    path('profile/delete/', profile_delete_view, name='profile_delete'),

]
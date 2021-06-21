from django.urls import path
from . import views

app_name = __name__.split('.')[0]

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path(
        'create_room',
        views.RoomCreateView.as_view(),
        name='create_room'
    ),
    path(
        'create_room/room_list',
        views.RoomListView.as_view(),
        name='room_list'
    ),
]
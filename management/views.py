from management.models import Room
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, UpdateView, CreateView
from django.views.generic import ListView

from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.utils import timezone
from django.http import (
    HttpResponseRedirect,
    HttpResponseForbidden,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import PermissionDenied

from django.conf import settings
from .forms import RoomForm

class IndexView(
        TemplateView,
    ):
    """
    Displays the home page of NoraApp
    """
    template_name = 'web/index.html'


class RoomCreateView(
        CreateView,
    ):
    """Room Creation View
    Display a forms to create a room with start_date and options to choose
    """
    template_name = 'web/create_room.html'
    form_class = RoomForm

    def get_success_url(self):
        return reverse_lazy(
            'management:room_list'
        )

    def form_valid(self, form):
        form.save()
        return super(RoomCreateView, self).form_valid(form)


class RoomListView(
        ListView,
    ):
    """
    Display a list of all room that the user creates
    """
    model = Room
    template_name = "web/room_list.html"
import datetime
from datetime import timedelta

from decimal import Decimal
from django import forms
from django.forms import ModelForm
from django.forms import modelformset_factory
from django.contrib import messages
from django.utils import timezone
from django_select2.forms import Select2Widget, Select2MultipleWidget
from bootstrap_datepicker_plus import DatePickerInput

from .models import (
    Room

)

class RoomForm(ModelForm):
    """Form used to create a room"""

    class Meta:
        model = Room
        fields = ['name','capacity','status']

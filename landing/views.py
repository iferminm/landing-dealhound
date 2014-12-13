from django.shortcuts import render
from django.views.generic.edit import CreateView

from .mixins import AjaxResponseMixin
from .models import Lead


class LandingView(AjaxResponseMixin, CreateView):
    template_name = 'index.html'
    model = Lead
    fields = ('email',)

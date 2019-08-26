from django.shortcuts import render
from django.views.generic import ListView, DetailView
from minerals_app.models import Mineral


class MineralListView(ListView):
    model = Mineral
    template_name = 'minerals_app/index.html'
    context_object_name = 'minerals'

    def get_queryset(self):
        return Mineral.objects.all()


class MineralDetailView(DetailView):
    model = Mineral
    context_object_name = 'mineral'

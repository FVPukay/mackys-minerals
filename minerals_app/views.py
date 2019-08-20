from django.views.generic import ListView
from minerals_app.models import Mineral


class MineralListView(ListView):
    model = Mineral
    template_name='minerals_app/index.html'

    def get_queryset(self):
        return Mineral.objects.all()

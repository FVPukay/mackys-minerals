from django.views.generic import ListView
from minerals_app.models import MineralData


class MineralDataListView(ListView):
    model = MineralData
    template_name='minerals_app/index.html'

    def get_queryset(self):
        return MineralData.objects.all()

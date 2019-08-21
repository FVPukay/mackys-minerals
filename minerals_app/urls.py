from django.urls import path, re_path
from minerals_app import views

app_name = 'minerals'

urlpatterns = [
    re_path(r'^(?P<pk>\d+)/$', views.MineralDetailView.as_view(template_name='minerals_app/mineral_details.html'), name='detail'),
]

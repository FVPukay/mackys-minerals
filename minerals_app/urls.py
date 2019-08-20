from django.urls import path
from minerals_app import views

urlpatterns = [
    path('', views.MineralDataListView.as_view(), name='minerals_list'),
]

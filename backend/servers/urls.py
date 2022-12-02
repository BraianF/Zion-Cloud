from django.urls import path

from . import views

app_name = 'servers'
urlpatterns = [
    path('', views.ServerListCreateAPIView.as_view(), name='list-create'),
    path('<int:pk>', views.ServerDetailAPIView.as_view(), name='detail-update-destroy')
]

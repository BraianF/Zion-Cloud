from django.urls import path

from . import views

app_name = 'backups'
urlpatterns = [
    path('', views.BackupListCreateAPIView.as_view(), name='list-create'),
    path('<int:pk>', views.BackupDetailAPIView.as_view(), name='detail-update-drestry')
]

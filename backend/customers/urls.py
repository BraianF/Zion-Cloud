from django.urls import path

from . import views

app_name = 'customers'
urlpatterns = [
    path('', views.CustomerListCreateAPIView.as_view(), name='list-create'),
    path('<int:pk>', views.CustomerDetailAPIView.as_view(), name='detail-update-destroy'),
]

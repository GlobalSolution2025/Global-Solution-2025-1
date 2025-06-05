from django.urls import path
from .views import SensorDataAPIView

urlpatterns = [
    path('sensor/', SensorDataAPIView.as_view(), name='sensor-data'),
]

from django.urls import path, include
from .views import Conversions

# allowing Conversion class to handle requests to conversions page
urlpatterns = [
    path('', Conversions.as_view(), name='conversions'),
]

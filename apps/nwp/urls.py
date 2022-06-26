from django.urls import path
from . import views

urlpatterns = [
    path('',views.lobby),
    path('/nwp/',views.predict_next_word),
]
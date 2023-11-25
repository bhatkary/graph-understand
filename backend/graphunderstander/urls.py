from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('understand/', views.understand_graph)
]
from django.urls import path
from .views import PersonListView, PersonDetailView

urlpatterns = [
    path('api/', PersonListView.as_view(), name='person-list'),
    path('api/<int:pk>/', PersonDetailView.as_view(), name='person-detail'),
]
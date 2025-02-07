from django.urls import path
from .views import personal_info_view, travel_view, waste_view, energy_view, expenditure_view

urlpatterns = [
    path('', personal_info_view, name='personal_info'),
    path('travel/', travel_view, name='travel'),
    path('waste/', waste_view, name='waste'),
    path('energy/', energy_view, name='energy'),
    path('expenditure/', expenditure_view, name='expenditure'),
]

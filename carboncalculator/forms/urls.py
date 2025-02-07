from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('', views.personal_info_view, name='home'),
    path("travel_view/",views.travel_view,name='travel'),
    path("waste_view/",views.waste_view,name='waste'),
    path("energy_view/",views.energy_view,name='energy'),
    path("expenditure_view",views.expenditure_view,name='expenditure'),
    path("result/",views.result_view,name='result'),
]

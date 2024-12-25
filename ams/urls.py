from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('program/<int:program_id>/', program_detail, name='program_detail'),
    path('american-corners/', american_corner_list, name='american_corner_list'),   
]

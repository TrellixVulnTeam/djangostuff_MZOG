from django.urls import path
from .import views


# URL for the tanks app/tankbattle page
app_name = "tanks"

urlpatterns = [
    path('tankbattle/', views.tank_view, name='tank_battle'),
    path('tankbattle/', views.tank_1, name=('sim1')),
    path('tankbattle/', views.tank_2, name=('sim2')),
    path('tankbattle/', views.tank_3, name=('sim3')),
    path('tankbattle/', views.tank_4, name=('sim4')),

]

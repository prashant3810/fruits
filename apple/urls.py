from apple import views
from django.urls import path

urlpatterns = [

    path('types/', views.types,name='types'),
    path('apple_types/',views.apple_types,name='apple_types'),
    path('apple_colour/',views.apple_colour,name='apple_colour'),
    path('apple_grade/',views.apple_grade,name='apple_grade'),

    ]
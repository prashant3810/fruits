from juices import views

from django.urls import path
urlpatterns= [
    path('varaities/', views.varaities, name='varaities'),
    path('juices_colour/',views.varaities_colour,name='juices_colour'),
    path('juices_types/',views.varaities_types,name='juices_types'),
]

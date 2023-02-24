from django.urls import path, include
from . import views


app_name = 'hotel'
urlpatterns=[
    path('',views.HomeView.as_view(),name='home'),
    path('detail/<int:id>',views.DetailView.as_view(),name='detail'),
    path('reserved/<int:room_id>',views.ReservedView.as_view(),name='reserved'),

]
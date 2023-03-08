from django.urls import path, include
from . import views


app_name = 'hotel'
urlpatterns=[
    path('',views.HomeView.as_view(),name='home'),
    # path('reserved/',views.ReservedvApi.as_view(),name='reservedapi'),
    path('reserved/<int:room_number>',views.ReservedView.as_view(),name='reserved'),

]
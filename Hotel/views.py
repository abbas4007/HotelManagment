from django.shortcuts import render, redirect
from django.views import View

from .models import Room
# Create your views here.
class HomeView(View):

     def get(self,request):
         rooms = Room.objects.all()
         return render(request,'index.html',{"rooms":rooms})


class DetailView(View):
    def post(self,request,room_id):
        room = Room.objects.get(id == room_id)
        if room.is_availble == True :
            return redirect('hotel:reserved')



class ReservedView(View):
    def post(self, request, room_id):
        # room = Room.objects.get(id == room_id)
        return render(request,'reserved.html')
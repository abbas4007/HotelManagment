from django.shortcuts import render, redirect
from django.views import View
from .forms import AddForm
from .models import Room
# Create your views here.
class HomeView(View):

     def get(self,request):
         rooms = Room.objects.all()
         form = AddForm()

         return render(request,'index.html',{"rooms":rooms,'form':form})


class DetailView(View):
    def post(self,request,room_id):
        room = Room.objects.get(id == room_id)
        form = AddForm()

        if room.is_availble == True :
            form.save()
            return redirect('hotel:reserved',{'form':form})



class ReservedView(View):
    form_class = AddForm
    def dispatch(self, request, *args, **kwargs):
        room = Room.objects.get(pk = kwargs['room_id'])
        room.is_availble = False
        return render(request,'reserved.html',{'room':room})

        return super().dispatch(request, *args, **kwargs)

    def get(self,request,room_id):
        form =self.form_class
        return render(request,'reserved.html',{'form':form})

    def post(self, request, room_id):
        room = Room.objects.get(number = room_id)
        form = self.form_class(request.POST,instance=room)
        # print('***********')
        # print(room)
        if form.is_valid():
            new_room = form.save(commit=False)
            new_room.is_availble = False
            new_room.save()

        return redirect('hotel:home')
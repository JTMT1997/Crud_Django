from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from app.models import Data

class DataList(ListView):
    model = Data

class DataView(DetailView):
    model = Data

class DataCreate(CreateView):
    model = Data
    fields = ['name', 'age']
    success_url = reverse_lazy('data_list')

class DataUpdate(UpdateView):
    model = Data
    fields = ['name', 'age']
    success_url = reverse_lazy('data_list')

class DataDelete(DeleteView):
    model = Data
    success_url = reverse_lazy('data_list')
    
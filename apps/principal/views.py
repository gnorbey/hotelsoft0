from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, request
from apps.principal.models import Habitacion
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.principal.form import HabitacionForm
from django.urls import reverse_lazy
# Create your views here.
#from apps.principal.form import HabitacionList, NacionalidadList

def index(request):
    return HttpResponse('index')
    #return render(request, 'principal/habitacion_list.html')

def habitacion_view(request):
    if request.method == 'POST':
        form = HabitacionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('principal:habitacion_listar')
    else:
        form = HabitacionForm()
    return render(request, 'principal/habitacion_form.html', {'form': form})               

def habitacion_list(request):
    habitacion = Habitacion.objects.all().order_by('id')
    contexto = {'habitacion':habitacion}
    return render(request, 'principal/habitacion_list.html', contexto)



class HabitacionList(ListView):
    model = Habitacion
    template_name = 'principal/habitacion_list.html' 

class HabitacionCreate(CreateView):
    model = Habitacion
    form_class = HabitacionForm
    template_name = 'principal/habitacion_form.html' 
    success_url = reverse_lazy('habitacion_listar')

class HabitacionUpdate(UpdateView):
    model = Habitacion
    form_class = HabitacionForm
    template_name = 'principal/habitacion_form.html' 
    success_url = reverse_lazy('habitacion_listar')

class HabitacionDelete(DeleteView):
    model = Habitacion
    template_name = 'principal/habitacion_delete.html'
    success_url = reverse_lazy('habitacion_listar')


def habitacion_listar(request):
    habitacion=Habitacion.objects.all()
    contexto={'habitaciones': habitacion}
    return render(request, 'principal/habitacion_list.html', contexto) 

def habitacion_crear(request):
    form = HabitacionForm
    contexto = {
        'form':form
    }
    return render(request, 'principal/habitacion_form.html', contexto)

def habitacion_editar(request, id_habitacion):
    habitacion = Habitacion.objects.get(id=id_habitacion)
    if request.method == 'GET':
        form = HabitacionForm(instance=habitacion)
    else:
        form = HabitacionForm(request.POST, instance=habitacion)    
        if form.is_valid():
            form.save()
        return redirect('principal:habitacion_listar')
    return render(request, 'principal/habitacion_form.html')

def habitacion_delete(request, id_habitacion):
    habitacion = Habitacion.objects.get(id=id_habitacion)
    if request.method == 'POST':
        habitacion.delete()
        return redirect(habitacion_listar)
    return render(request, 'principal/habitacion_delete.html', {'principal': habitacion})


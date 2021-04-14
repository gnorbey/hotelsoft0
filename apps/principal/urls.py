from django.conf.urls import url, include
from apps.principal.views import index, HabitacionList, HabitacionCreate,  HabitacionUpdate, HabitacionDelete




urlpatterns= [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', HabitacionCreate.as_view(), name='habitacion_crear'),
    url(r'^listar$', HabitacionList.as_view(), name='habitacion_listar'),
    url(r'^editar/(?P<pk>\d+)/$', HabitacionUpdate.as_view(), name='habitacion_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', HabitacionDelete.as_view(), name='habitacion_eliminar'),
   
    #url(r'^listar$', habitacion_list, name='habitacion_listar'),
    

]
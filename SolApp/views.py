from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def mostrar_index(request):
    return render(request, 'SolApp/templates/SolApp/index.html')

#discos a reseñar


def we_opinion(request):

    if request.method == 'POST':

        formulario = WeForm(request.POST)
        
        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data
    
            we_opinion = We (publicacion=formulario_limpio['publicacion'], suscriptor=formulario_limpio['suscriptor'], critica=formulario_limpio['critica'])
    
            we_opinion.save()

            return render(request, 'SolApp/templates/SolApp/index.html')
    
    else:
        formulario = WeForm

    return render(request, 'SolApp/templates/SolApp/we_opinion.html', {'formulario': formulario})


def the_car_opinion(request):

    if request.method == 'POST':

        formulario = TheCarForm(request.POST)
        
        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data
    
            thecar_opinion = TheCar (publicacion=formulario_limpio['publicacion'], suscriptor=formulario_limpio['suscriptor'], critica=formulario_limpio['critica'])
    
            thecar_opinion.save()

            return render(request, 'SolApp/templates/SolApp/index.html')
    
    else:
        formulario = TheCarForm

    return render(request, 'SolApp/templates/SolApp/the_car_opinion.html', {'formulario': formulario})


def wotp_opinion(request):

    if request.method == 'POST':

        formulario = WOTPForm(request.POST)
        
        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data
    
            wotp_opinion = WOTP (publicacion=formulario_limpio['publicacion'], suscriptor=formulario_limpio['suscriptor'], critica=formulario_limpio['critica'])
    
            wotp_opinion.save()

            return render(request, 'SolApp/templates/SolApp/index.html')
    
    else:
        formulario = WOTPForm

    return render(request, 'SolApp/templates/SolApp/wotp_opinion.html', {'formulario': formulario})


def rhcp_opinion(request):

    if request.method == 'POST':

        formulario = RHCPForm(request.POST)
        
        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data
    
            rhcp_opinion = RHCP (publicacion=formulario_limpio['publicacion'], suscriptor=formulario_limpio['suscriptor'], critica=formulario_limpio['critica'])
    
            rhcp_opinion.save()

            return render(request, 'SolApp/templates/SolApp/index.html')
    
    else:
        formulario = WOTPForm

    return render(request, 'SolApp/templates/SolApp/rhcp_opinion.html', {'formulario': formulario})


def phoenix_opinion(request):

    if request.method == 'POST':

        formulario = PhoenixForm(request.POST)
        
        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data
    
            phoenix_opinion = Phoenix (publicacion=formulario_limpio['publicacion'], suscriptor=formulario_limpio['suscriptor'], critica=formulario_limpio['critica'])
    
            phoenix_opinion.save()

            return render(request, 'SolApp/templates/SolApp/index.html')
    
    else:
        formulario = PhoenixForm

    return render(request, 'SolApp/templates/SolApp/phoenix_opinion.html', {'formulario': formulario})

#suscriptor y posteo
def crear_suscriptor(request):

    if request.method == 'POST':

        formulario = CrearSuscriptorForm(request.POST)
        
        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            suscriptor = Suscriptor(nombre=formulario_limpio['nombre'], email=formulario_limpio['email'], fecha_nacimiento=formulario_limpio['fecha_nacimiento'], acepta_mails=formulario_limpio['acepta_mails'])

            suscriptor.save()

            return render(request, 'SolApp/templates/SolApp/index.html')

    else:
        
        formulario = CrearSuscriptorForm()

    return render(request, 'SolApp/templates/SolApp/suscriptor.html', {'formulario': formulario})

def crear_posteo(request):

    formulario = CrearPosteoForm()
    
    if request.method == 'POST':

        formulario = CrearPosteoForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            post = Posteo(id_post=formulario_limpio['id_post'], nombre=formulario_limpio['nombre'],fecha_publicacion=formulario_limpio['fecha_publicacion'],descripcion=formulario_limpio['descripcion'])

            post.save()

            return render(request,'SolApp/templates/SolApp/index.html')
        
    else:
            
        formulario = CrearPosteoForm()
        
        
    return render(request, 'SolApp/templates/SolApp/posteo.html', {'formulario': CrearPosteoForm})


#busquedas

def buscar_posteo(request):

    if request.GET.get('id_post', False):
        id_post = request.GET['id_post']
        posteos = Posteo.objects.filter(id_post__icontains=id_post)

        return render(request, 'SolApp/templates/SolApp/buscar_posteo.html', {'posteos':posteos})
    
    else:
        respuesta = 'No hay datos'
    return render(request, 'SolApp/templates/SolApp/buscar_posteo.html', {'respuesta': respuesta})


def buscar_suscriptor(request):

    if request.GET.get('email', False):
        email = request.GET['email']
        suscriptores = Suscriptor.objects.filter(email__icontains=email)

        return render(request, 'SolApp/templates/SolApp/buscar_suscriptor.html', {'suscriptores':suscriptores})
    
    else:
        respuesta = 'No hay datos'
    return render(request, 'SolApp/templates/SolApp/buscar_suscriptor.html', {'respuesta': respuesta})

#la otra opcion

#def buscar_posteo(request):
#    
#    if request.GET.get('id_post', False):
#        id_post = request.GET['id_post']
#        post = Posteo.objects.filter(id_post__icontains=id_post)
#        return render(request, 'buscar_posteo.html',{'buscar posteo':post})
#    else:
#        respuesta = 'No hay datos'
#    return render(request,'buscar_post.html', {'respuesta': respuesta})
from django.shortcuts import render
from .forms import PasajeroFormulario
from .models import Pasajero
from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.

def home_view(request):
    return render(request,"index.html",{})

def pasajeros(request):
    pasajeros = Pasajero.objects.all()

    if request.method == 'POST':
        formulario = PasajeroFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('pasajeros')  # importante

    else:
        formulario = PasajeroFormulario()

    return render(request, "pasajeros.html", {
        "pasajeros": pasajeros,
        "form": formulario
    })

def pasajerosCreate(request):
    if request.method == 'POST':
        formulario = PasajeroFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('pasajeros')
    else:
        formulario = PasajeroFormulario()

    return render(request, 'pasajerosCreate.html', {'form': formulario})

def pasajerosEdit(request, id):
    pasajeros = get_object_or_404(Pasajero, id = id)
    data = {
        'form' : PasajeroFormulario(instance=pasajeros)
    }
    if request.method == 'POST':
        formulario = PasajeroFormulario(data=request.POST, instance=pasajeros, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="pasajeros")

    return render(request,'pasajerosEdit.html',data)


def pasajerosDelete(request, id):
    pasajero = get_object_or_404(Pasajero, id=id)

    if request.method == 'POST':
        pasajero.delete()
        return redirect('pasajeros')

    return render(request, 'confirmar_eliminar.html', {'pasajero': pasajero})
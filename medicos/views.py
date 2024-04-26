from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from .models import Especialidades

@login_required
def cadastro_medico(request):
    if request.method == "GET":
        return render(request, 'cadastro_medico.html')
    
#        especialidades = Especialidades.objects.all()
#        return render(request, 'cadastro_medico.html', {'especialidades': especialidades})

# Create your views here.

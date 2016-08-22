from django.shortcuts import render
from .models import Paciente
#from .models import Medico
#from .models import Turnos
#from .models import Horario



def vistainicio(request):
        return render(request, 'consultorioodontologico/inicio.html', {})


def vistapaciente(request):
        paciente = Paciente.objects.all()
        return render(request, 'consultorioodontologico/paciente.html', {'paciente': paciente})
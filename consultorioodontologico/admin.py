from django.contrib import admin
from .models import Paciente
from .models import Medicos
from .models import Turno
from .models import Horario
from .models import Especialidad


admin.site.register(Paciente)
admin.site.register(Medicos)
admin.site.register(Turno)
admin.site.register(Horario)
admin.site.register(Especialidad)
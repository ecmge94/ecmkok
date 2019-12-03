from rest_framework.serializers import ModelSerializer
from El_Bosque_School.Apps.Sistema_Academico.models import *

class estudianteSerializer(ModelSerializer):

    class Meta:
        model= Estudiante
        fields = "__all__"
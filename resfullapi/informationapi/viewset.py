from rest_framework import viewsets
from . import models
from . import serializers

class TeacherViewsets(viewsets.ModelViewSet):
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer #with this we convert our information which we got from serializer into json format

#it will create few classes inside it like which are fetched according to situation!
#list(),reteive(),create(),update(),destroy()
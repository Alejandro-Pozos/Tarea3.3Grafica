from django.db import models

class Alumno(models.Model):
    idAlumno = models.IntegerField(primary_key=True)
    grupo = models.CharField(max_length=1)
    numLista = models.IntegerField()
    password = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.idAlumno}"


class CalifLog(models.Model):
    id_log = models.BigAutoField(primary_key=True)
    idAlumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    nivel = models.CharField(max_length=255)
    dificultad = models.CharField(max_length=255)
    calificacion = models.FloatField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.id_log}, {self.idAlumno}, {self.nivel}::{self.dificultad}, {self.calificacion} ({self.timestamp})"
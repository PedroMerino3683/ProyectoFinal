from django.db import models

# Create your models here.
class Clima(models.Model):
    temperatura = models.FloatField()
    presion = models.FloatField()
    humedad = models.FloatField()
    monoxidoCarbono = models.FloatField()
    fecha = models.DateTimeField(auto_now=False, auto_now_add=False)
    delegacion = models.CharField(max_length=50)

    def __str__(self):
        return "Delegacion: {} - Fecha: {}".format(self.delegacion, self.fecha)
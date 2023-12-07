from django.db import models

# Create your models here.
class Mensaje(models.Model):
    nombre_completo = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    asunto = models.CharField(max_length=255)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre_completo

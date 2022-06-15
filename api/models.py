from django.db import models

class Conversation(models.Model):
    nombre = models.CharField(max_length=30)
    numero = models.IntegerField()
    text = models.TextField()

    def __str__(self) -> str:
        return self.nombre

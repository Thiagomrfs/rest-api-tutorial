from django.db import models

class Todo(models.Model):
    priority_choices = [
        ("B", "Baixa"), 
        ("M", "Media"), 
        ("A", "Alta")
    ]

    titulo = models.CharField(max_length=20)
    description = models.CharField(max_length=80)
    priority = models.CharField(max_length=1, choices=priority_choices)

    def __str__(self):
        return self.titulo

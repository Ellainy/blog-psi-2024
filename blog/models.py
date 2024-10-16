from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='static/imgs')
    texto = models.TextField(max_length=1200)
    
    def __str__(self):
        return self.titulo

from django.db import models
from django.contrib.auth.models import User

# Campos de texto y fecha
class Pelicula(models.Model):
    titulo        = models.CharField(max_length=200)
    genero        = models.CharField(max_length=100)
    director      = models.CharField(max_length=100)
    fecha_estreno = models.DateField()

    def __str__(self):
        return self.titulo

# Campo relacionado al usuario, texto, numero y fecha (Se agrega automaticamente)
class Resena(models.Model): # Reseña de la pelicula
    usuario           = models.ForeignKey(User, on_delete=models.CASCADE)
    pelicula          = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    contenido         = models.TextField()
    calificacion      = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reseña de {self.usuario.username} para {self.pelicula.titulo}'

# Información extra para el usuario, como su biografia y una imagen de pefil
class UsuarioPerfil(models.Model):
    usuario   = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = models.TextField(blank=True, null=True)
    avatar    = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.usuario.username

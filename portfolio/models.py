from django.db import models

# Create your models here.
class Project(models.Model):
    titulo = models.CharField(max_length=50, verbose_name="Titulo")
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.ImageField(verbose_name="Imagen del producto" ,upload_to="projects")
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Proyecto skere"
        verbose_name_plural = "Proyectos skere"
        ordering = ["-create"]
    
    def __str__(self):
        return self.titulo
    
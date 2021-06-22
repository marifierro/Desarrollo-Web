from django.db import models

# Create your models here.

# Modelo para categoria
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name ="Nombre de la categoria")

    def __str__(self):
        return self.nombreCategoria

# modelo para libros
class Libro(models.Model):
    isbn = models.CharField(max_length=17, primary_key=True, verbose_name='isbnlibro')
    nombrelibro = models.CharField(max_length=50, verbose_name='Nombre libro')
    autor = models.CharField(max_length=20, null=True, blank=True, verbose_name='Autor')
    descripcion = models.CharField(max_length=20, null=True, blank=True, verbose_name='Descripción')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.isbn
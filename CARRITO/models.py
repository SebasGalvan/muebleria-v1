from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Categoria(models.Model):
    descripcion = models.TextField(max_length=100)
    def __str__(self):
        return f"{self.descripcion}"
        
    
    
class Producto(models.Model):
    titulo =  models.CharField(max_length=200)
    imagenProducto =  models.ImageField(upload_to='productos',blank = True, null = True)
    descripcion = models.CharField(max_length=254)
    precio =  models.FloatField()
    categoria = models.ForeignKey(Categoria,on_delete= models.CASCADE, null=False)
    created =  models.DateTimeField(auto_now_add=True)
    updated =  models.DateTimeField(auto_now_add=True)
        
    def __unicode__(self,):
            return str(self.imagenProducto)   
    def __str__(self):
        return f'{self.titulo} | {self.descripcion} | Categoria {self.categoria}'
    

    
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario')
    productos = models.ForeignKey(Producto, on_delete=models.CASCADE,related_name="carrito")
    cantidad =  models.IntegerField()
    
    
    def __srt__(self):
        return f'{self.usuario} | {self.productos} | {self.cantidad}' 
        
    
    class Meta:
        verbose_name='Carrito'
    
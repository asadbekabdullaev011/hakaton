from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length= 30 , verbose_name= "Category")

    def __str__(self):
        return self.title


class Meals(models.Model):
    title = models.CharField(max_length= 40 , verbose_name= "Называния Блюда")
    image = models.ImageField(upload_to='main', verbose_name= "Image")
    price = models.CharField(max_length=50, verbose_name= "Price")
    category = models.ForeignKey(Category, verbose_name= 'Category', on_delete = models.CASCADE)

class Client(models.Model):
    email = models.EmailField(max_length=40, verbose_name="email")
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и Время")
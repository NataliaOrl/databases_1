from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    price = models.FloatField(verbose_name="Цена")
    image = models.ImageField(upload_to="images", verbose_name="Внешний вид")
    release_date = models.DateField(verbose_name="Дата релиза")
    lte_exists = models.BooleanField(default=True, verbose_name="LTE")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return f'{self.name}, {self.price}₽'

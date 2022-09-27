from tabnanny import verbose
from django.db import models


class Category(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=100, null=False, blank=False)
    description = models.CharField(verbose_name='Описание', max_length=300, null=False, blank=False, default='')


    def __str__(self) -> str:
        return f'{self.title}, {self.description}'


class Product(models.Model):
    category = models.ForeignKey(verbose_name='Категория', to='market.Category', null=False, blank=False, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Наименование', max_length=100, null=False, blank=False)
    description = models.TextField(verbose_name='Описание', max_length=600, null=False, blank=False, default='')
    created_at = models.DateTimeField(verbose_name='дата и время создания', auto_now_add=True)
    price = models.DecimalField(verbose_name='Стоимость', max_digits=10, decimal_places=3, null=False, blank=False)
    image = models.CharField(verbose_name='Картинка', max_length=200,  null=False, blank=False, default='no image')


    def __str__(self) -> str:
        return f'{self.title}, {self.category}, {self.price}'

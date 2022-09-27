from tabnanny import verbose
from django.db import models


class Category(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=100, null=False, blank=False)
    description = models.CharField(verbose_name='Описание', max_length=300, null=False, blank=False, default='')


    def __str__(self) -> str:
        return f'{self.title}, {self.description}'

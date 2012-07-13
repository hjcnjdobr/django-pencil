# coding: utf-8
from django.db import models

from sorl.thumbnail import ImageField


class Picture(models.Model):

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ('-id',)
    
    file = ImageField(u'файл',upload_to='pencil/picture')
    
    def __unicode__(self):
        return self.file.path.split('/')[-1]

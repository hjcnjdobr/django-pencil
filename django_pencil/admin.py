# -*- coding: utf-8 -*-
from django import forms
from django.db import models
from django.conf import settings
from django.contrib import admin
from django.contrib import messages



from sorl.thumbnail import get_thumbnail

from .models import Picture


class PictureAdmin(admin.ModelAdmin):

    list_display = ('display_thumb', 'display_filename', 'display_url', 'id',)
    list_display_links = ()
    
    def display_thumb(self, obj):
        image = getattr(obj, 'file', None)
        if image:
            t = get_thumbnail(image,"50x50",crop='center', quality=99)
            return u'<a href="%s"><img src="%s" /></a>' % (image.url, t.url)
        else:
            return u"Нет"
    display_thumb.short_description = u'Изображение'
    display_thumb.allow_tags = True

    def display_filename(self, obj):
        image = getattr(obj, 'file', None)
        if image:
            return image.path.split('/')[-1]
        return ''
    display_filename.short_description = u'Имя файла'
    display_filename.allow_tags = True

    def display_url(self, obj):
        image = getattr(obj, 'file', None)
        if image:
            return '<a href="%s" target="_blank">%s</a>' % (image.url, image.url)
        return ''
    display_url.short_description = u'Ссылка'
    display_url.allow_tags = True
    
    
    def save_model(self, request, obj, form, change):
        if obj.pk:
            messages.error(request, u'Созданное изображение не может быть изменено.')
        else:
            super(PictureAdmin, self).save_model(request, obj, form, change)
        


admin.site.register(Picture, PictureAdmin)


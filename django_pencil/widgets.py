# coding: utf-8
from django.forms import widgets
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django.utils import simplejson as json
from django.conf import settings


JQUERY_URL = getattr(settings, 'JQUERY_URL', 'https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js')
JQUERY_FORM_URL = getattr(settings, 'JQUERY_FORM_URL', 'http://malsup.github.com/jquery.form.js')


class PencilTextarea(widgets.Textarea):

    class Media:
        js = (
            JQUERY_URL,
            JQUERY_FORM_URL, 
            settings.STATIC_URL + 'pencil/pencil.js',
        )
        css = {
            'all': (
                settings.STATIC_URL + 'pencil/pencil.css',
            ),
        }
        
    def __init__(self, attrs=None):
        default_attrs = {'cols': '100', 'rows': '23'}
        if attrs:
            default_attrs.update(attrs)
        super(PencilTextarea, self).__init__(default_attrs)
        
    def render(self, name, value, attrs=None):
        output = super(PencilTextarea, self).render(name, value, attrs)
        output += """
        <script>
            $(function(){
                var editor_%(id)s = $('#%(id)s').pencil({
                    'uploaderUrl': '%(uploader_url)s'
                });
                //editor = editor_%(id)s; // DEBUG
            });
        </script>
        <style>
            .pencil_wrapper{float: left;}
            .pencil_toolbar{margin-left: 0 !important; padding-left: 0 !important;}
            .pencil_modal table td{border: none; vertical-align: middle;}
            .pencil_div p{margin-left: 0 !important; padding: 5px 0 5px 0 !important;}
            .pencil_switch li{list-style-type: none !important;}
        </style>
        """ % {
            'id': attrs['id'], 
            'uploader_url':reverse('pencil:upload')
        }
        return mark_safe(output)


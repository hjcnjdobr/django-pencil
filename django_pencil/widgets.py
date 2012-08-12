# coding: utf-8
from django.forms import widgets
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django.utils import simplejson as json
from django.conf import settings


PENCIL_JQUERY_URL = getattr(settings, 'PENCIL_JQUERY_URL', settings.STATIC_URL + 'js/jquery.min.js')
PENCIL_JQUERY_FORM_PLUGIN_URL = getattr(settings, 'PENCIL_JQUERY_FORM_PLUGIN_URL',  settings.STATIC_URL +'js/jquery.form.js')
PENCIL_JS_URL = getattr(settings, 'PENCIL_JS_URL', settings.STATIC_URL + 'pencil/pencil.js')


class PencilTextarea(widgets.Textarea):

    class Media:
        js = (
            PENCIL_JQUERY_URL,
            PENCIL_JQUERY_FORM_PLUGIN_URL,
            PENCIL_JS_URL,
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
	    .pencil_div p{font-size: 13px !important;}
        </style>
        """ % {
            'id': attrs['id'], 
            'uploader_url':reverse('pencil:upload')
        }
        return mark_safe(output)


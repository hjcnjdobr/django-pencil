# coding: utf-8
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson

from .forms import PictureForm

@login_required
@csrf_exempt
def upload_image(request):
    form = PictureForm(request.POST or None, request.FILES)
    if form.is_valid():
        img = form.save()
        data = {'url': img.file.url}
    else:
        data = {'error': u'Файл не является изображением.'}
        
    return HttpResponse(simplejson.dumps(data), content_type='text/plain; charset=utf-8')


# django-pencil

Integration Pencil WYSIWYG into Django.

## Requirements

- sorl-thumbnail

## Installation

### settings.py

    INSTALLED_APPS = (
        ...
        'sorl.thumbnail',
        'django_pencil',
    )

### urls.py

    urlpatterns = patterns('',
        ...
        url(r'^pencil/', include('django_pencil.urls', namespace='pencil')),
    )

### Download Pencil to your STATIC_DIR

- https://github.com/un1t/pencil

### Download jQuery and jQuery Form Plugin to your STATIC_DIR/js
    
- https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js
- http://malsup.github.com/jquery.form.js

### Syncdb

    manage.py syncdb

### Use widgets

Add widget to admin.py

    from django_pencil.widgets import PencilTextarea

    class PageAdminForm(forms.ModelForm):
        
        class Meta:
            model = Page
            widgets = {'content':PencilTextarea}


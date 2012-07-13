# django-pencil

Integration Pencil WYSIWYG into Django.


## Installation

### Step 1
settings.py

    INSTALLED_APPS = (
        ...
        'django_pencil',
    )

### Step 2
urls.py

    urlpatterns = patterns('',
        ...
        url(r'^pencil/', include('django_pencil.urls', namespace='pencil')),
    )

### Step 3
Also you need to download [Pencil](https://github.com/un1t/pencil) WYSIWYG to your STATIC_ROOT.

### Step 4
    manage.py syncdb

### Step 5
Add widget to admin.py

    from django_pencil.widgets import PencilTextarea

    class PageAdminForm(forms.ModelForm):
        
        class Meta:
            model = Page
            widgets = {'content':PencilTextarea}


# Django-md-editor

> Django-md-editor package helps integrate [editor.md](https://github.com/pandao/editor.md) with Django.

## Getting started

Install the package:

  `pip install django-md-editor`


Add `djmd` to INSTALLED_APPS in `settings.py`.


## Usage

1. Usage in models

```python
from djmd.models import EditorMdField


class Page(models.Model):
    content_editormd1 = EditorMdField()
```

2. Usage in forms

```python
from djmd.fields import EditorMdFormField


class PageForm(forms.ModelForm):
    content_editormd1 = EditorMdFormField()
    content_editormd2 = EditorMdFormField()
    content_editormd3 = EditorMdFormField()

    class Meta:
        model = Page
        fields = '__all__'


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    form = PageForm
```

3. To show detail page your web site
- install djmd_tags
`{% load djmd_tags %}`
- and use
```
{{ content|md_detail:"content"|safe }}
```

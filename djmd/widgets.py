from django import forms
from django.conf import settings
from django.contrib.admin import widgets as admin_widgets
from django.forms.utils import flatatt
from django.utils.html import conditional_escape

try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_unicode as force_text
from django.utils.safestring import mark_safe


class EditorMdWidget(forms.Textarea):
    def __init__(self, attrs=None):
        super(EditorMdWidget, self).__init__(attrs)

    def build_attrs(self, base_attrs, extra_attrs=None, **kwargs):
        attrs = dict(base_attrs, **kwargs)
        if extra_attrs:
            attrs.update(extra_attrs)
        return attrs

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(self.attrs, attrs, name=name)
        html =  """
          <script src='/static/jquery.min.js'></script>
          <link href="/static/css/editormd.css" type="text/css" media="all" rel="stylesheet">
          <script type="text/javascript" src="/static/editormd.min.js"></script>
            <div id="%(id)s_editormd" class="editormd">
                <textarea %(attrs)s style="display:none;">%(body)s</textarea>
            </div>
            <script type="text/javascript">$(function() {
              var Editor = editormd('%(id)s_editormd', {
                height: 670,
                path : '%(path)s',
                htmlDecode: "html,iframe",
                emoji : true,
                atLink: false,
                emailLink : false
              });
              var lang = "en";
              var path  = "/static/languages/en";
              editormd.loadScript(path, function() {
                Editor.lang = editormd.defaults.lang;
                Editor.recreate();
                });
            });
            </script>
            """% {
            'path': settings.STATIC_URL + 'lib/',
            'attrs': flatatt(final_attrs),
            'body': conditional_escape(force_text(value)),
            'id': attrs['id'],
            }
        return mark_safe(html)

class AdminEditorMdWidget(EditorMdWidget, admin_widgets.AdminTextareaWidget):
    def __init__(self, attrs=None):
        super(AdminEditorMdWidget, self).__init__(attrs)

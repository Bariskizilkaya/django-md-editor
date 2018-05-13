from django import template
from django.conf import settings
register = template.Library()

@register.filter(name="md_detail")
def md_detail(value, arg):
    html = """
      <script src='%(direkt_path)sjquery.min.js'></script>
      <link href="%(direkt_path)scss/editormd.css" type="text/css" media="all" rel="stylesheet">
      <script type="text/javascript" src="%(direkt_path)seditormd.min.js"></script>
      <script type="text/javascript" src="%(path)s/codemirror/codemirror.min.js"></script>
      <script type="text/javascript" src="%(path)s/codemirror/modes.min.js"></script>
      <script type="text/javascript" src="%(path)s/codemirror/addons.min.js"></script>
      <script type="text/javascript" src="%(path)s/marked.min.js"></script>
      <script type="text/javascript" src="%(path)s/prettify.min.js"></script>
      <script type="text/javascript" src="%(path)s/raphael.min.js"></script>
      <script type="text/javascript" src="%(path)s/underscore.min.js"></script>
      <script type="text/javascript" src="%(path)s/flowchart.min.js"></script>
      <script type="text/javascript" src="%(path)s/jquery.flowchart.min.js"></script>
      <script type="text/javascript" src="%(path)s/sequence-diagram.min.js"></script>
     <div id="%(id)s" style="width: auto" class="editormd">
        <textarea style="display:none;">%(body)s</textarea>
    </div>
    <script type="text/javascript">
    $(function() {
    var Editor = editormd.markdownToHTML("%(id)s", {
    height: 670,
    path : "%(path)s/",
    htmlDecode: "html,iframe",
    atLink: false,
    emailLink : false
    });
    });
    </script>"""%{
    'body':value,
    'path':settings.STATIC_URL + 'lib',
    'direkt_path':settings.STATIC_URL,
    'id':'id_'+arg+'_editormd'
    }
    return html

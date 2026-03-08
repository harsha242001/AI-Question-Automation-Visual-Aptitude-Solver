from jinja2 import Template

def render_html(template_path, data):
    with open(template_path, 'r', encoding='utf-8') as f:
        template = Template(f.read())
    return template.render(**data)

from jinja2 import Environment, FileSystemLoader
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent  

templates = Environment(loader=FileSystemLoader(BASE_DIR / "template"))

def render_verification_email(name: str, code: str, expires_at: datetime, templateName):
    template = templates.get_template(templateName)
    return template.render(
        name=name,
        code=code,
        expires_at=expires_at.strftime("%H:%M:%S %d/%m/%Y"),
        now=datetime.now()  
    )





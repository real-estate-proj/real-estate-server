from fastapi_mail import FastMail, MessageSchema, MessageType
from core.config.smtp import conf
from schemas.email.emailSchema import EmailSchema

async def sendEmail(data: EmailSchema):
    message = MessageSchema(
        subject=data.subject,
        recipients=[data.email],
        body=data.content,
        subtype=MessageType.html 
    )

    fm = FastMail(conf)
    await fm.send_message(message)


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class MyEmail(object):
    """
    -------------------------------------------------------------------------
    Atributes in **kwargs:
    
    from_addr: str - object email address
    
    to_addr: str - subject email address
    
    mail_subject: str - theme of mail
    
    mail_text: str - text of mail message
    
    mail_api_pswd: str - password of api connection to object email address
    
    -------------------------------------------------------------------------
    Methods:
    
    send_email(send_email_addr: str = None)
    
    ## Send prepare email message from object email address to subject
    
    -------------------------------------------------------------------------
    
    """
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        
    def send_email(self, send_email_addr: str = None):
        if send_email_addr is None:
            send_email_addr = self.to_addr
            
        msg = MIMEMultipart()
        msg['From'] = self.from_addr
        msg['To'] = send_email_addr
        msg['Subject'] = self.mail_subject
        msg.attach(MIMEText(self.mail_text, 'plain'))

        server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
        server.login(self.from_addr, self.mail_api_pswd)
        text = msg.as_string()
        server.sendmail(self.from_addr, send_email_addr, text)
        server.quit()
        return 'Message to {to} send!'.format(to=send_email_addr)
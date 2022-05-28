import toml
from bin.mail import MyEmail


email_args = toml.load('./config.toml')

email = {
    'from_addr': email_args['user']['email'],
    'to_addr': "to_addr",
    'mail_subject': "Subject",
    'mail_text': "Print text here",
    'mail_api_pswd': email_args['user']['password'],
}

emailObj = MyEmail(**email)

emailObj.send_email()
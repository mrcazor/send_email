# Send Email Intro

1)  Открыть почту и создать пароль приложения

    - в mail это можно сделать так: Аккаунт -> Пароль и безопасность
      -> Способы входа -> пароли от внешних приложений
      
    - далее по инструкции добавить внешнее подключение
    
    - пароль от внешнего соединения будет использоваться для подключения к серверу отправки сообщений smtp.mail.ru
    
2) В отличие от Gmail - Mail.ru использует TLS соединение на 465 порту, поэтому обьект соединенияя:
    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    
3) Логика отправки сообщения завернута для простоты в класс MyEmail в модуле myemail


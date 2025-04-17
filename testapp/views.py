from django.shortcuts import render
from django.core.mail import EmailMessage, get_connection, EmailMultiAlternatives, send_mail, send_mass_mail
from django.template.loader import render_to_string

def test_cookie(request):
    # if request.method == 'POST':
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        print("Браузер поддерживает cookie")
    else:
        print("Браузер не поддерживает cookie")

    request.session.set_test_cookie()

    return render(request, 'testapp/test_cookie.html')


# Низкоуровневый способ отправки почты

# def email(request):
    # 1 var
    # em = EmailMessage(subject='Test', body='Test Body', to=['user@supersite.kz'])
    # em.send()
    
    
    # 2 var
    # em = EmailMessage(subject='Ваш новый пароль', 
    #                   body='Ваш новый пароль находится во вложении', 
    #                   attachments=[('password.txt', '1234', 'text/plain')], 
    #                   to=['user@supersite.kz'])
    # em.send()
    
    # 3 var
    # em = EmailMessage(subject='Запрошен вами файл', 
    #                   body='Получите файл, который вы запросили', 
    #                   to=['user@supersite.kz'])
    # em.attach_file(r'C:\Work\file.txt')
    # em.send()
    
    
    # return render(request, 'testapp/test_cookie.html')
    

# def email(request):
    # context = {'user': 'Вася Пупкин'}
    # s = render_to_string('email/letter.txt', context)
    # em = EmailMessage(subject='Оповещение', 
    #                   body=s, 
    #                   to=['vpupkin@othersite.kz'])
    # em.send()
    
    
    
    # Рассылка
    
    # 1 variant
    
    # con = get_connection()
    # con.open()
    # em1 = EmailMessage(subject='Оповещение', 
    #                   body='Тестовое сообщение', 
    #                   to=['vpupkin@othersite.kz'],
    #                   connection=con)
    # em1.send()
    
    # em2 = EmailMessage(subject='Оповещение', 
    #                   body='Тестовое сообщение', 
    #                   to=['vpupkin@othersite.kz'],
    #                   connection=con)
    # em2.send()
    
    # em3 = EmailMessage(subject='Оповещение', 
    #                   body='Тестовое сообщение', 
    #                   to=['vpupkin@othersite.kz'],
    #                   connection=con)
    # em3.send()
    
    # con.close()
    
    # 2 variant
    # con = get_connection()
    # con.open()
    # em1 = EmailMessage(...)
    # em2 = EmailMessage(...)
    # em3 = EmailMessage(...)
    # con.send_messages([em1, em2, em3])
    # con.close()
    
    
    # 3 variant
    # em = EmailMultiAlternatives(subject='Оповещение', 
    #                             body='Тестовое сообщение', 
    #                             to=['vpupkin@othersite.kz'])
    
    # em.attach_alternative('<h1>Test message</h1>', 'text/html')
    # em.send()
    
    # return render(request, 'testapp/test_cookie.html')


# высокоуровневый способ отправки почты

def email(request):
    # send_mail('test mail', 'test!!!', 'webmaster@localhost', ['vpupkin@mail.ru'], html_message='<h1>Test message</h1>')
    
    # Рассылка через высокоуровневый способ
    # msg1 = ('Подписка', 'Подтвердите подписку', 'webmaster@localhost', ['vpupkin1@mail.ru', 'vpupkin2@mail.ru'])
    # msg2 = ('Отписка', 'Подтвердите отписку', 'webmaster@localhost', ['vpupkin1@mail.ru', 'vpupkin2@mail.ru'])
    # send_mass_mail([msg1, msg2])

    
    
    return render(request, 'testapp/test_cookie.html')

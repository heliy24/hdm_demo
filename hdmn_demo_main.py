import requests

#url = 'https://hidemyname.org/ru/demo/' #to 30.08.2025
#url = 'https://hxdemy.name/demo/'# from 30.08.2025 to 25.09.2025
#url = 'https://hide-my-name.org/demo/' # from 25.09.2025
#url = 'https://hide-my-name.com/demo/' # from 06.10.2025
#url = 'https://hide-my-name.org/demo/' # from 23.10.2025
url = 'https://hide-my-name.com/' # from 01.02.2026
#url = 'https://safeclick.email/' # from 01.02.2026

if 'Ваша электронная почта' in requests.get(url).text:
    
    email = input('Введите электронную почту для получения тестового периода: ')

    response = requests.post('https://hide-my-name.org/demo/success/', data={
        "demo_mail": f"{email}"
    })

    if 'Ваш код выслан на почту' in response.text:
        confirm = input('Введите полученную ссылку для подтверждения e-mail адреса: ')
        
        while True:
            try:
                response = requests.get(confirm)
                if 'Спасибо' in response.text:
                    print('Почта подтверждена. Код отправлен на вашу почту!')
                    break
                else:
                    confirm = input('Ссылка невалидная, повторите попытку: ')
            except:
                confirm = input('Ссылка невалидная, повторите попытку: ')
                continue


    else:
        print('Указанная почта не подходит для получения тестового периода ')

else:
    print('Невозможно получить тестовый период')

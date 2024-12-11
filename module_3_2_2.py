def send_email(message,recipient, *,sender="university.help@gmai.com"):

    if "@" not in sender or not (sender.endswith(".com") or  sender.endswith(".ru") or  sender.endswith(".net")):
        return f"Невозможно отправить письмо с адреса {sender}"
    if "@" not in recipient or not(recipient.endswith(".com") or  recipient.endswith(".ru") or  recipient.endswith(".net")):
        return f"Невозможно отправить письмо с адреса {sender} на адрес {recipient} "
    if  sender==recipient:
        return f"Невозможно отправить письмо самому себе"

    return f"Письмо отправлено от {sender} к {recipient} с сообщением {message}"
print(send_email("Привет!как дела?", "olvol54@yandex."))
print(send_email("Это тест","olvol54@yndex.ru",sender="universty.help@gmail."))
print(send_email("Это тест","university.help@gmail.com",sender="university.help@gmail.com"))
print(send_email("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ","olvol54@yandex.ru",sender="university.help@gmail.com"))
print(send_email("Письмо успешно отправлено","olvol54@yandex.ru"))





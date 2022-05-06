opção = str(input("Digite a sua opção:\n"))

if opção == "play1":
    from datetime import datetime
    from time import strftime

    print("www.eupodiatamatando.com".split('.'))
    print("19:16:23".split(':'))

    hora, minuto, segundos = "19:16:23".split(':')
    print(hora,"Horas.")
    print(minuto,"Minutos.")
    print(segundos,"Segundos.","\n")

    hora = datetime.now()
    print(hora)

    hora_texto = hora.strftime('%d/%m/%y %H:%M:%S')
    print(hora_texto)
    hora_texto2 = hora.strftime('%H:%M:%S')
    print(hora_texto2)

    hora, minuto, segundos = hora_texto2.split(':')
    print(hora,"Horas.")
    print(minuto,"Minutos.")
    print(segundos,"Segundos.","\n")
else:
    from datetime import *
    from time import strftime

    print("19:16:23".split(':'))
    hora, minuto, segundos = "19:16:23".split(':')
    print(hora,"Horas.")
    print(minuto,"Minutos.")
    print(segundos,"Segundos.","\n")

    now = datetime.now()
    print("Ano:",now.year)
    print("Mês:",now.month)
    print("Dia:",now.day)
    print("Hora:",now.hour)
    print("Min:",now.minute)
    print("Seg",now.second)
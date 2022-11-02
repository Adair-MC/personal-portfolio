""" login.py - Un extractor de nombre de usuario dado un email. """

def user():
    email_given = input('Ingrese su correo electrónico. Luego recibirá su nombre de usuario.\n >> ')
    for ch in email_given:
        if ch == "@":
            break
        else:
            print(ch, end="")
    print('\n')
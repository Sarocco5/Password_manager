import pyperclip
import keyring

# https://haveibeenpwned.com/


def aggiunta_password(mail):
    service_id = input("Inserire nome del servizio: ")
    password = input("Inserire password: ")
    keyring.set_password(service_id, mail, password)


def check_scelta_menu(lista):
    try:
        if lista == ["aggiungere password", "scegliere password"]:
            print("Vuoi aggiungere password o scegliere password?")
            for numero, opzione in enumerate(lista):
                print(f'[{numero}] - {opzione}')
            scelta = int(input("Inserire scelta: "))
            while scelta not in range(len(lista)):
                scelta = int(input("Scelta errata! Inserire scelta: "))
            return lista[scelta]
    except (ValueError, AttributeError):
        print("Scelta errata o inesistente. \n")
        menu()


def menu():
    mail = input("Inserire mail: ")
    start = check_scelta_menu(["aggiungere password", "scegliere password"])
    if start == "aggiungere password":
        aggiunta_password(mail)
    elif start == "scegliere password":
        scelta_sito(mail)


def scelta_sito(mail):
    sito_scelto = input("Inserisci il sito: ")
    password_scelta = keyring.get_password(sito_scelto, mail)
    pyperclip.copy(password_scelta)
    print("\nPassword trovata! Sei pronto ad incollarla.")
    input("Premi invio per terminare.")


if __name__ == '__main__':
    menu()

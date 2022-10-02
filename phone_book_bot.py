import sys

CONTACTS = {}


def corrector(handler):
    def wrapper(*args, **kwargs):
        try:
            handler(*args, **kwargs)
        except IndexError:
            print('Erorr. \nYou should enter Name and Phone diveded by space!')
        except Exception as error:
            print(f'Error {error}! \nEnter command once again, please.')
    return wrapper


def exit_func():
    sys.exit('Work done. Bye!')


@corrector
def add_contact_handler():
    name = input('Enter Name: ')
    phone = input('Enter phone number: ')
    CONTACTS[name] = phone
    print('New contact was added')


@corrector
def find_contact_handler():
    name = input('Enter Name: ')
    if name in CONTACTS:
        phone = CONTACTS[name]
        print(f'Phone number: {phone}')
    else:
        print(f'There is no such Name {name} in Phone Book')


@corrector
def change_contact_handler():
    user_input = input('Enter name and phone diveded by space: ')
    name_phone = user_input.split(' ')
    new_name = name_phone[0]
    new_phone = name_phone[1]
    if new_name in CONTACTS:
        CONTACTS.update({new_name: new_phone})
        print(f'Phone number was changed for the Name: {new_name}')
    else:
        print('There is no such Name in Phone Book')


@corrector
def hello_handler():
    print('Hello! How can I help you?')


@corrector
def all_contacts_show_handler():
    if len(CONTACTS) > 0:
        header = '| {:^15}| {:^15}|\n'.format('Name', 'Phone') + 35*'-'
        print(header)
        for k, v in CONTACTS.items():
            line = ('| {:<15}| {:<15}|'.format(k, v))
            print(line)
    else:
        print('There are no contacts in the phone book yet')


def main():
    commands = {
        'exit': exit_func,
        'close': exit_func,
        'good bye': exit_func,
        'add': add_contact_handler,
        'phone': find_contact_handler,
        'change': change_contact_handler,
        'hello': hello_handler,
        'show all': all_contacts_show_handler
    }

    while True:
        user_input = input('Enter your command: ')
        key = user_input.lower()
        if key not in commands:
            print('Unknown command!')
            continue
        commands[key]()


if __name__ == '__main__':
    main()

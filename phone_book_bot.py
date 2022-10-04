import sys

CONTACTS = {}


def corrector(handler):
    def wrapper(*args, **kwargs):
        try:
            handler(*args, **kwargs)
        except IndexError:
            print('Erorr. \nYou should enter Name and Phone number diveded by space!')
        except KeyError:
            print('There is no such Name in Phone Book')
        except Exception as error:
            print(f'Error {error}! \nEnter command once again, please.')
    return wrapper


def exit_func():
    sys.exit('Work done. Bye!')


@corrector
def add_contact_handler(contact_info):
    name = contact_info[0]
    phone = contact_info[1]
    CONTACTS[name] = phone
    print('New contact was added')


@corrector
def find_contact_handler(contact_info):
    name = contact_info[0]
    phone = CONTACTS[name]
    print(f'Phone number: {phone}')


@corrector
def change_contact_handler(contact_info):
    name = contact_info[0]
    new_phone = contact_info[1]
    old_phone = CONTACTS[name]
    CONTACTS[name] = new_phone
    print(f'Phone number "{old_phone}" was changed for "{name}"')


@corrector
def hello_handler(contact_info):
    print('Hello! How can I help you?')


@corrector
def all_contacts_show_handler(contact_info):
    if len(CONTACTS) > 0:
        header = '| {:^15}| {:^15}|\n'.format('Name', 'Phone') + 35*'-'
        print(header)
        for k, v in CONTACTS.items():
            line = ('| {:<15}| {:<15}|'.format(k, v))
            print(line)
    else:
        print('There are no contacts in the phone book yet')


COMMANDS = {
    'exit': exit_func,
    'close': exit_func,
    'good bye': exit_func,
    'add': add_contact_handler,
    'phone': find_contact_handler,
    'change': change_contact_handler,
    'hello': hello_handler,
    'show all': all_contacts_show_handler
}


def main():

    while True:
        user_input = input('Enter command and info: ')
        command_info = user_input.lower()
        for key in COMMANDS:
            if command_info.find(key) == 0 and command_info[len(key):len(key)+1].isalnum() == False:
                command = key
                contact_info = user_input[len(key):].split()
                COMMANDS[command](contact_info)
                break
        else:
            print("Command isn't correct!")


if __name__ == '__main__':
    main()

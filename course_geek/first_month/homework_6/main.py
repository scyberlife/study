contacts = [
    {'name': 'Geektech', 'phone': '0507052018'},
    {'name': 'Emergency services', 'phone': '911'},
    {'name': 'Fire department', 'phone': '101'},
]

def find_contact(name):
    for i in range(0, len(contacts)):
        if name in contacts[i].values():
            return True, i
        else:
            return False, i

while True:
    for _ in contacts:
        print(_)
    commands = int(input((f'1) create\n'
                    f'2) edit\n'
                    f'3) delete\n'
                    f'4) exit\n')))
    if commands == 1:
        name2 = input("Enter the name: ")
        name1 = input("Enter the phone number: ")
        list_one = []
        def create(name, number):
            if not (find_contact(name))[0]:
                return contacts.append({'name': name, 'phone': number})
            else:
                list_one.append(contacts[(find_contact(name2))[1]].get('phone'))
                list_one.append(number)
                return contacts[(find_contact(name2))[1]].update({'name': name, 'phone': list_one})
        create(name2, name1)
    if commands == 2:
        name2 = input("Enter the name: ")
        def edit(name):
            a = input("Enter new name: ")
            b = input("Enter new phone number: ")
            if (find_contact(name))[0] and not (find_contact(a))[0] and not(find_contact(b))[0]:
                return contacts[(find_contact(name2))[1]].update({'name': a, 'phone': b})
        edit(name2)
    if commands == 3:
        name2 = input("Enter the name: ")
        def delete (name):
            del contacts[(find_contact(name2))[1]]
        delete(name2) if not contacts[(find_contact(name2))[0]] else print('Name not found')
    if commands == 4:
        break
    else:
        print('')
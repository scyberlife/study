ten = list(range(1, 11))
evens = list(filter(lambda x: x % 2 == 0, ten))
print(list(map(lambda x: x**2, evens)))

def fun(o, ten=ten):
    return ten[o]

while True:
    try:
        ind = int(input('Enter the index number: '))
        print(fun(ind))
    except ValueError:
        print('Only integers allowed')
    except IndexError:
        print(f'Index can be from 0 to {len(ten)-1}')
from ordered_set import OrderedSet

x = [3, 6, 10, 2]

def iterations() -> None:
    try:
        it = iter(x)
        print(f'{x = }, {it = }')
        print(f'{next(it) = }')
        print(f'{next(it) = }')
        print(f'{next(it) = }')
        print(f'{next(it) = }')
        print(f'{next(it) = }')
    except StopIteration:
        print('stop')

    try:
        it = iter(x)
        iterator = True

        while iterator:
        print(f'{next(it) = }')
    except StopIteration:
        print('stop')

    for elem in x:
        print(f'{elem = }')
    else:
        print('stop')

def main() -> None:
    iterations()

    o = OrderedSet(['one', 'two', 'three', 'four', 'five'])
    it2 = iter(o)
    print(f'{next(it2) = }')
    print(f'{next(it2) = }')

    for str_elem in o:
        print(f'{str_elem = }')

if __name__ == '__main__':
    main()
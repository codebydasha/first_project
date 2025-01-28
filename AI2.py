grocery = []


def add():
    item = input('What will be added?: ')
    grocery.append(item)


def remove():
    maara = len(grocery)
    print('There are', maara, 'items in the list.')
    number = int(input('Which item is deleted?: '))
    try:
        grocery.pop(number)
    except IndexError:
        print('Incorrect selection.')


def main():
    while True:
        print("Would you like to")
        print("(1)Add or")
        print("(2) Remove items or")
        vastaus = input("(3) Quit?: ")
        if vastaus == '3':
            print('The following items remain in the list: ')
            for item in grocery:
                print(item)
            break
        elif vastaus == '1':
            add()
        elif vastaus == '2':
            remove()
        else:
            print('Incorrect selection.')


if __name__ == "__main__":
    main()

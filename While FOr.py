def main():
    while True:
        vastaus = input('Write something (quit ends):')
        if vastaus == 'quit':
            break
        tester(vastaus)
def tester(vastaus, givenstring = 'Too short'):
    if len(vastaus) < 10:
        print(givenstring)
    elif len(vastaus) >= 10:
        print(vastaus)


if __name__ == "__main__":
    main()
list = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]
total = 0

print('Supermarket')
print('===========')
while True:
    select = int(input('Please select product (1-10) 0 to Quit:'))
    if select > 0 and select < 11:
        print(f'Product: {select}, Price: {list[select-1]}')
        total = total + list[select-1]
    elif select == 0:
        print('Total:', total)
        payment = int(input('Payment:'))
        change = payment - total
        print(change)
        break


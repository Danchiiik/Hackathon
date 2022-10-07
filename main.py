from views import *

def main():
    while True:
        print('Hello, there is function:\n 1- get all products,\n 2 - get one product,\n 3 - create product,\n 4 - delete product,\n 5 - update product,\n 0 - to exit ')
        method = input('enter the number: ')
        if method == '1':
            filter = True if input('Do you want to filter? (Yes or anything) ').title() == 'Yes' else False 
            print(get_data(filter))
            print('\n')
        elif method == '2':
            id = int(input('enter the id: '))
            print(get_one_data(id))
            print('\n')
        elif method == '3':
            print(post_data())
            print('\n')
        elif method == '4':
            id = int(input('enter the id: '))
            print(delete_data(id))
            print('\n')
        elif method == '5':
            id = int(input('enter the id: '))
            print(update_data(id))
            print('\n')
        elif method == '0':
            break
        else:
            print('no such method')


main()



if '__name__' == '__main__':
    main()
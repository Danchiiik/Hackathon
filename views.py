from datetime import *
import json

FILE_PATH = 'data.json'



def get_data(filter = None ): # Получение всего списка
    with open(FILE_PATH) as file:
        data = json.load(file)
    if filter:
        filter_type = input('what type of filtering: by price(p), by status(s) or by date(d)?: ').lower() # Выбор фильтрации
    
        if filter_type == 'p': # Фильтрация по цене
            price = float(input('Enter the price: '))
            cost = input(f'Is price need to be lower(l) or higher(h) than {price}? : ').lower()
            if cost == 'h':
                new_data = [i for i in data if i['price'] >= price]
                if new_data:
                    return new_data
                return 'No product found'
            elif cost == 'l':
                new_data = [i for i in data if i['price'] <= price]
                if new_data:
                    return new_data
                return 'No product found'

        if filter_type == 's': # Фильтрация по статусу
            activeness = input('Is status need to be active(a) or not(n)? ').lower()
            if activeness == 'a':
                new_data = [i for i in data if i['status'] == True]
                if new_data:
                    return new_data
                return 'No product found'
            elif activeness == 'n':
                new_data = [i for i in data if i['status'] == False]
                if new_data:
                    return new_data
                return 'No product found'

        if filter_type == 'd':
            date = str(datetime.strptime(input("Enter the date dd/mm/yyyy: "), '%d/%m/%Y').date()) 
            new_data = [i for i in data if i['create_at'] == date]
            if new_data:
                return new_data
            return 'No product found'
    return data

    
def get_one_data(id): # Получение одного элемента
    data = get_data()
    one_data = [i for i in data if i['id'] == id]
    if one_data:
        return one_data
    return 'No product found'


def post_data(): # Добавление элемента
    data = get_data()
    try:
        maxid = max([i['id'] for i in data ])
    except ValueError:
        maxid = 0

    data.append({
        'id': maxid + 1,
        'name': input('enter the name: ').capitalize(),
        'price': float(input('enter the price: ')),
        'create_at' : str(datetime.now().strftime("%Y-%m-%d")),
        'updated_at': str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        'description': input('add some description: ').title(),
        'status' : True if input('True or False: ').capitalize() == 'True'   else False
        
    })
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
        return 'Created'


def update_data(id): # Обновление элемента 
    data = get_data()
    update_d = [i for i in data if i['id'] == id]
    
    if update_d:
        index_ = data.index(update_d[0])
        data[index_]['name'] = input('enter the new name: ').capitalize()
        data[index_]['price'] = float(input('enter the new price: '))
        data[index_]['updated_at'] = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        data[index_]['description'] = input('Add some description: ').title()
        data[index_]['status'] = True if input('True or False: ').title() == 'True' else False
        json.dump(data, open(FILE_PATH, 'w'))
        return 'Updated'
    return 'No product found'



def delete_data(id): # Удаление элемента
    data = get_data()
    delete_d = [i for i in data if i['id'] == id]

    if delete_d:
        data.remove(delete_d[0])
        json.dump(data, open(FILE_PATH, 'w'))
        return 'Deleted'
    return 'No product found'

# %H:%M:%S
# Задача №1:

cook_book = {}
with open('C:\\Users\\Вера\\Desktop\\Python нетология\\HW_files\\recipes.txt', 'rt', encoding='utf-8') as file:
    dishes = ''
    for x in file:
        x = x.strip()
        if x.isdigit():
            continue
        elif x and '|' not in x:
            cook_book[x] = []
            dishes = x
        elif x and '|' in x:
            a, b, c = x.split(" | ")
            cook_book.get(dishes).append(dict(ingredient_name=a, quantity=int(b), measure=c))

# Задача №2

def get_shop_list_by_dishes(dishes_list, person_count):
    shop_list = {}
    for dish in dishes_list:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in shop_list:
                    shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
                else:
                    shop_list[ingredient['ingredient_name']] = ({'measure': ingredient['measure'], 'quantity':
                                                                (ingredient['quantity'] * person_count)})
        else:
            print('Такого блюда нет в книге')
    return shop_list


print(get_shop_list_by_dishes(['Омлет'], 10))
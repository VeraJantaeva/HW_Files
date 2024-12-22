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
print(cook_book)
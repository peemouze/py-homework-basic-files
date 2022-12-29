# with open(recipes, 'r') as f:
#     for line in f:
#         print()
#
# f.read()

# считываем все
# f = open('recipes.txt', 'rt')
# res = f.read()
# print(res)
# print(type(res))
# f.close()

# считываем по одному
# f = open('recipes.txt')
# result = f.readline()
# print(result)
# print(type(result))
# f.close()

# считываем строк в виде списка
# with open('recipes.txt') as f:
#     # result = f.readlines()
#     # print(result[4])
#     # print(type(result))
#     for line in f:
#         print(line)

# #запись по одной строке
# with open('recipes2.txt', 'a') as file:
#     file.write('novaya stroka!\n')

# #запись нескольких строк
# with open('recipes2.txt', 'w') as f:
#     f.writelines(['line1\n','line2\n'])

cook_book = {}

def get_cook_book():
    with open('recipes.txt', encoding='utf-8') as f:
        for line in f:
            item_name = line.strip()
            ingredients_count = int(f.readline())
            ingredients = []
            for i in range(ingredients_count):
                ingredient_name = f.readline().strip()
                ingredient_name, quantity, measure = ingredient_name.split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            f.readline()
            cook_book[item_name] = ingredients
    # print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for item in dishes:
        print(item)
        if item in cook_book:
            for ingredients in cook_book[item]:
                m_q_list = dict()
                if ingredients['ingredient_name'] not in shop_list:
                    m_q_list['measure'] = ingredients['measure']
                    m_q_list['quantity'] = ingredients['quantity'] * person_count
                    shop_list[ingredients['ingredient_name']] = m_q_list
                else:
                    shop_list[ingredients['ingredient_name']]['quantity'] = shop_list[ingredients['ingredient_name']]['quantity'] + ingredients['quantity'] * person_count
        else:
            print(f'Блюда {item} нет в кулинарной книге!')

    return shop_list

def param():
    dishes = input('Введите название блюда: ').split(', ')
    person_count = int(input('Введите количество порций: '))
    get_cook_book()
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print(shop_list)


param()
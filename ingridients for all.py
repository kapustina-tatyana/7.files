def my_cook_book():
    cook_book = {}

    sub_book = []
    tmp_book = {}
    tmp_books = []
    with open('test.txt', encoding='utf -8') as file:
        for line in file.read().split('\n\n'):
            for sub_line in line.split('\n'):
                sub_book.append(sub_line)
                # print(sub_book)
            ingridient_limit = len(sub_book)
            for ingridient_num in range(2,ingridient_limit):
                ingridient_value = sub_book[ingridient_num].split(' | ')

                tmp_book['ingridient_name'] = ingridient_value[0]
                tmp_book['quantity'] = ingridient_value[1]
                tmp_book['measure'] = ingridient_value[2]
                tmp_books.append(tmp_book)
                tmp_book = {}
                ingridient_value = []
            cook_book[sub_book[0]] = tmp_books
            tmp_books = []
            sub_book = []

    return cook_book

cook_book = my_cook_book()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:

        dish_str = dishes[dish]
        for ingridient in dish_str:

            ingrid_shop = ingridient['ingridient_name']
            quantity_shop = int(ingridient['quantity']) * int(person_count)
            shop_list.setdefault(ingrid_shop, {})
            quantity_shop_get = shop_list.get(ingrid_shop).get('quantity', 0) + quantity_shop

            measure_shop = ingridient['measure']
            shop_list[ingrid_shop] = {'measure': measure_shop, 'quantity': quantity_shop_get}
    return shop_list

shop_list_by_dishes = get_shop_list_by_dishes(cook_book, 5)
print(shop_list_by_dishes)

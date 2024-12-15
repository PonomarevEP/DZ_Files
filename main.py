def parse_cookbook(file_path):
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    current_recipe = None
    ingredient_count = 0
    ingredients = []

    for line in lines:
        line = line.strip()
        if line.isdigit():  # Число ингредиентов
            ingredient_count = int(line)
        elif line and not line.isdigit():  # Название рецепта или ингредиента
            if current_recipe is None:  # Начало нового рецепта
                current_recipe = line
                cook_book[current_recipe] = []
            else:  # Новый ингредиент
                parts = line.split('|')
                ingredient_name = parts[0].strip()
                quantity = int(parts[1].strip())
                measure = parts[2].strip()
                ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
                if len(ingredients) == ingredient_count:
                    cook_book[current_recipe] = ingredients
                    current_recipe = None
                    ingredients = []
                    ingredient_count = 0

    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    
    for dish in dishes:
        if dish not in cook_book:
            print(f"Блюдо '{dish}' отсутствует в книге рецептов.")
            continue
        
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            
            # Проверяем, есть ли ингредиент уже в списке покупок
            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += ingredient['quantity'] * person_count
            else:
                shop_list[ingredient_name] = {
                    'measure': ingredient['measure'],
                    'quantity': ingredient['quantity'] * person_count
                }
                
    return shop_list

cook_book = parse_cookbook('files/recipes.txt')
print(cook_book)

dishes = ['Запеченный картофель', 'Омлет']
person_count = 2

shop_list = get_shop_list_by_dishes(dishes, person_count)
print(shop_list)
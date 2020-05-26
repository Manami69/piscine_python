cookbook = {
    'sandwich': {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
                 'meal': 'lunch', 'prep_time': '10'},
    'cake': {'ingredients': ['flour', 'sugar', 'eggs'],
             'meal': 'dessert', 'prep_time': '60'},
    'salad': {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
              'meal': 'lunch', 'prep_time': '15'},
}


def print_recipe(name):
    verify = cookbook.get(name)
    if verify is None:
        print("There is no {} recipe in the cookbook, please add one".format(
            name))
    else:
        print("Recipe for {}:\nIngredient list: {}\nTo be eaten for \
{}.\ntakes {} minutes of cooking.".format(name,
                                          cookbook[name]["ingredients"],
                                          cookbook[name]["meal"],
                                          cookbook[name]["prep_time"]))


def del_recipe(name):
    try:
        del cookbook[name]
        print("{} recipe deleted from cookbook".format(name))
    except KeyError:
        print("recipe {} not found".format(name))


def add_recipe(name, ingredients, meal, prep_time):
    new_entry = {name: {'ingredients': ingredients,
                        'meal': meal, 'prep_time': prep_time}}
    cookbook.update(new_entry)


def print_all_recipes():
    for key in cookbook.keys():
        print_recipe(key)
        print("\n")


def ask_for_recipe(request):
    recipe = str(
        input("Please enter the recipe's name to get its details:\n>>"))
    if request == 'add':
        print_recipe(recipe)
    if request == 'del':
        del_recipe(recipe)


def give_new():
    print("Enter a recipe name:")
    name = str(input(">> "))
    ingredients = []

    while True:
        next_i = input(
            "Add an ingredient to your recipe (put 0 when you're done)\n>> ")
        if (next_i == '0'):
            break
        ingredients.append(next_i)
    print("For what meal you want to make this recipe")
    meal = input(">> ")
    time = input("How much time you need to make this recipe\n>> ")
    add_recipe(name, ingredients, meal, time)


while True:
    print("Please select an option by typing the corresponding number:\
\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n\
4: Print the cookbook\n5: Quit")
    request = input(">> ")
    if request == '5':
        break
    elif request == '4':
        print_all_recipes()
    elif request == '3':
        ask_for_recipe('add')
    elif request == '2':
        ask_for_recipe('del')
    elif request == '1':
        give_new()
    else:
        print("This option does not exist, please type the \
corresponding number.\nTo exit, enter 5")

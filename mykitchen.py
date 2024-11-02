# My Kitchen User Interface
# David Marin
# Last Updated: 11/1/2024
# 
# Description: This program has a list of features. 
# Features include:
# --> Get user input for ingredients & appliances they have in their kitchen. Output all recipies that only include those ingredients & appliances
# --> Add a recipe inputted from the user
# --> Output alternative food options for ingredients that could be swapped


# * NOTE * The user_recipes and the recipes from "All Recipes" (website) will be in separate databases so we can distinguish between the two.
recipes = {    # Theses are the recipes that will be taken from a recipe database
    "Spicy Potato Soup":  ["stove", "blender", "potato", "stock", "cream", "siracha"],
    "Tacos": ["beef", "tortilla", "cheese"],
    "Pizza": ["oven", "flour", "cheese", "tomato"]
}

user_recipes = {    # These are the recipes that the users themselves will add into the database.
}

working_recipes = []
user_ingredients = []


def find_recipe(recipes, user_ingredients, working_recipes):
    ''' Find valid recipes based on user's ingredient availability. '''

    for recipe in recipes:    # For each recipe
        for recipe_ingredient in recipes[recipe]:    # For each ingr in the recipe
            if recipe_ingredient in user_ingredients:    # If the recipe's ingr is in the list of user's ingr's
                if recipe_ingredient == recipes[recipe][-1]:    # If the recipe_ingr is the last one in the recipe AND it is in the user's ingr.s, 
                                                                # then the recipe works, so we append the recipe to the list of working recipeds
                    working_recipes.append(recipe)
                # do something
                continue
            else:    # If the recipe_ingredient isn't in user's ingredients, we go to the next recipe
                break
 

# Getting user ingredients and finding valid recipes for them.
# user_ingredients = [x for x in input("\nWhat ingredients and appliances do you have? \n").split(" ")]
# find_recipe()
# working_recipes = ", ".join(working_recipes)
# print(f"\nRecipes you can use: {working_recipes}\n")

def add_ingredients():
    ''' Add user ingredients to a list. '''

    for item in [x for x in input("\nWhat ingredients and appliances do you have? \n").split(" ")]:
        user_ingredients.append(item)

    return user_ingredients




# Creating User Recipe
# recipe_name = input("Please enter your recipe name: " )
# recipe_ingredients = input("Please enter the ingredients and appliances included in your recipe: ")
# user_recipes[recipe_name] = recipe_ingredients

def add_user_recipe():
    ''' Add a user-made recipe to the list. '''

    recipe_name = input("Please enter your recipe name: " )
    recipe_ingredients = input("Please enter the ingredients and appliances included in your recipe: ")
    user_recipes[recipe_name] = recipe_ingredients

    print("\nHere are the users' recipes: \n")
    for key in user_recipes:
        print(f'"{key}"')
        print(f"To make {key}, you need these ingredients and appliances:")
        for value in user_recipes[key].split():
            print(value)
    print("\n")





# # Printing the user's created recipe
# print("Here are the users' recipes: \n")
# for key in user_recipes:
#     print(f"{key}")
#     print(f"To make {key}, you need these ingredients and appliances:")
#     for value in user_recipes[key].split():
#         print(value, end= ", ")
# print("\n")





def get_menu_option():
    ''' Get user's option. '''
    print("\nMy Kitchen")
    print("     (H): Home")
    print("     (A): Add Ingredients/Appliances")
    print("     (D): Discover")
    print("     (F): Favorites")
    print("     (G): Get Recipe")
    print("     (R): Add User Recipe")
    print("     (Q): Quit\n")

    option = input("Option: ")

    return option


def main():
    option = get_menu_option()
    working_recipes = []
    
    while option != "Q":
        if option == "A":
            add_ingredients()
            print(user_ingredients)

        if option == "G":
            find_recipe(recipes, user_ingredients, working_recipes)
            working_recipes = ", ".join(working_recipes)
            print(f"\nRecipes you can use: {working_recipes}\n")
        
        if option == "R":
            add_user_recipe()

        if option == "Q":
            sys.exit()
            
        option = input("Option: ")






if __name__ == "__main__":
    main()

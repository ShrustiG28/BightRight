def check_allergy_risk(user_allergies, ingredients):
    allergies = [str(allergy).lower() for allergy in user_allergies]
    ingredient_list = [str(ingredient).lower() for ingredient in ingredients]

    for allergy in allergies:
        for ingredient in ingredient_list:
            if allergy in ingredient:
                return True
    return False

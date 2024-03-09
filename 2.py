from random import randint

def get_numbers_ticket(min, max, quantity):
    result =set()
    if min >= 1 and max <= 1000:
        while len(result) < quantity:
            random_number = randint(min, max)
            result.add(random_number)
        return sorted(list(result))
    else:
        return []  
lottery_numbers = get_numbers_ticket(1, 49, 6)
lottery_numbers2 = get_numbers_ticket(1, 1001, 6)
lottery_numbers3 = get_numbers_ticket(-1, 49, 6)
print("Your lottery numbers:", lottery_numbers)
print("Your lottery numbers:", lottery_numbers2)
print("Your lottery numbers:", lottery_numbers3)

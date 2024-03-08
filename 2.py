from random import randint

def get_numbers_ticket(min, max, quantity):
    result =set()
    while len(result) < quantity:
        random_number = randint(min, max)
        result.add(random_number)
    return sorted(list(result))  
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

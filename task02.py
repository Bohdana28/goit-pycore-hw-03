import random

def get_numbers_ticket(min, max, quantity) :
    
    if not (1<= min <=max<=1000):
        return "Your diapason isn't correct"
    if quantity<1 or quantity > (max - min + 1) :
        return "Your quantity isn't correct"
    
    numbers_ticket =random.sample(range(min, max+1), quantity)
    return sorted(numbers_ticket)

print(get_numbers_ticket(1, 49, 8))
print(get_numbers_ticket(18, 16, 2))
print(get_numbers_ticket(1, 6, 10))
        
def  find_duplicates(numbers):
    seen = set()

    for number in numbers:
        if number in seen:
            return True 
        seen.add(number)
    return False

my_numbers = [1 ,  2 ,3 ,4 ,3,6]
result = find_duplicates(my_numbers)
print(result)


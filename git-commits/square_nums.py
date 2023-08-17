
chosen_numbers = [1,3,5,7,9,11]
squared_numbers = []

def square_nums_func():
  for x in chosen_numbers:
    number =  x * x
    squared_numbers.append(number)
  squared_numbers.sort()
  print(squared_numbers)

square_nums_func()

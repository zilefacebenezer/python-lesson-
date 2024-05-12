def print_equilateral_triangle(rows):
    for i in range(1,rows + 1):
        print(' ' * (rows-i) + "*" * (2*i-1))
          #print(" " * (rows - i) + "*" * (2*i-1))

print("equilateral triangle") 
print_equilateral_triangle(5)       
      
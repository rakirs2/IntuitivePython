def print_number_of_stars_triangle_increasing(number):
    for i in range(1, number+1):
        print('*' * i)

# print_number_of_stars_triangle_increasing(5)

def print_number_of_stars_triangle_decreasing(number):
    for i in range(number, 0, -1):
        print('*' * i)

# print_number_of_stars_triangle_decreasing(5)

def print_number_of_stars_and_underscores(number):
    for i in range(number, 0, -1):
        print(return_stars_and_underscores(i))
       

def return_stars_and_underscores(number):
    result_string = ""
    for i in range(number):
        if i % 2 == 0:
            result_string += "*"
        else: 
            result_string += "_"
    return result_string

print_number_of_stars_and_underscores(5)

# print(return_stars_and_underscores(5))
# print(return_stars_and_underscores(4))
# print(return_stars_and_underscores(0))
# for i in range(0, 5, 1):
#     print(i)
# for (int i = 0; i< number; i++){}

# ***** i = n; * = n; _ = 0
# _**** i = n-1; * = (n-1); _ = 0 ()
# __***
# ___**
# ____*


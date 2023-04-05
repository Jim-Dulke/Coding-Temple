#Question 1: Write a function to print "hello_USERNAME! USERNAME is the input of the function."

def hello_name(user_name):
    print(f'Hello {user_name}!')
hello_name()

#Question 2: Write a function (first_odds) that prints the numbers from 1-100 and returns nothing

def first_odds():
    first_odd = 1
    last_num = 100

    for number in range (first_odd, last_num):
        first_odd += 2
        return None
    
first_odds()

#Question 3: Write a function (max_num_in_list) to return the max number of a given list

def max_num_in_list(a_list):
    a_list = []
    return max(a_list) 

#Question 4: Write a function to return if a leap year is a given year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400.

def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 400 == 0:
        return True
    elif a_year % 4 != 0 or a_year % 400 != 0:
        return False


#Question 5: Write a function to see if all numbers in a list are consecutive numbers. Return type should be true/false

def is_consecutive(a_list):
    a_list = []
    count = 0
    for x in a_list:
        if x:
            return True
        else:
            return False

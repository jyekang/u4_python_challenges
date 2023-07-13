# Python Challenges


#  1) The Time Stone: Lets get cosmic here and begin working with Time.

# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
# -  Then take it up a step further, converting Hours into seconds (1 -> 3600)
# -  We're on the right track here, how many seconds are in a day
# - How many Hours are in the month of June? 
# - How many Minutes are in the month of August?
 
 
 # Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year? 
 # In days, in weeks, in cups of coffee?


# def get_seconds(minutes):
#     return minutes * 60

# def get_hours_to_seconds(hours):
#     return hours * 3600

# def get_days_to_seconds(days):
#     return days * 86400

# def hours_in_june():
#     return 30 * 24

# def minutes_in_august():
#     return 30 * 24 * 60


# print(get_seconds(5))
# print(get_hours_to_seconds(1))
# print(get_days_to_seconds(2))
# print(hours_in_june())
# print(minutes_in_august())


#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


# def middle_letter(string):
#     if len(string) % 2 == 0:
#         return " "
#     else: 
#         return string[len(string) // 2]
    
# print(middle_letter("janicek"))


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".

# def hidden_cc(cc_number):
#    cc_number_str = str(cc_number)
#    return "*********" + cc_number_str[-4:]

# print(hidden_cc(1234567894444))



# ### 4) Online status
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

# For example, consider the following dictionary:

# ```
# statuses = {
#     "John": "online",
#     "Paul": "offline",
#     "George": "online",
#     "Ringo": "offline"
# }

# ```

# In this case, the number of people online is 2.
# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
# Your function should return the number of people who are online.

# def online_count(statuses):
#     count = 0
#     for status in statuses.values():
#         if status == "online":
#             count += 1
#     return count
        
        
# print(online_count(statuses = {
#     "John": "online",
#     "Paul": "offline",
#     "George": "online",
#     "Ringo": "offline"
#  }))



#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

# def discount(full_price, discount):
#     percent_discount = discount * 0.01
#     new_price = full_price * (1 - percent_discount)
#     return new_price

# print(discount(100, 20))




#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse



# def calc_hypotenuse(a, b):
    
#    hypotenuse = (a**2 + b**2)**0.5
#    return hypotenuse

# print(calc_hypotenuse(3, 4))
   

  


#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence


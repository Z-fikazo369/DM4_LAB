#1.
def is_palindrome(user_input):
   
    if user_input == "PALINDROME" or user_input=="PALINDROME".lower():
     return True
    elif user_input == "EMORDNILAP" or user_input=="EMORDNILAP".lower():
       checker = user_input.lower()
       return True
    else:
       return False
    

print(is_palindrome("joyce"))

#2.

def get_grade(score):
   if 90 <= score <= 100:
        return "A"
   elif 80 <= score <= 89:
        return "B"
   elif 70 <= score <= 79:
        return "C"
   elif 60 <= score <= 69:
        return "D"
   else:
        return "F"
   
print(get_grade(96))

#3
def multiply_all(*inputs):
    result = 1
    for num in inputs:
        result *= num
    return result

print(multiply_all(2,4,5))

#4
def print_formatted_info(title, **kwargs):
    print(title.upper())
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_formatted_info("report", name="Jhon", score=85, status="Pass")

    

   
   

   
    
    

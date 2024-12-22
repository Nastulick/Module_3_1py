from operator import truediv

calls = 0

def count_calls():
    global calls
    print(calls)
    return count_calls()
    def string_info(input_string):
       if input_string == "Capybara":
           input_string_1 == "ARMAGEDON"
           upper_case = input_string.upper()
           lower_case = input_string_1.lower()
           print(len(input_string), upper_case, lower_case)
           def is_contains(input_string):
               for i in string_list:
                   if i.lower() == input_string.lower:
                       print(True)
                   else:
                       print(False)


print(input_string('Capybara'))
print(input_string_1('ARMAGEDON'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)




## PODATKOVNI TIPI

integer_number = 10
float_number = 10.123
string_variable = "Jaz sem tekst"
string_variable_of_a_number = "42"

list_of_numbers = []
list_of_numbers = [1,2,3,4,5]
lenth_of_list = len(list_of_numbers)
list_of_all_kinds_of_stuff = [1,2,3,4,"dance!"]

for num in list_of_numbers:
    pass

list_of_all_kinds_of_stuff.append("polka")
list_of_all_kinds_of_stuff.extend(list_of_numbers)
list_of_all_kinds_of_stuff.index("dance!")
max(list_of_numbers)
min(list_of_numbers)
list_of_all_kinds_of_stuff.count(4)
list_of_all_kinds_of_stuff.reverse()
list_of_all_kinds_of_stuff.clear()


imenik = {}
imenik = { 
    'Matej': 38641123123,
    'Janja': 38631911324
 }
print(imenik['Matej'])
imenik['Tim'] = 38644123125

for key in imenik.keys():
    print(key)
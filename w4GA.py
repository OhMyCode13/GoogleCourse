def format_address(address_string):
    # Declare variables
    house_number = address_string.split(" ")[0]
    house_street_name = address_string[len(house_number) + 1:]
    # Return the formatted string
    return "house number {} on street named {}".format(house_number, house_street_name)


# print(format_address("123 Main Street")) # Should print: "house number 123 on street named Main Street"
# print(format_address("1001 1st Ave")) # Should print: "house number 1001 on street named 1st Ave"
# print(format_address("55 North Center Drive")) # Should print "house number 55 on street named North Center Drive"

def highlight_word(sentence, word):
    return " ".join(cap_word.upper() if cap_word.strip("!,.") == word else cap_word for cap_word in sentence.split(" "))


# return [x.upper() for x in sentence.split(" ") if x==word]

# print(highlight_word("Have a nice day", "nice"))
# print(highlight_word("Shhh, don't be so loud!", "loud"))
# print(highlight_word("Automating with Python is fun", "fun"))

def combine_lists(list1, list2):
    return list2 + list1[::-1]


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

#print(combine_lists(Jamies_list, Drews_list))

def squares(start, end):
	return [ x**2 for x in range(start, end+1) ]

#print(squares(2, 3)) # Should be [4, 9]
#print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
#print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed
  # only once, and the value from guests1 taking precedence
    temp=guests2.copy()
    temp.update(guests1)
    return temp


Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

#print(combine_guests(Rorys_guests, Taylors_guests))

def count_letters(text):
  result = {}
  # Go through each letter in the text
  for letter in text:
    # Check if the letter needs to be counted or not
    if letter.isalpha():
        ltr_key = letter.lower()
        if ltr_key in result.keys():
            result[ltr_key] = result.get(ltr_key,0)+1
        else:
            result.update({letter.lower():1})
  return result

#print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}
#print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}
#print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

x = 5
y = 10
x, y = y, x
print("After Swapping values of x and y are", x, y)
import re

'''top-level web address, meaning that it contains alphanumeric characters 
(which includes letters, numbers, and underscores), as well as periods, dashes, 
and a plus sign, followed by a period and a character-only top-level domain 
such as ".com", ".info", ".edu", etc. Fill in the regular expression to do that, 
using escape characters, wildcards, repetition qualifiers, beginning and end-of-line characters, 
and character classes.'''
def check_web_address(text):
    pattern = "(^[a-zA-Z0-9\+\-\_\.]+$)"
    result = re.search(pattern, text)
    return result != None

'''
print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True
'''
def check_time(text):
    pattern = "(^[1-9]?[0-9])\:([0-5][0-9])\s?(a|A|p|P)(m|M)"
    result = re.search(pattern, text)
    return result != None
'''
print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False
'''
'''
checks the text for the presence of 2 or more characters or digits surrounded by parentheses, 
with at least the first character in uppercase (if it's a letter), returning True if the condition is met, 
or False otherwise. For example, "Instant messaging (IM) is a set of communication technologies used for 
text-based communication" should return True since (IM) satisfies the match conditions."  
'''
def contains_acronym(text):
    pattern = "\([a-zA-z0-9]+\)"
    result = re.search(pattern, text)
    return result != None

# print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
# print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
# print(contains_acronym("Please do NOT enter without permission!")) # False
# print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
# print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True
'''
Fill in the code to check if the text passed includes a possible U.S. zip code, formatted as follows: exactly 5 digits, 
and sometimes, but not always, followed by a dash with 4 more digits. The zip code needs to be preceded by at least one space, 
and cannot be at the start of the text.
'''
def check_zip_code(text):
    result = re.search(r"\s\d{5}\-?(\d{4})?", text)
    return result != None
'''
print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False
'''
def long_words(text):
    pattern = "\w{7,}"
    result = re.findall(pattern, text)
    return result
'''
print(long_words("I like to drink coffee in the morning."))  # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon."))  # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night."))  # []
'''
#print(re.split(r"the|a", "One sentence. Another one? And the last one!"))

def transform_record(record):
  new_record = re.sub('(\d*-\d*(-\d*)?)','+1-'+record.split(',')[1], record)
  return new_record
'''
print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
# Sabrina Green,+1-802-867-5309,System Administrator
print(transform_record("Eli Jones,684-3481127,IT specialist"))
# Eli Jones,+1-684-3481127,IT specialist
print(transform_record("Melody Daniels,846-687-7436,Programmer"))
# Melody Daniels,+1-846-687-7436,Programmer
print(transform_record("Charlie Rivera,698-746-3357,Web Developer"))
# Charlie Rivera,+1-698-746-3357,Web Developer
'''
def transform_comments(line_of_code):
  result = re.sub('#+','//',line_of_code)
  return result
'''
print(transform_comments("### Start of program"))
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable"))
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable"))
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)"))
# Should be "  return(number)"
'''
'''
The convert_phone_number function checks for a U.S. phone number format: 
XXX-XXX-XXXX (3 digits followed by a dash, 3 more digits followed by a dash, and 4 digits), 
and converts it to a more formal format that looks like this: (XXX) XXX-XXXX. 
Fill in the regular expression to complete this function.
'''
def convert_phone_number(phone):
  result = re.sub('(\d{3})-(\d{3})-(\d{4}[\.]?)$', r"(\1)-\2-\3", phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300"))
# Phone number of Buckingham Palace is +44 303 123 7300
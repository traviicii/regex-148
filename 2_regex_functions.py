import re   #re = regex
from helper import d

# Regex methods/functions

#-- re.findall(pattern, text) : retrieves all non-overlapping matches of the pattern and returns a list of all the matches

# Find how many times I use the word 'and'
text = "Hi my name is Travis, and I like to go and do things and stuff."

ands = re.findall(r'and', text) # always start a regex pattern with a raw string : r"<string>"
print(ands)
print(len(ands))

# Find all hashtags in my post
post = "I LOVE # learning #Python_is_lyfe and #Regex, this is so fun! #Coder"

tags = re.findall(r'#\w+', post)
print(tags)

# Find all words that start with b and end with the letter e
sentence = "Abe asked to build a bridge be but he was told 'beware of the beehives"

bes = re.findall(r"\bb\w*e\b", sentence)
print(bes)

# Finding all email addresses
text = 'you can contact me at t.p@gmail.co or travis-p2@codingtemple.com, traviscpeck@email.com'

# username can include letters a-z, digits, _, -, .
# domain can include letters a-z, digits, _, -
# domain extension needs to be only 2 or 3 characters, a-z

# When making regex patterns, break it into pieces
# emails = re.findall(r"[\w.-]+@[\w.-]+", text)
emails = re.findall(r"[\w.-]+@[\w-]+\.[a-z]{2,3}", text)
print(emails)

d()

#-- re.search(pattern, text) : searches a string for a pattern match, and returns the first occurance as a match object, else returns None
# perfect for email validation

#email = input("Enter an email: ")
email = 'tp@email.com'
found = re.search(r"[\w.-]+@[\w-]+\.[a-z]{2,3}", email)
#print(found)
#print(found.group()) # unpacks the match object that was found

if found:
    print(f"{found.group()} is a valid email!")
else:
    print("That is an invalid email")

# Validating phone numbers

# We wanna accept a variety of phone numbers
# 000-000-0000
# 000 000 000
# 0000000000
# (000) 000 0000

number = "My phone number is: (770)880 1180"

phone = re.search(r"\(?\d{3}(\s|-|\))?\d{3}(\s|-)?\d{4}", number)
print(phone.group())

d()

#-- re.match(pattern, text) : will return a match object if there is a pattern match at the very beginning of the text

text = "Hello, world"

obj = re.match(r"Hello", text)
print(obj.group())

# check if a website is secure
# http or https

url = "https://something.com"
secure = re.match(r"https", url)
print(secure.group())

if secure:
    print("this site is a secure website!")
else:
    print("This site is not very secure")

d()

#-- re.split(pattern, text) : splits the text on the occurances of the pattern, returns a list

# split on the garbage characters
text = "Python,Regex;Splitting-Example. Fun, right?"
words = re.split(r"[,;.?-]", text)
print(words[:-1])

d()

#-- re.sub(pattern, replacer, text) : replaces occurances of the pattern in a string with the replacer

number = "(770) 880-1180"

# we want to replace anything that is not a number
formatted_number = re.sub(r"\D", '', number)
print(formatted_number)

# anonymous chat

chat = '''
@Yvebee123 : "I think I love regex"
@Travis : "Aren't you married?"
@Yvebee123 : "It's just not the same"
@Travis : "I hope they don't see this!"
'''

anon_chat = re.sub(r"@\w+", "@user-anon", chat)
print(anon_chat)
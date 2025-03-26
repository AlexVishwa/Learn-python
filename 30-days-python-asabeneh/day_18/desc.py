# syntac
# *re.match(substring, string, re.I)
# substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore

# re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
# re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
# re.findall: Returns a list containing all matches
# re.split: Takes a string, splits it at the match points, returns a list
# re.sub: Replaces one or many matches within a string

import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns an object with span and match
# match = re.search('first', txt, re.I)
# #match = re.search('first|First', txt)
# print(match)  # <re.Match object; span=(100, 105), match='first'>
# # We can get the starting and ending position of the match as tuple using span
# span = match.span()
# print(span)     # (100, 105)
# # Lets find the start and stop position from the span
# start, end = span
# print(start, end)  # 100 105
# substring = txt[start:end]
# print(substring)       # first
#? re.I tells that compiler shall search in both upper and lower case
# # It return a list
# matches = re.findall('[Ll]anguage', txt, re.I)
# matches = re.findall('Language|language', txt, re.I)
# print(matches)  # ['language', 'Language']

# match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
# print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
# OR
# #match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
# #print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.

txt2 = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
# print(re.split(' ', txt2)) # splitting using \n - end of line symbol
#['I', 'am', 'teacher', 'and', '', 'I', 'love', 'teaching.\nThere', 'is', 'nothing', 'as', 'rewarding', 'as', 'educating', 'and', 'empowering', 'people.\nI', 'found', 'teaching', 'more', 'interesting', 'than', 'any', 'other', 'jobs.\nDoes', 'this', 'motivate', 
# 'you', 'to', 'be', 'a', 'teacher?']
#yes

regex_pattern = r'an+'
txt3 = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
# print(matches)  # ['apple']

# To make case insensitive adding flag '
matches = re.findall(regex_pattern, txt, re.I)
# print(matches)  # ['Apple', 'apple']
# or we can use a set of characters method
regex_pattern = r'[Aa]pple'  # this mean the first letter could be Apple or apple
matches = re.findall(regex_pattern, txt)
# print(matches)  # ['Apple', 'apple']

regex_pattern = r'[Aa]pple' # this square bracket mean either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
# print(matches)  # ['Apple', 'apple']

regex_pattern = r'[Aa]pple|[Bb]anana' # this square bracket means either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
# print(matches)  # ['Apple', 'banana', 'apple', 'banana']

regex_pattern = r'\d'  # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
# print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1'], this is not what we want

regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] - now, this is better!

regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . any character, + any character one or more times 
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  #*   ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1, 4}'   # 1 to 4
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ means starts with
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']
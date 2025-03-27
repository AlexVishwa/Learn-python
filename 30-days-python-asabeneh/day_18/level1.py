import re
paragraph = '''I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'''
def most_frequent_words(paragraph):
    r = re.split(' ', paragraph)
    unique_words = set(r)  # Use a set to avoid duplicates
    for word in unique_words:
        srch = re.findall(r'\b' + re.escape(word) + r'\b', paragraph)#Used to escape special character in words
    print(f'({len(srch)},{word})')
    # print(f'({len(srch)},{r[i]})')
most_frequent_words(paragraph)
txt='The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'
regex_pattern=r'-?\b[0-9]+\b'
matches=re.findall(regex_pattern, txt)
finalmatch=(int(p) for p in matches)
# print(int(matches[len(matches)-1])-int(matches[0]))
# print(type(matches))
# regex_pattern=r'[+|-]*[0-9]{2}'
# matches+=re.findall(regex_pattern,txt)
finalmatch=sorted(finalmatch)
print(finalmatch[len(finalmatch)-1]-finalmatch[0])
#20
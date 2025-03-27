
import os,re
import json
from collections import Counter

# def email_extraction():
#     current_dir = os.path.dirname(__file__)
#     file_path = os.path.join(current_dir, '../data/email_exchange_big.txt')
#     f=open(file_path)
#     lines=f.readlines()
#     regex_pattern=r'[a-zA-Z0-9]\@[a-zA-Z0-9]\.[a-zA-Z]'
#     listofemails=(email for line in lines lambda email: re.findall(regex_pattern,line))
#     print(listofemails)

def find_most_common_words(filename,number):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir,filename)
    f=open(file_path)
    lines=f.readlines()

    # r = (words for line in lines re.split(' ', lines))
    for line in lines:
        words=re.split(' ', line)
    unique_words = set(words)
    print(unique_words)
    # for word in unique_words:
    #     regex_pattern=r'\b'+re.escape(word)+r'\b'
    #     for line in lines:
    #         list2= re.findall(regex_pattern,line)
    #         print((list2,word))
    duplicates_count=Counter(unique_words)
    print(duplicates_count)
find_most_common_words('file1.txt',10)
# TypeError: expected string or bytes-like object, got 'list'
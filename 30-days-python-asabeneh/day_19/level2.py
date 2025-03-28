
import os,re,csv
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

def find_most_common_words(filename):
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
# find_most_common_words('file1.txt')
# TypeError: expected string or bytes-like object, got 'list'
# find_most_common_words('../assets/obama_speech.txt')
# print('Obama Couple')
# find_most_common_words('../assets/michelle_obama_speech.txt')
#Not getting all the words also facing .\n issue
def numberOfLines():
    current_dir = os.path.dirname(__file__)
    # //file_path = os.path.join(current_dir, '../data')
    csv_file_path = os.path.join(current_dir, '../data/hacker_news.csv')
    with open(csv_file_path) as f:
        csv_reader = csv.reader(f, delimiter=',') # we use the reader method to read csv
        line_count = 0
        # word_count=0
        # regex_pattern=r'python|Python'
        # regex_pattern=r'javascript|Javascript|JavaScript'
        regex_pattern=r'Javascript'
        for row in csv_reader:
            matches=[]
            for word in row:
                matches+=(re.findall(regex_pattern,word))
            # *print(matches) debugger
            if(matches!=[]):
                print(row)
                line_count+=1
            else:
                pass
                # line_count += 1
            # print(line_count)
        return line_count
        
print(numberOfLines())
# for Java 225
# for Javascript 3
# for Java and not Javascript only 2
#Answer 222
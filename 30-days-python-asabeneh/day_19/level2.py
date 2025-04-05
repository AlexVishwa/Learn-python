try:
    import requests
except ImportError:
    print("The 'requests' module is not installed. Please install it using 'pip install requests'.")
    raise
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
find_most_common_words('file1.txt')
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

def find_most_common_words_url(url):
    # import requests
    import os,re,csv
    import json
    from collections import Counter
    # current_dir = os.path.dirname(__file__)
    # file_path = os.path.join(current_dir,filename)
    # f=open(file_path)
    # lines=f.readlines()
    lines= requests.get(url)
    print(type(lines))
    # r = (words for line in lines re.split(' ', lines))
    lines2=lines.text
    # print(type(lines2))
    words=[]

    lines=re.split('\r\n', lines2)
    for line in lines:
        words+=re.split(' ', line)
    for word in words:
        word.replace(',','')
        word.replace('.','')
        word.replace('!','')
        word.replace('?','')
        word.replace(':','')
        word.replace(';','')
        word.replace('\"','')
        # word.replace('\'','') this is special case where ' can be used for e,i etc.
        word.replace('(','')
        word.replace(')','')
        word.replace('\'\'','')
        word.replace('`','')
        word.replace('`','')
        word.replace('\'','')
        word.replace('\"','')
        word.replace('\'\'','')
        word.replace('\"','')
        word.replace('\'\'','')
    # TypeError: cannot use a string pattern on a bytes-like object
    unique_words = set(words)
    print(unique_words)
    # for word in unique_words:
    #     regex_pattern=r'\b'+re.escape(word)+r'\b'
    #     for line in lines:
    #         list2= re.findall(regex_pattern,line)
    #         print((list2,word))
    duplicates_count=Counter(unique_words)
    print(duplicates_count)

# TypeError: write() argument must be str, not list, not set, not dict, not Counter, nor tuple
# also need to import requests,re externally on terminal
#  Also on terminal we have to recursively exit terminal after making changes in imported files
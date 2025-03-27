import os
import json
from collections import Counter
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, '../assets/donald_speech.txt')
with open(file_path,'w+') as f:
    lines=f.readlines()
    print(lines)
file_path = os.path.join(current_dir, '../assets/melania_trump_speech.txt')
with open(file_path,'r') as f:
    line=f.readline()
    print(line)

file_path = os.path.join(current_dir, '../assets/obama_speech.txt')
with open(file_path, 'r') as f:
    lines = f.readlines()
    print(f'Number of lines in speech by Obama:{len(lines)}')
    w=0
    for i in range(len(lines)-1):
        w+=len(lines[i].split('\n'))
    print(f'No. of words are:{w}')
file_path = os.path.join(current_dir, '../assets/michelle_obama_speech.txt')
with open(file_path,'r') as f:
    lines=f.readlines()
    print(f'Number of lines in Michelle Obama speech:{len(lines)}')
    w=0
    for i in range(len(lines)-1):
        w+=len(lines[i].split('\n'))
    print(f'No. of words are:{w}')
# []
# Number of lines in speech by 
# Obama:66
# Number of lines in Michelle Obama speech:83

def most_spoken_languages(File,number):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, File)
    f=open(file_path)
    countries_data=json.loads((f.read()))
    list1=[unpacking_country_info(**country) for country in countries_data]
    # print(list1[0])
    country=0
    list2=[language for i in list1 for language in i]
    # for i in list1:
    #     for language in list1:
    #         list2=language
    # print(list2)
    set1 = set(list2)
    duplicates_count = Counter(list2)
    print(type(duplicates_count))
    # print(len(list2))
    # print(len(set1))
    # #put t in a list
def unpacking_country_info(name, capital, languages,population, flag, currency):
    return languages
# most_spoken_languages("../data/countries_data.json",10)

def most_populated_countries(File, number):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, File)
    f=open(file_path)
    countries_data=json.loads((f.read()))
    list1 = [unpacking_country_info2(**country) for country in countries_data]
    sorted_countries = sorted(list1, key=lambda x: x["population"], reverse=True)
    print(sorted_countries[:number])
def unpacking_country_info2(name, capital, languages,population, flag, currency):
    return {"name": name, "population": population}
most_populated_countries("../data/countries_data.json",10)

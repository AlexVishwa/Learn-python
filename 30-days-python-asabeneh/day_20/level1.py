import os
import json
from pathlib import Path
import requests
from day_19 import level2
# res=requests.get()
print(level2.find_most_common_words_url("https://www.gutenberg.org/cache/epub/1112/pg1112.txt"))

# TypeError: write() argument must be str, not list, not set, not dict, not Counter, nor tuple
# also need to import requests,re externally on terminal
#  Also on terminal we have to recursively exit terminal after making changes in imported files
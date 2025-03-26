import re
from level1 import most_frequent_words
sentence = '''%I am@ a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @empo@wering peo@ple. ;I found tea@ching mo@re interesting tha@n any other %jo@bs. %Do@es this mo@tivate yo@u to be a tea@cher!?'''

refined_sentence=re.sub('%|@|$|&|!|#|;','',sentence)
# sentence.replace('%','')
most_frequent_words(refined_sentence)

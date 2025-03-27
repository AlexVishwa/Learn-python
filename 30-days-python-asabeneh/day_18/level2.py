#not working properly
import re
def is_valid_identifier(txt):
    regex_pattern=r'[0-9]'
    match1=re.findall(regex_pattern,txt)
    # print(match1)
    regex_pattern=r'[\!|\@|\#|\$|\%|\^|\&|\*|\(|\)]'
    match2=re.findall(regex_pattern,txt)
    # print(matches)
    regex_pattern=r'[^A-Z]'
    match3=re.findall(regex_pattern,txt)
    # print(match3)
    if match1!=[]:
        return False
    elif match2==[]:
        return True
    elif match3!=[]:
        print('Reached here')
        return True
    else:
        return False
    
    
print(is_valid_identifier('bc'))
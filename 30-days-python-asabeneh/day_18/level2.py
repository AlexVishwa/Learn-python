import re
def is_valid_identifier(txt):
    regex_pattern=r'[^0-9][a-zA-Z0-9][%|_]*'
    matches=re.findall(regex_pattern,txt)
    print(matches)
    if matches is None:
        return False
    else:
        return True
    
is_valid_identifier('123abc')
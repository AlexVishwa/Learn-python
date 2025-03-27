
# txt='The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'
# regex_pattern=r'-?\b[0-9]+\b'
# matches=re.findall(regex_pattern, txt)
# finalmatch=(int(p) for p in matches)
# # print(int(matches[len(matches)-1])-int(matches[0]))
# # print(type(matches))
# # regex_pattern=r'[+|-]*[0-9]{2}'
# # matches+=re.findall(regex_pattern,txt)
# finalmatch=sorted(finalmatch)
# print(finalmatch[len(finalmatch)-1]-finalmatch[0])
# #20
import re

todo = [
    "It is 800-555-1212.",
    "It is 800 555 1212.",
    "It is 800.555.1212.",
    "It is (800) 555-1212.",
    "It is 1-800-555-1212.",
    "It is 800-555-1212-1234.",
    "It is 800-555-1212x1234.",
    "It is 800-555-1212 ext. 1234.",
    "It is work 1-(800) 555.1212.",
]
# todo = "abc".join(todo)
# phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
phonePattern = re.compile(r'''
                # don't match beginning of string, number can start anywhere
    (\d{3})     # area code is 3 digits (e.g. '800')
    \D*         # optional separator is any number of non-digits
    (\d{3})     # trunk is 3 digits (e.g. '555')
    \D*         # optional separator
    (\d{4})     # rest of number is 4 digits (e.g. '1212')
    \D*         # optional separator
    (\d*)       # extension is optional and can be any number of digits
    $           # end of string
    ''', re.VERBOSE)

# res = phonePattern.search(todo)
# print(res.groups())
# print(res.group())

# for i in todo:
#     res = phonePattern.search(i)
#     print(res.groups(), res.group())
    
for i in todo:
    res = re.findall(phonePattern, i)
    print(res)
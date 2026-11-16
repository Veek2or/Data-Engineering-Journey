'''
1.4 Defensive parsing. Write parse_mark(value) that handles "72", " 65 ", "N/A", "", "105", "-3" and None. 
You decide what each should return or raise, and write that decision in the docstring. 
'''

def parse_mark(value):
    if value == None:
        return None

    nospace = value.strip()
    
    if nospace == "" or nospace.lower() == "n/a":
        return None

    converted = int(nospace)

    if converted > 100 or converted < 0:
        raise ValueError("Mark is out of range")

    return converted

test = ["72", " 65 ", "N/A", "", "105", "-3", None]

for t in test:
    try:
        print(repr(t), "->", parse_mark(t))
    except ValueError as e:
        print(repr(t), "-> error:", e)
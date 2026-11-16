'''
1.4 Defensive parsing. Write parse_mark(value) that handles "72", " 65 ", "N/A", "", "105", "-3" and None. 
You decide what each should return or raise, and write that decision in the docstring. 
'''

def parse_mark(value):
    if value == None:
        return None

    nospace = value.strip() # remove space from the values
    
    if nospace == "" or nospace.lower() == "n/a": # check missing values
        return None

    converted = int(nospace) # convert values into integers

    if converted > 100 or converted < 0: # check if mark in in range
        raise ValueError("Mark is out of range")

    return converted # return the valid number

test = ["72", " 65 ", "N/A", "", "105", "-3", None] # list of test values

for t in test:
    try:
        print(repr(t), "->", parse_mark(t))
    except ValueError as e:
        print(repr(t), "-> error:", e)


'''
None -> None
"72" -> 72 (valid number)
" 65 " -> 65 (valid number with spaces removed)
"N/A" -> None (none should be returned instead of 0, as 0 can indicate that the student scored 0)
"" -> None
"105" -> error should be raised as it is out of range
"-3" -> same as above. Out of range
None -> None
'''
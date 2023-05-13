import sys
script = sys.stdin.readlines()

for line in script:
    cmd = line.strip()  # a single command line
    
    operation = cmd.split(';')[0]
    types = cmd.split(';')[1]
    letters = cmd.split(';')[2]
    answer = ''
    if operation == 'S':   # if the first word is "S",which means 'split'
        letters = letters.replace("()","")
        if types == "M" or types == "V":    # if the types is "M",which indicates 'method'
            for l in letters:
                if l.isupper():
                    answer += (" "+ l.lower())
                else:
                    answer += l
                    
        elif types == 'C':     # if the types is "C",which indicates 'Class'
            letters = (letters[0].lower() + letters[1:])
            for l in letters:
                if l.isupper():
                    answer += (" "+ l.lower())
                else:
                    answer += l
        
    elif operation == 'C': # if the first word is "C",which means 'combine'
        letters_list = letters.split()
        if types == 'M':  # if the types is "M",which indicates 'method' 
            answer += letters_list[0]
            for word in letters_list[1:]:
                answer += (word[0].upper() + word[1:])
            answer += "()"
        
        elif types == 'V':    # if the types is "V",which indicates 'variable'
            answer += letters_list[0]
            for word in letters_list[1:]:
                answer += (word[0].upper() + word[1:])
                
        elif types == 'C':     # if the types is "C",which indicates 'Class'
            answer += (letters_list[0][0].upper() + letters_list[0][1:])
            for word in letters_list[1:]:
                answer += (word[0].upper() + word[1:])
    
    print(answer)

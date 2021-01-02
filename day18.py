# day 18 p1: Evaluate the expression on each line, what is the sum of the resulting values?
'''
Find every expression within (), evaluate python's eval() or my evaluate() function - replace expression
incl brackets in loop until no more brackets. Evaluate is recursive. Data prep: remove all spaces
'''

def repl_strbysum(s, strng, part):
    return s.replace(strng, part, 1)

def evaluate(s):
    s = s.replace('(','').replace(')','') # don't need brackets now    
    pos = oper = -1

    for i, _ in enumerate(s): # store bracket pos, find numbers
        if i == len(s):
            return evaluate(s)
        if s.count('*') + s.count('+') <= 1:
            return eval(s)
        if pos == -1:
            pos = i # pos of 1st number
            while s[i] not in '*+':
                oper=i
                i+=1
        elif oper > -1:
            while str(s[i]).isnumeric():
                if (i := i + 1) == len(s):
                    break
            
            s = repl_strbysum(s, str(s[pos:i]), str(evaluate(s[pos:i])))

def parse(s):
    s=s.replace(' ', '')
    while True:
        sum = l_br = r_br = 0
        if s.count('(') + s.count(')') == 0: # skip processing
            return evaluate(s)
            
        for i, j in enumerate(s):
            if s[i] == '(': # store brackets position
                l_br = i # check following brackets
            elif s[i] == ')':
                r_br = i # evaluate content between brackets
                part = s[l_br:r_br+1]
                sum = evaluate(part)
                s = repl_strbysum(s, str(part), str(sum))
                break
    return 0

def init():
    lines = open('day18.txt').read()

    s = sum(parse(line) for line in lines.splitlines())
    t = eval("("+lines.replace('*',')*(').replace('\n',')+(')+"0)")
    print('Part 1: {} - Part 2: {}'.format(s, t))

def main():
    init()

main()

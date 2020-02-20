op_stack = []
val_stack = []

def get_prec(token):
# returns 2 for * and /, 1 for + and -
    if token in "*/":
        return 2
    elif token in "()":
        return 0
    else:
        return 1

def get_token(s):
# reads a token at a time from the input string
# returns: type of token (val, op, empty, error), 
#          token, substring of input string after stripping the token
    s = s.strip()  # get rid of trailing spaces
    if not s:
        return "empty", None, "", 0
    s = s.strip()  # get rid of trailing spaces
    token = s[0]
    if token in "+-()":
        return "op", token, s[1:]
    elif token in "*/":
        return "op", token, s[1:]
    elif token in "0123456789.":
        i=1
        while i<len(s) and s[i] in "0123456789.":
            token = token + s[i]
            i=i+1
        try:
            number = float(token)
        except:
            return "error", token + " not a number", s
        return "val", number, s[i:]
    else:
        return "error", token + " invalid string near ", s
def operation():
    error = False
    oper = op_stack[-1]
    op_stack.pop()
    if len(val_stack) < 2:
        if oper == "-":   # sign, not operation...
            val_stack[-1] = -1*val_stack[-1]
            return error #continue
        else:
            print("Too few arguments for "+oper)
            error = True
            return error #break
    else:
        val2 = val_stack[-2]
    val1 = val_stack[-1]
    val_stack.pop()
    val_stack.pop()
    if oper == "+":
        val_stack.append(val1+val2)
    elif oper == "-":
        val_stack.append(val2-val1)
    elif oper == "*":
        val_stack.append(val1*val2)
    else:  # oper must be "/"
        if val1 == 0:
            print("Division by 0 %s / %s "%(val2,val1))
            error = True
            return error #break
        else:
            val_stack.append(val2/val1)
    return error
def calc(inp):
    error = False

    while inp != "":
        type, token, inp = get_token(inp)
        if type == "error":
            error = True
            print(type, token, inp)
            break
        elif type == "empty":
            break
        elif type == "val":
            val_stack.append(token)
#            print("val_stack", val_stack)
        elif type == "op":
            if token == "(":
                op_stack.append(token)
#                print("op_stack", op_stack)
            elif token == ")":
                while op_stack[-1] != "(":
                    error = operation()
                    if error:
                        break
#                    oper = op_stack[-1]
#                    op_stack.pop()
#                    if len(val_stack) < 2:
#                        if oper == "-":   # sign, not operation...
#                            val_stack[-1] = -1*val_stack[-1]
#                            continue
#                        else:
#                            print("Too few arguments for "+oper)
#                            error = True
#                            break
#                    else:
#                        val2 = val_stack[-2]
#                    val1 = val_stack[-1]
#                    val_stack.pop()
#                    val_stack.pop()
#                    if oper == "+":
#                        val_stack.append(val1+val2)
#                    elif oper == "-":
#                        val_stack.append(val2-val1)
#                    elif oper == "*":
#                        val_stack.append(val1*val2)
#                    else:  # oper must be "/"
#                        if val1 == 0:
#                            print("Division by 0 %s / %s "+(val2,val1))
#                            error = True
#                            break
#                        else:
#                            val_stack.append(val2/val1)
                op_stack.pop()  
#                print(val_stack)
#                print(op_stack)

            else:  # normal operators
                while op_stack and get_prec(op_stack[-1]) >= get_prec(token):
                    error = operation()
                    if error:
                        break
#                    oper = op_stack[-1]
#                    op_stack.pop()
#                    if len(val_stack) < 2:
#                        if oper == "-":   # sign, not operation...
#                            val_stack[-1] = -1*val_stack[-1]
#                            continue
#                        else:
#                            print("Too few arguments for "+oper)
#                            error = True
#                            break
#                    else:
#                        val2 = val_stack[-2]
#                    val1 = val_stack[-1]
#                    val_stack.pop()
#                    val_stack.pop()
#                    if oper == "+":
#                        val_stack.append(val1+val2)
#                    elif oper == "-":
#                        val_stack.append(val2-val1)
#                    elif oper == "*":
#                        val_stack.append(val1*val2)
#                    else:  # oper must be "/"
#                        if val1 == 0:
#                            print("Division by 0 %s / %s "+(val2,val1))
#                            error = True
#                            break
#                        else:
#                            val_stack.append(val2/val1)
                op_stack.append(token)
    while op_stack: # and get_prec(op_stack[-1]) >= get_prec(token):
        error = operation()
        if error:
            break
#        oper = op_stack[-1]
#        op_stack.pop()
#        if len(val_stack) < 2:
#            if oper == "-":   # sign, not operation...
#                val_stack[-1] = -1*val_stack[-1]
#                continue
#            else:
#                print("Too few arguments for "+oper)
#                error = True
#                break
#        else:
#            val2 = val_stack[-2]
#        val1 = val_stack[-1]
#        val_stack.pop()
#        val_stack.pop()
#        if oper == "+":
#            val_stack.append(val1+val2)
#        elif oper == "-":
#            val_stack.append(val2-val1)
#        elif oper == "*":
#            val_stack.append(val1*val2)
#        else:  # oper must be "/"
#            if val1 == 0:
#                print("Division by 0 %s / %s "% (val2,val1))
#                error = True
#                break
#            else:
#                val_stack.append(val2/val1)
##        if not error:
##            print(val_stack)
##            print(op_stack)

    if not error:
        return(val_stack[0])
    else:
        return("error")
#        print(val_stack)
#        print(op_stack)
#x = calc("12 3  aa")
#if x:
#    print(x)
y="12+3-(2.5-1)"
x = calc(y)
if x:
    print(y+"="+str(x))
val_stack=[]
y="12*3-(2.5-1)"
x = calc(y)
if x:
    print(y+"="+str(x))

val_stack=[]
y="12/3-(2.5-1)+2"
x = calc(y)
if x:
    print(y+"="+str(x))

val_stack=[]
y="12/(2.5-2.5)"
x = calc(y)
if x:
    print(y+"="+str(x))

val_stack=[]
y="-1+2"
x = calc(y)
if x:
    print(y+"="+str(x))

val_stack=[]
y="-(1+2)"
x = calc(y)
if x:
    print(y+"="+str(x))

val_stack=[]
y="1.4+(2+(3+7)/2)/20"
x = calc(y)
if x:
    print(y+"="+str(x))

#### tempo: 25+70+30+60 minuti = 3 ore e 15!
s ='h15o13N12U1W11K20Y6P18j6a7E1L13S20n2J3W11I16y12h19e8n15O5q5O11J5q15y5L2x12O11s4K20v20T8o16F3q17V15d18'

string = ''
num = ''
new_string = ''
i = 0
while i < len(s):
    if s[i].isalpha():
        string += s[i]
        num +=  ':'
        i += 1
    elif s[i].isdigit():
        num += s[i]
        i += 1
num = num.split(':')
del num[0]
for i in range(len(num)):
    num[i] = int(num[i])
i = 0
while i < len(string):
    new_string += string[i] * num[i]
    i += 1
    

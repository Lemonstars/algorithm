import sys

# line = sys.stdin.readline().strip()
line = '2[B3(A)C]'

ch_stack = ''
big_stack = list()
med_stack = list()
sma_stack = list()

number = -1
big_current = ''
med_current = ''
current = ''

i = 0
while i < len(line):
    ch = line[i]
    ord_ch = ord(ch)
    if ord('0') <= ord_ch <= ord('9'):
        number = int(ch)
    elif ch == '(':
        sma_stack.append(number)
    elif ch == '[':
        med_stack.append(number)
    elif ch == '{':
        big_stack.append(number)
    elif ch == ')':
        current = current * sma_stack[-1]
        del sma_stack[-1]
        if not(sma_stack) and not(med_stack) and not(big_stack):
            ch_stack += current
            current = ''
    elif ch == ']':
        current = current * med_stack[-1]
        del med_stack[-1]
        if not(med_stack) and not(big_stack):
            ch_stack += current
            current = ''
    elif ch == '}':
        current = current * big_stack[-1]
        del big_stack[-1]
        if not(big_stack):
            ch_stack += current
            current = ''
    else:
        if not(sma_stack) and not(med_stack) and not(big_stack):
            ch_stack += ch
        else:
            if sma_stack:
                current += ch
            elif med_stack:
                med_stack += ch
            else:
                big_stack += ch

    i += 1

for i in range(len(ch_stack)-1, -1, -1):
    if i == 0:
        print(ch_stack[i])
    else:
        print(ch_stack[i], end='')
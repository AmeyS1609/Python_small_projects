def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    line1=line2=lin3=lin4=''
    R=[]
    Q=[]
    P=[]
    S=[]
    if show_answers:
        for char in problems:
            L=char.split()
            s1,op,s2=L
            if op not in ['+','-']:
                return "Error: Operator must be '+' or '-'."
            if not s1.isdigit() or not s2.isdigit():
                return 'Error: Numbers must only contain digits.'
            if len(s1)>4 or len(s2)>4:
                return 'Error: Numbers cannot be more than four digits.'
            size=max(len(s1),len(s2))+2
            R.append(s1.rjust(size))
            P.append(op+' '+s2.rjust(size-2))
            Q.append('-'*size)
            if op=='+':
                S.append(str(int(s1)+int(s2)).rjust(size))
            else:
                S.append(str(int(s1)-int(s2)).rjust(size))   
            line1='    '.join(R)#distance between each problem is 4 spaces so
            line2 = '    '.join(P)#distance between each problem is 4 spaces so
            line3='    '.join(Q)#distance between each problem is 4 spaces so
            line4='    '.join(S)#distance between each problem is 4 spaces so
        return line1+'\n'+line2+'\n'+line3+'\n'+line4
    for char in problems:
        L=char.split()
        s1,op,s2=L
        if op not in ['+','-']:
            return "Error: Operator must be '+' or '-'."
        if not s1.isdigit() or not s2.isdigit():
           return 'Error: Numbers must only contain digits.'
        if len(s1)>4 or len(s2)>4:
             return 'Error: Numbers cannot be more than four digits.'
        size=max(len(s1),len(s2))+2
        R.append(s1.rjust(size))
        P.append(op+' '+s2.rjust(size-2))
        Q.append('-'*size)
    line1='    '.join(R)#distance between each problem is 4 spaces so
    line2 = '    '.join(P)#distance between each problem is 4 spaces so
    line3='    '.join(Q)#distance between each problem is 4 spaces so
    return line1+'\n'+line2+'\n'+line3
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
#rjust(x) right-aligns a string within a space of width x.
#It adds spaces to the left so that the total length becomes x.
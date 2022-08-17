# making a function that counts as and bs
def count():
    string=input('Give your answer: ')
    a=string.count('a')
    b=string.count('b')
    if a==b:
        print(bool(True))
    else:
        print(bool(False))    
count()        
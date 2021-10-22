import string
#Python yield 
def add():
    i = 0
    while True:
        yield i+i
        i +=1
    
for i in add():
    if i >50:
        print("\n")
        break
    print(i,end=" ")

# Iterators in Python
atoz = [i for i in string.ascii_lowercase]
iterator_object = iter(atoz)
while True:
    try:
        print(next(iterator_object),end=" ")
    except:
        break

#utilizzo di global:
a = 10

def f1():
    global a
    a = 20
    print("nella funzione: ", a)

print(a)
f1()
print("dopo: ", a)


file = open('python.png', 'rb')
byte = file.read(1)
i = 0
while byte:    
    print(f"{i}: {byte}")
    byte = file.read(1)
    i += 1
file.close()
    
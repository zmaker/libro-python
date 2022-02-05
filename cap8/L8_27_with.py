# 1 - scrittura non protetta
file = open('readme.txt', 'w')
file.write('hello world !')
file.close()
  
# 2 - scrittura protetta con try except
file = open('readme.txt', 'w')
try:
    file.write('hello world')
finally:
    file.close()
 
# 3 - scrittura con with
with open('readme.txt', 'w') as file:
    file.write('hello world !')
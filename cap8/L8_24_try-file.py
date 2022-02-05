try:
    f = open('readme.txt', 'w')
    #operazioni sul file
except:
    print("file error")
finally:
    f.close()

import os, time
f = open("myfile.txt", "x")
f.close()
time.sleep(2)
os.remove("myfile.txt")

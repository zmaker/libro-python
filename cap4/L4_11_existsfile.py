import os
if os.path.exists("demofile.txt"):
    print("Il file esiste: lo cancello!")
    os.remove("demofile.txt")
else:
    print("Il file non esiste, lo creo...")
    f = open("demofile.txt", "x")
    f.close()

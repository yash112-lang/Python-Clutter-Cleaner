import os


files = os.listdir()
# files.remove(Files_cleaner.py)
print(files)

try:

    def CheckIfDoesntExist(folder):
        if (folder not in files):
            os.makedirs(folder)



    CheckIfDoesntExist("Images")
    CheckIfDoesntExist("Documents")
    CheckIfDoesntExist("Media")


    #Moving Images into Images Folder

    for i in files:
        a = os.path.splitext(i)[1]
        print(a)
        a.lower()
        if (a == ".png" or a == ".jpg" or a == ".jfif"):
            os.replace(i,f"Images/{i}")

    #Moving music files into media folder
    for i in files:
        a = os.path.splitext(i)[1]
        print(a)
        a.lower()
        if (a == ".mp3" or a == ".3gp" or a == ".wav" or a == "webm"):
            os.replace(i,f"Media/{i}")

    #moving document files in Documents folder

    for i in files:
        a = os.path.splitext(i)[1]
        print(a)
        a.lower()
        if (a == ".doc" or a == ".pdf" or a == ".ppt"):
            os.replace(i,f"Documents/{i}")
    


except Exception as e:
    print(e)
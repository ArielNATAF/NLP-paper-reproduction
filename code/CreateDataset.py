'''
Create a new dataset with new filenames, and removed metadata. 
Renamed corpora are in the Datasets/ folder in this repo
Original corpora for all languages can be downloaded from MERLIN website
http://www.merlin-platform.eu/C_data.php
'''

import os

dirpath = "../Datasets/" #CZ_ltext_txt", DE_ltext_txt, IT_ltext_txt
outputdirpath = "../Datasets/"
files = os.listdir(dirpath)
print(files)

inputdirs = ["CZ_ltext_txt", "DE_ltext_txt", "IT_ltext_txt"]
outputdirs = ["CZ","DE","IT"]

for i in range(0, len(inputdirs)):
    files = os.listdir(os.path.join(dirpath,inputdirs[i]))
    for file in files:
        print(file)
        if file.endswith(".txt"):
            content = open(os.path.join(dirpath,inputdirs[i],file),"r").read()
            cefr = content.split("Learner text:")[0].split("Overall CEFR rating: ")[1].split("\n")[0]
            newname = file.replace(".txt","") + "_" + outputdirs[i] + "_" + cefr + ".txt"
            fh = open(os.path.join(outputdirpath,outputdirs[i],newname), "w")
            text = content.split("Learner text:")[1].strip()
            print("wrote: ", os.path.join(outputdirpath,outputdirs[i],newname))


# il prend le jeux des données du merlin et enleve les méta data (informations sur le fichier)
# il nous manque les fichiers ltext_text pour lancer ce script 
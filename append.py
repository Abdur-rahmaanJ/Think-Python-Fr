from os import listdir
from os.path import isfile, join

mypath = '../translated'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for f in onlyfiles:
    with open(f, 'r', encoding="utf8") as trf:
        with open('newf.md', 'a', encoding="utf8") as mdf:
            mdf.write(trf.read())
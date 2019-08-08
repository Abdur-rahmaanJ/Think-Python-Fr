from os import listdir
from os.path import isfile, join

mypath = '../translated'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for f in onlyfiles:
    with open(f, 'r', encoding="utf8") as trf:
        with open('newf.md', 'a', encoding="utf8") as mdf:
            mdf.write(trf.read())

Python Project of the Week



Made an Open Inventory Mangement solution called Shopyo (shop+py+open). It's designed to be a localhost app!



Months ago i was searching github, looking for a point of sales solution using Python. What pricked me was that a good many had an annoying point. Some mandatorily required Posgres as though it ships with your computer, others codebases' were a tkinter spaghetti mess, others were django-based accounting monsters ...



I decided to give it a try, modelling it after a client request i once got. Made it flask-based with sqlalchemy+sqlite. You can instantly get started with no hassle, switching to something powerful when you want to (since it uses an ORM)



For the UI, we used the latest, bootstrap4, fa5 and jq3. Interestingly enough, i had two shop owners try it, the usage simplicity was praised.



It's still in dev and supports instant lookup. Long story short, with some programming skills, you can solve some everyday problems. And yes, no cdn, all libs are bundled so that you can use it completely offline.



Github: https://github.com/Abdur-rahmaanJ/shopyo



If you want to contributee, go ahead, we ❤️ it. Don't be afraid, we follow a 💯 % first-timers-friendly policy.



Cedric Poilly - That's where i use web

Jean Paul Fortuno - Flask XD

#python 
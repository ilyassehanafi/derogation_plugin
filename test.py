from os import listdir
from os.path import join
import os.path

random=1
onlyfiles = [f for f in listdir(r'C:\Users\ilyasse2.0\Desktop\points_derogation') if os.path.isfile(join(r'C:\Users\ilyasse2.0\Desktop\points_derogation', f))]
fn1='points' + str(random) +'.shp'
a = 0
i = 0
print(onlyfiles)
while a < len(onlyfiles):
    if (onlyfiles[i] == fn1) :
        random += 1
        fn1 = 'points' + str(random) + '.shp'
    a += 1
    i += 1
print(random)
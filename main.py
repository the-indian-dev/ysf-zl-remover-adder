print("Programmed by @the_indian_dev")
import os
directory = os.listdir('./input')
for old in directory:
    print("Now working on {} file.".format(old))
    f = open('./input/{}'.format(old),'r')
    lst = []
    for line in f:
        if 'ZL' in line:
            line = line.replace("ZL",'')
            print("Removing ZL line from {}".format(old))
            lst.append(line)
        elif '     ' in line:
            line = line.replace("     ",'ZL')
            print("Now adding ZL line to {}".format(old))
            lst.append(line)
    f.close()
    old_name,old_ext = tuple(old.split("."))
    f = open('./output/{}.dnm'.format(old_name),'w')
    for line in lst:
        f.write(line)
    f.close()

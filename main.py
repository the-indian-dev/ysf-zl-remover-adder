print("Programmed by @the_indian_dev")
import os
directory = os.listdir('./input')
for old in directory:
    f = open('./input/{}'.format(old),'r')
    lst = []
    for line in f:
        if 'ZL' in line:
            line = line.replace(word,'')
        lst.append(line)
        elif '     ' in line:
            line = line.replace(word,'ZL')
        lst.append(line)
    f.close()
    old_name,old_ext = tuple(old.split("."))
    f = open('./output/{}.dnm'.format(old_name),'w')
    for line in lst:
        f.write(line)
    f.close()

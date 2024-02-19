import os

#CHANGE DEPENDING ON LANGUAGE EDITION - will allow for separate directories for language editions
lang = "english"

#Where the articles should end up
current_dir = "C:\\Users\\Admin\\Desktop\\Computer_Scence\\academic_shet\\Diss"
new_dir = "Articles{}".format(lang)
write = False
smallfile = None
i = 0
n = 0
path = os.path.join(current_dir, new_dir)
if not os.path.isdir("C:\\Users\\Admin\\Desktop\\Computer_Scence\\academic_shet\\Diss\\Articles{}".format(lang)):
    os.mkdir(path)
with open('data\\{}.xml'.format(lang), encoding='utf-8', errors="replace") as bigfile:
    
    for line in bigfile:
            if "<page>" in line:
                 write = True
            if n < 1577348 and write is True:
                n = n + 1
                write = False
                continue
            if write == True:
                if smallfile:
                    smallfile.close()
                small_filename = 'C:\\Users\\Admin\\Desktop\\Computer_Scence\\academic_shet\\Diss\\Articles{}\\article{}.xml'.format(lang,n)
                smallfile = open(small_filename, "a", encoding='utf-8')
                smallfile.write(line)
            if "</page>" in line:
                 write = False
                 n = n + 1
    if smallfile:
        smallfile.close()
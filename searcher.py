import os
import re
import string


#CHANGE DEPENDING ON LANGUAGE EDITION - will allow for separate directories for language editions
lang = "english"

search_criteria = "United Kingdom"




#iterate through articles("article"+i+".xml")
            #open as read
            #if contain criteria copy to next dir
            #otherwise delete

dir = os.fsencode("C:\\Users\\Admin\\Desktop\\Computer_Scence\\academic_shet\\Diss\\Articles{}_Filtered".format(lang))


path = "C:\\Users\\Admin\\Desktop\\Computer_Scence\\academic_shet\\Diss\\Articles{}_Filtered2".format(lang)
if not os.path.isdir("C:\\Users\\Admin\\Desktop\\Computer_Scence\\academic_shet\\Diss\\Articles{}_Filtered2".format(lang)):
    os.mkdir(path)

for i in os.listdir(dir):
    lines= []
    count = 0
    found = False
    filename = os.fsdecode(i)
    file = open("C:\\Users\\Admin\\Desktop\\Computer_Scence\\academic_shet\\Diss\\Articles{}_Filtered\\{}".format(lang, filename), "r", encoding="utf-8", errors="replace")
    for ii in file:
        count = count + 1
        lines.append(ii)
        if search_criteria in ii:
            #print("found in "+filename)
            found = True
        if count > 65 and found == False:
            break

    if found == False:
        None
        #delete file?
    elif found == True:
        #if criteria achieved write to different directory

        file_new = open("C:\\Users\\Admin\\Desktop\\Computer_Scence\\academic_shet\\Diss\\Articles{}_Filtered2\\{}".format(lang, filename), "a", encoding="utf-8")
        for line in lines:
            file_new.write(line)
        file_new.close()
    file.close()
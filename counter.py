import os
import csv

#CHANGE DEPENDING ON LANGUAGE EDITION - will allow for separate directories for language editions
lang = "vietnamese"

appendix = "Total"


counts = [['reference_count','internal_links','word_count','file_size','image_count']]

current_count = [0,0,0,0,0]

count_line = 0


dir = os.fsencode("C:\\Users\\Admin\\Desktop\\Computer_Scence\\academic_shet\\Diss\\Articles{}_Filtered{}".format(lang, appendix))
    
for i in os.listdir(dir):
    filename = os.fsdecode(i)
    file = open("C:\\Users\\Admin\\Desktop\\Computer_Scence\\academic_shet\\Diss\\Articles{}_Filtered{}\\{}".format(lang, appendix, filename), "r", encoding="utf-8", errors="replace")
    current_count = [0,0,0,0,0]
    file_size = os.path.getsize("C:\\Users\\Admin\\Desktop\\Computer_Scence\\academic_shet\\Diss\\Articles{}_Filtered{}\\{}".format(lang, appendix, filename))
    for ii in file:
        count_line = count_line + 1
        count_reference = ii.count("[[")
        count_internal = ii.count("{{")
        count_word = ii.count(" ")
        count_image = ii.count(":Image:")
        current_count[0] = current_count[0] + count_reference
        current_count[1] = current_count[1] + count_internal
        current_count[2] = current_count[2] + count_word
        current_count[4] = current_count[4] + count_image
    current_count[3] = file_size
    counts.append(current_count)
    file_size = 0

file = open("C:\\Users\\Admin\\Desktop\\Computer_Scence\\academic_shet\\Diss\\metrics_{}{}.txt".format(lang, appendix), "w", encoding="utf-8", errors="replace")
    
for i in counts:
    ii = "/ "+str(i[0])+"/ "+str(i[1])+"/ "+str(i[2])+"/ "+str(i[3])+"/ "+str(i[4])+"/ "
    file.write(ii)
    file.write("\n")

file.close


with open("C:\\Users\\Admin\\Desktop\\Computer_Scence\\academic_shet\\Diss\\metrics_{}{}.csv".format(lang, appendix), "w", encoding="utf-8", errors="replace") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in counts:
            writer.writerow(line)

#print(counts)

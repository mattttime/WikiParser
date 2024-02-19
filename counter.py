import os

#CHANGE DEPENDING ON LANGUAGE EDITION - will allow for separate directories for language editions
lang = "Eng"

count_criteria = "[["

counts = []

current_count = 0

count_line = 0


dir = os.fsencode("C:\\Users\\Admin\\Desktop\\Computer_Scence\\academic_shet\\Diss\\Articles{}".format(lang))
    
for i in os.listdir(dir):
    filename = os.fsdecode(i)
    file = open("C:\\Users\\Admin\\Desktop\\Computer_Scence\\academic_shet\\Diss\\Articles{}\\{}".format(lang, filename), "r", encoding="utf-8", errors="replace")
    for ii in file:
        count_line = ii.count(count_criteria)
        current_count = current_count + count_line
    counts.append(current_count)
    current_count = 0
    count_line = 0

sum_count = 0
for i in counts:
    sum_count = sum_count + i

avg_count = sum_count / len(counts)

print(counts)
print(avg_count)
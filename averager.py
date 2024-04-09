import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statistics as st

#CHANGE DEPENDING ON LANGUAGE EDITION - will allow for separate directories for language editions
lang = "Vietnamese"

appendix = "Vietnam"

metrics = []
ref_count = []
internal_count = []
word_count = []
file_size = []




df = pd.read_csv("C:\\Users\\Admin\\Desktop\\Computer_Scence\\academic_shet\\Diss\\metrics_{}{}.csv".format(lang, appendix), encoding="utf-8")
ref_count = df['reference_count'].tolist()
internal_count = df['internal_links'].tolist()
word_count = df['word_count'].tolist()
file_size = df['file_size'].tolist()
image_count = df['image_count'].tolist()


ref_count = sorted(ref_count)
internal_count = sorted(internal_count)
word_count = sorted(word_count)
file_size = sorted(file_size)
image_count = sorted(image_count)

avg_size = 0
avg_ref = 0
avg_internal = 0
avg_word = 0
avg_image = 0
new_ref_count = []
new_word_count = []
new_file_size = []
new_internal_count = []
new_image_count = []
new_avg_size = 0
new_avg_ref = 0
new_avg_internal = 0
new_avg_word = 0
new_avg_image = 0

for i in ref_count:
    avg_ref = avg_ref + i
stdev_ref = st.stdev(ref_count)
avg_ref = avg_ref / len(ref_count)
outlier_barrier = stdev_ref * 2.5
max_ref = max(ref_count)
for i in ref_count:
    if int(i) > avg_ref + outlier_barrier or int(i) < avg_ref - outlier_barrier:
        continue
    else:
        new_ref_count.append(i)
for i in new_ref_count:
    new_avg_ref = new_avg_ref + i
new_avg_ref = new_avg_ref / len(new_ref_count)

print("Average Ref: "+str(avg_ref))
print("Max Ref: "+str(max_ref))
print("Average Ref Without Outliers: "+str(new_avg_ref))

for i in word_count:
    avg_word = avg_word + i
stdev_word = st.stdev(word_count)
avg_word = avg_word / len(word_count)
outlier_barrier = stdev_word * 2.5
max_word = max(word_count)
for i in word_count:
    if int(i) > avg_word + outlier_barrier or int(i) < avg_word - outlier_barrier:
        continue
    else:
        new_word_count.append(i)
for i in new_word_count:
    new_avg_word = new_avg_word + i
new_avg_word = new_avg_word / len(new_word_count)

print("Average Words: "+str(avg_word))
print("Max Words: "+str(max_word))
print("Average Words Without Outliers: "+str(new_avg_word))

for i in file_size:
    avg_size = avg_size + i
stdev_size = st.stdev(file_size)
avg_size = avg_size / len(file_size)
outlier_barrier = stdev_size * 2.5
max_size = max(file_size)
for i in file_size:
    if int(i) > avg_size + outlier_barrier or int(i) < avg_size - outlier_barrier:
        continue
    else:
        new_file_size.append(i)
for i in new_file_size:
    new_avg_size = new_avg_size + i
new_avg_size = new_avg_size / len(new_file_size)

print("Average Size: "+str(avg_size))
print("Max Size: "+str(max_size))
print("Average Size Without Outliers: "+str(new_avg_size))

for i in internal_count:
    avg_internal = avg_internal + i
stdev_internal = st.stdev(internal_count)
avg_internal = avg_internal / len(internal_count)
outlier_barrier = stdev_internal * 2.5
max_internal = max(internal_count)
for i in internal_count:
    if int(i) > avg_internal + outlier_barrier or int(i) < avg_internal - outlier_barrier:
        continue
    else:
        new_internal_count.append(i)
for i in new_internal_count:
    new_avg_internal = new_avg_internal + i
new_avg_internal = new_avg_internal / len(new_internal_count)

print("Average Internal: "+str(avg_internal))
print("Max Internal: "+str(max_internal))
print("Average Internal Without Outliers: "+str(new_avg_internal))

for i in image_count:
    avg_image += i
stdev_image = st.stdev(image_count)
avg_image = avg_image / len(image_count)
outlier_barrier = stdev_image * 2.5
max_image = max(image_count)
for i in image_count:
    if int(i) > avg_image + outlier_barrier or int(i) < avg_image - outlier_barrier:
        continue
    else:
        new_image_count.append(i)
for i in new_image_count:
    new_avg_image = new_avg_image + i
new_avg_image = new_avg_image / len(new_image_count)

print("Average Images: "+str(avg_image))
print("Max Images: "+str(max_image))
print("Average Images Without Outliers: "+str(new_avg_image))

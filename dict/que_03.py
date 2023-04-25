#Write a Python script to concatenate the following dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
d4={}
for d in (dic1,dic2,dic3):d4.update(d)
print(d4)
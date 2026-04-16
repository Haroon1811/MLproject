""""
file = open("python.txt", "a")
file.write("API integration practice\n")
file.write("API integration practice\n")
file = open("python.txt", "r")
print(file.read())
file.close()



import pandas as pd

df = pd.DataFrame({"1":[1,2,3,4],"2":[2,3,4,5]})
print(df)

df.to_csv("df.csv", index = False)  #ata frame to csv file 
f = pd.read_csv("df.csv")            # reading the csv file 
print(f)

# for creating excel files 
import openpyxl

df.to_excel("df.xlsx", index=False)
f1 = pd.read_excel("df.xlsx")
print(f1)

# json file creation

df.to_json("df.json")
f2 = pd.read_json("df.json")
print(f2)


"""


import pandas as pd
import json 
data =  {
    "name" : ["hnojk"],
    "age" : [30],
    "city" : ["new york"]
}


df = pd.DataFrame(data)
print(df)

df.to_json("new.json")

with open("new.json", "r") as file:
    d = json.load(file)



# write data tofile

with open("new.json", "w") as f:
    json.dump(data, f)

with open("new.json", "r") as f:
    a = json.load(f)
print(a)
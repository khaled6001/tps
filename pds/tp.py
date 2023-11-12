import numpy as np
import pandas as pd

header =["dep_1", "dep_2", "dep_3", "dep_4"]
value = [[45200, 65190, 10000,33500],
         [16000, 11500, 8550, 73200],
         [13050, 15000, 22050, 8030]]
materiel = ["Iron", "Copper", "Aluminum"]
footer = ["Product", "...", "...", "...", "..."]
data = {"head" : header,
        "materiel" : materiel,
        "value" : value,
        "footer" : footer
        }
print (data)
maxValueDep = np.max(data["value"], 0)
maxValueMat = np.max(data["value"], 1)
# data = np.array(data)
# data = pd.Series(data)
print(f"{data['materiel'][0]}, value max = {maxValueMat[0]} kg\n"+
      f"{data['materiel'][1]}, value max = {maxValueMat[1]} kg\n"+
      f"{data['materiel'][2]}, value max = {maxValueMat[2]} kg\n")
index = np.argwhere(data["value"] ==np.max(data["value"], 0))
print(f"{data['head'][index[0][1]]}, {data['materiel'][index[0][0]]}, value max = {maxValueDep[0]} kg\n"+
      f"{data['head'][index[1][1]]}, {data['materiel'][index[1][0]]}, value max = {maxValueDep[1]} kg\n"+
      f"{data['head'][index[3][1]]}, {data['materiel'][index[3][0]]}, value max = {maxValueDep[2]} kg\n"+
      f"{data['head'][index[2][1]]}, {data['materiel'][index[2][0]]}, value max = {maxValueDep[3]} kg\n ")
average = np.round(np.average(value, 0), 2)
print (f"average {data['head'][index[0][1]]} = {average[0]}\n"+
       f"average {data['head'][index[1][1]]} = {average[1]}\n"+
       f"average {data['head'][index[2][1]]} = {average[2]}\n"+
       f"average {data['head'][index[3][1]]} = {average[3]}\n")
print (value[1])
def Product(val1, val2, val3):
    newVal1 = np.empty(4)
    newVal2 = np.empty(4)
    newVal3 = np.empty(4)
    product = np.empty(4)
    for i in range (len(val1)):
        newVal1[i]=val1[i]/10;newVal2[i]=val2[i]/5;newVal3[i]=val3[i]/6
        product[i] =np.min([newVal1[i], newVal2[i], newVal3[i]])
    rest = [val1-product[0]*10, val2-product[1]*5,  val3-product[2]*6]
    remining = [rest[0]*3, rest[1]*8, rest[2]*6]
    return np.round(product), np.round(rest), remining
print(f"pices = {Product(value[0], value[1], value[2])[0]},\n"+
      f"rest = {Product(value[0], value[1], value[2])[1]},\n"+
      f"remining ={Product(value[0], value[1],value[2])[2]},\n"+
      f"sum remining = {sum(Product(value[0], value[1],value[2])[2])},\n"+
      f"sum = {sum(sum(Product(value[0], value[1],value[2])[2]))}")


    
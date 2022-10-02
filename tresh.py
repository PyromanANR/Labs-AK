import openpyxl
import math 

book = openpyxl.open('date.xlsx',read_only=True)
sheet = book.active 
cells = sheet['B3':'G34']
mouth__dif = 0
result_=list()
for Y1, M1, Y2, M2, V2, Tmoor in cells:
    mouth__dif = ((Y2.value - Y1.value) * 12 + M2.value - M1.value) / Tmoor.value
    # print(mouth__dif)
    
    power = pow(mouth__dif , 2 )
    # print (power)
    
    result = V2.value/power
    result=round(result , 2)
    result_.append(result)

print(result_)
    


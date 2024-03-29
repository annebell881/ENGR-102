# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 14:25:18 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 9 write
# Date:         18 10 2020

##### 5 MPa Data #####
# temperature in degrees C
tempC5 = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260]
# specific volume in m^3/kg
v5 = [0.0009977, 0.0009996, 0.0010057, 0.0010149, 0.0010267, 0.001041, 
      0.0010576, 0.0010769, 0.0010988, 0.001124, 0.0011531, 0.0011868, 
      0.0012268, 0.0012755]
# internal energy in kJ/kg
u5 = [0.04, 83.61, 166.92, 250.29, 333.82, 417.65, 501.91, 586.8, 672.55,
      759.47, 847.92, 938.39, 1031.6, 1128.5]
# enthalpy in kJ/kg
h5 = [5.03, 88.61, 171.95, 255.36, 338.96, 422.85, 507.19, 592.18, 
      678.04, 765.09, 853.68, 944.32, 1037.7, 1134.9]
# entropy in kJ/(kg K)
s5 = [0.0001, 0.2954, 0.5705, 0.8287, 1.0723, 1.3034, 1.5236, 1.7344, 
      1.9374, 2.1338, 2.3251, 2.5127, 2.6983, 2.8841]

#open file
outFile = open('Lab9_ThermoProperties.csv', "w")

#write in the file
outFile.write ("5 Mpa data")

for i in range (len(s5)):
    outFile.write((str(tempC5[i])) + ",")
    outFile.write((str(v5[i])) + ", ")
    outFile.write((str(u5[i])) + ", ")
    outFile.write((str(h5[i])) + ", ")
    outFile.write((str(s5[i])))
    outFile.write('\n')
    
    


##### 10 MPa Data #####
# temperature in degrees C
tempC10 = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260]
# specific volume in m^3/kg
v10 = [0.0009952, 0.0009973, 0.0010035, 0.0010127, 0.0010244, 0.0010385,
       0.0010549, 0.0010738, 0.0010954, 0.0011200, 0.0011482, 0.0011809,
       0.0012192, 0.0012653]
# internal energy in kJ/kg
u10 = [0.12, 83.31, 166.33, 249.43, 332.69, 416.23, 500.18, 584.72,
       670.06, 756.48, 844.32, 934.01, 1026.2, 1121.6]
# enthalpy in kJ/kg
h10 = [10.07, 93.28, 176.37, 259.55, 342.94, 426.62, 510.73, 595.45,
       681.01, 767.68, 855.8, 945.82, 1038.3, 1134.3]
# entropy in kJ/(kg K)
s10 = [0.0003, 0.2943, 0.5685, 0.826, 1.0691, 1.2996, 1.5191, 1.7293,
       1.9316, 2.1271, 2.3174, 2.5037, 2.6876, 2.871]

outFile.write ("10 Mpa data")
for i in range (len(s10)):
    outFile.write((str(tempC10[i])) + ",")
    outFile.write((str(v10[i])) + ", ")
    outFile.write((str(u10[i])) + ", ")
    outFile.write((str(h10[i])) + ", ")
    outFile.write((str(s10[i])))
    outFile.write('\n')
    
    
    

#close file
outFile.close()

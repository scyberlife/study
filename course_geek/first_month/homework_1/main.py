# created a variable for frequently used text
repeat = 'Enter the air temperature for today in'
# output welcome message to screen
print('Welcome to the program for calculating the average air temperature in Kyrgyzstan!')
# assign temperature values for each region to their respective variables
temp_chuyskaya = float(input(repeat + ' Chui region '))
temp_talas = float(input(repeat + ' Talas region '))
temp_issicul = float(input(repeat + ' Issyk-Kul region '))
temp_narinsk = float(input(repeat + ' Naryn region '))
temp_osh = float(input(repeat + ' Osh region '))
temp_oshh = float(input(repeat + ' Osh city '))
temp_dgaal = float(input(repeat + ' Jalal-Abad region '))
temp_batken = float(input(repeat + ' Batken region '))
temp_bishkek= float(input(repeat + ' Bishkek '))
# calculate the average temperature
summ_temp = float((temp_chuyskaya + temp_talas + temp_issicul + temp_narinsk + temp_osh + temp_dgaal + \
                   temp_batken + temp_bishkek + temp_oshh)/9)
# display result with floating point value rounded to one decimal place
print("The average air temperature in Kyrgyzstan for today is {} °C.".format(round(summ_temp, 1)))

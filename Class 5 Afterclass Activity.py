Temp_type = input("Enter the temperature type for Celsius(C)/ Farenheit(F)/ Kelvin(K): ")
Temp_type.lower()
Current_Temp = float(input("Enter the current temperature: "))

if Temp_type == "c" and Current_Temp >= 24 or Temp_type == "f" and Current_Temp >= 75 or Temp_type == "k" and Current_Temp >= 297 :
    print("It's warm outside, light clothes are recommended")
else:
    print("It's cold outside, Wearing jackets is necessary")
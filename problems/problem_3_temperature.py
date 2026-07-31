"""
Convert a temperature from Fahrenheit to Celsius
"""
temp_f = float(input("Temp in °F: "))

# Calculate it in Celsius
temp_c = (temp_f - 32) * 5 / 9

print(f"Temp in °C: {round(temp_c, 1)}")

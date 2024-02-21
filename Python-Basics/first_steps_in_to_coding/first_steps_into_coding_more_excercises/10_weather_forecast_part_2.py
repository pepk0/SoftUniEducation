temperature_celsius = float(input())

if temperature_celsius >= 26.00 and temperature_celsius <= 35.00:
    whether = "Hot"
elif temperature_celsius >= 20.1 and temperature_celsius <= 25.9:
    whether = "Warm"
elif temperature_celsius >= 15.0 and temperature_celsius <= 20.0:
    whether = "Mild"
elif temperature_celsius >= 12.00 and temperature_celsius <= 14.9:
    whether = "Cool"
elif temperature_celsius >= 5.00 and temperature_celsius <= 11.9:
    whether = "Cold"
else:
    whether = "unknown"

print(whether)
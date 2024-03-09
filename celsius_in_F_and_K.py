FAHRENGAIT_MULTIPLIER = 9 / 5
FAHRENHAIT_APENDIX = 32
KELVIN_APENDIX = 273.15

celsius_input = int(input('Enter the value of celsius that you want to transfer to KELVIN and FAHRENHAIT: '))

fahrenheit_result = ((celsius_input * FAHRENGAIT_MULTIPLIER) + FAHRENHAIT_APENDIX)
kelvin_result = celsius_input + KELVIN_APENDIX


print ("F = ", fahrenheit_result, "\nK = ", kelvin_result )

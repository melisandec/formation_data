# 9 - Temperature Converter: Implement a function that converts temperatures from Celsius to Fahrenheit and vice versa.
def temp_convert(n):
    celsius=float(n)
    fahrenheit = (celsius * 1.8) + 32
    f = fahrenheit
    print(f)

temp_convert(10)
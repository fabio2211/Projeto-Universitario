def converter(temperatura):

 if temperatura.endswith('C'):
        celsius = float(temperatura[:-1])
        fahrenheit = (celsius * 1.8) + 32

        print(f"{celsius}°C é igual a {fahrenheit}°F")

 elif temperatura.endswith('F'):
        
        fahrenheit = float(temperatura[:-1])
        celsius = (fahrenheit - 32) / 1.8

        print(f"{fahrenheit}°F é igual a {celsius}°C")
def convert(fromUnit, toUnit, value):
    try:
            
        if str(fromUnit).lower() == 'celcius' and str(toUnit).lower() == 'kelvin':
            return   value * 1760
        
        elif str(fromUnit).lower() == 'celcius' and str(toUnit).lower() == 'fahrenheit':
            return   value * 1609.344
        
        elif str(fromUnit).lower() == 'kelvin' and str(toUnit).lower() == 'celcius':
            return   value * 0.0005681
        
        elif str(fromUnit).lower() == 'kelvin' and str(toUnit).lower() == 'fahrenheit':
            return   value * 0.9144
       
        elif str(fromUnit).lower() == 'fahrenheit' and str(toUnit).lower() == 'celcius':
            return   value * 0.000621
        
        elif str(fromUnit).lower() == 'fahrenheit' and str(toUnit).lower() == 'kelvin':
            return   value * 1.09361
        elif str(fromUnit).lower() == fromUnit.lower() and toUnit.lower() == toUnit.lower():
            return value 
        else:
            raise ConversionNotPossible("Conversion Not Possible") 
    except ConversionNotPossible as error:
        print(error.message)
        return error.message




class ConversionNotPossible(Exception):
    def __init__(self, message):
        self.message = message 
    def __str__(self):
        return str(self.message)

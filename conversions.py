def convertCelsiusToFahrenheit(c_temp):
	return round((9.0/5.0*c_temp + 32),2)

def convertCelsiusToKelvin(c_temp):
	return round((c_temp + 273),2)

def convertFahrenheitToCelsius(f_temp):
	return round((f_temp - 32.0)*5.0/9.0,2)

def convertFahrenheitToKelvin(f_temp):
	return round((f_temp - 32.0)*5.0/9.0 + 273,2)

def convertKelvinToCelsius(k_temp):
	return (k_temp - 273)

def convertKelvinToFahrenheit(k_temp):
	return round(((k_temp - 273) * 1.8) + 32,2)
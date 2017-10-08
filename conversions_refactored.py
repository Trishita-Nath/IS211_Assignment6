def convert(fromUnit,toUnit,value):
	if(fromUnit=="miles" and toUnit=="yards"):
		return round(value * 1760 ,2)
	elif(fromUnit=="yards" and toUnit=="miles"):
		return round(value * 0.00056818 ,2)
	elif(fromUnit=="yards" and toUnit=="meters"):
		return round(value / 1.0936 ,2)
	elif(fromUnit=="meters" and toUnit=="yards"):
		return round(value * 1.094 ,2)
	elif(fromUnit=="miles" and toUnit=="meters"):
		return round(value / 0.00062137 ,2)
	elif(fromUnit=="meters" and toUnit=="miles"):
		return round(value * 0.00062137 ,2)
	elif(fromUnit == toUnit):
		return value				

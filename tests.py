import unittest
import conversions
import conversions_refactored

class TestStringMethods(unittest.TestCase):

	def test_convertCelsiusToKelvin(self):
		self.assertEqual(conversions.convertCelsiusToKelvin(100.0),373)
		self.assertEqual(conversions.convertCelsiusToKelvin(0),273.0)
		self.assertEqual(conversions.convertCelsiusToKelvin(50.0),323.0)
		self.assertEqual(conversions.convertCelsiusToKelvin(75.0),348.0)
		self.assertNotEqual(conversions.convertCelsiusToKelvin(10),500)

	def test_convertKelvinToCelsius(self):
		self.assertEqual(conversions.convertKelvinToCelsius(373.0),100)
		self.assertEqual(conversions.convertKelvinToCelsius(323.0),50)
		self.assertEqual(conversions.convertKelvinToCelsius(573.0),300)
		self.assertEqual(conversions.convertKelvinToCelsius(0),-273)
		self.assertNotEqual(conversions.convertKelvinToCelsius(500.0),100)
		
	def test_convertCelsiusToFahrenheit(self):
		self.assertEqual(conversions.convertCelsiusToFahrenheit(100.0),212)
		self.assertEqual(conversions.convertCelsiusToFahrenheit(50.0),122)
		self.assertEqual(conversions.convertCelsiusToFahrenheit(150.0),302)
		self.assertEqual(conversions.convertCelsiusToFahrenheit(1),33.8)
		self.assertNotEqual(conversions.convertCelsiusToFahrenheit(100.0),555)

	def test_convertFahrenheitToCelsius(self):
		self.assertEqual(conversions.convertFahrenheitToCelsius(100.0),37.78)
		self.assertEqual(conversions.convertFahrenheitToCelsius(1.0),-17.22)
		self.assertEqual(conversions.convertFahrenheitToCelsius(50.0),10)
		self.assertEqual(conversions.convertFahrenheitToCelsius(75.0),23.89)
		self.assertNotEqual(conversions.convertFahrenheitToCelsius(100.0),337.78)

	def test_convertFahrenheitToKelvin(self):
		self.assertEqual(conversions.convertFahrenheitToKelvin(100.0),310.78)
		self.assertEqual(conversions.convertFahrenheitToKelvin(50.0),283)
		self.assertEqual(conversions.convertFahrenheitToKelvin(75.0),296.89)
		self.assertEqual(conversions.convertFahrenheitToKelvin(25.5),269.39)
		self.assertNotEqual(conversions.convertFahrenheitToKelvin(1.0),310.78)


	def test_convertKelvinToFahrenheit(self):
		self.assertEqual(conversions.convertKelvinToFahrenheit(100.0),-279.4)
		self.assertEqual(conversions.convertKelvinToFahrenheit(10.0),-441.4)
		self.assertEqual(conversions.convertKelvinToFahrenheit(50.0),-369.4)
		self.assertEqual(conversions.convertKelvinToFahrenheit(75.75),-323.05)
		self.assertNotEqual(conversions.convertKelvinToFahrenheit(0),-279.4)


	def test_convert(self):
		self.assertEqual(conversions_refactored.convert("meters","miles",10),0.01)
		self.assertEqual(conversions_refactored.convert("meters","yards",10),10.94)
		self.assertEqual(conversions_refactored.convert("miles","meters",10),16093.47)
		self.assertEqual(conversions_refactored.convert("miles","yards",10),17600)
		self.assertEqual(conversions_refactored.convert("yards","miles",50),0.03)
		self.assertEqual(conversions_refactored.convert("yards","meters",50),45.72)
		self.assertEqual(conversions_refactored.convert("yards","yards",50),50)
		self.assertRaises(TypeError,conversions_refactored.convert("yards","celsius",50))

	
		
			


if __name__ == '__main__':
    unittest.main()
from unittest import TestCase
import antennaclass

class DisplayAntennas(TestCase):
	def test_it_gives_correct_output(self):
		result = antenna_types(self,multiband=[900,1800,2100,800])
		self.assertEqual(result, 'Antenna is quadband', msg = "Antenna should be quadband")

#In wireless radio communications there are currently only four fixed bands
	def test_it_raises_an_error_if_wrong_band_values_supplied(self,multiband):
		self.assertNotIsInstance(multiband,[900,1800,2100,800], msg = "Wrong band value")

		


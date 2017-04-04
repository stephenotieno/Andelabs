class Antenna(object):
	#Antennae can have the following attributes:
	#directivity:
		#omnidirectional
		#semidirectional
		#directional
	#frequency:
		#singleband
		#dualband
		#triband
		#quadband

	def _init_(self, directivity, frequency):
		self.directivity = directivity
		self.frequency = frequency

	def antenna_directivity(self,directivity):
		if directivity == 'omnidirectional':
			print ('This type of antenna projects in all directions.')
		elif directivity == 'semidirectional':
			print ('This type of antenna projects at an angle sufficiently less than 360 degrees')
		elif directivity == 'directional':
			print ('This is used for point to point communications')
		else:
			print ('No such know type of antenna')

	def antenna_frequency(self,frequency):
		if frequency == 'singleband':
			print ('Can only transmit at a single frequency')
		elif frequency == 'dualband':
			print ('Can transmit two frequencies')
		elif frequency == 'triband':
			print ('Can transmit three frequencies')
		elif frequency == 'quadband':
			print ('Can transmit four frequencies')
		else:
			print ('No such anttenna')

	def radio_bands(self,band):
		if band == 900:
			print ('This is a wide coverage 2G band')
		elif band == 1800:
			print ('This is a narrower coverage 2G band')
		elif band == 2100:
			print ('This is a 3G band')
		elif band == 800:
			print ('This is a 4G band')
		else:
			print ('Know such band in wireless radio communications')

	def antenna_types(self,multiband=[]):
		if len(multiband)==4:
			output = quadband
		elif len(multiband)==3:
			output = triband
		elif len(multiband)==2:
			output = dualband
		else:
			output = singleband		
			
		return output






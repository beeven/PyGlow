#!/usr/bin/env python

import time
import multiprocessing

class Light(object):
	def __init__(self,addr):
		self.status = False
		self.addr = addr
		self.brightness = 0

	def set_brightness(self,brightness):
		self.brightness = brightness
		pass

	def turn_on(self):
		self.set_brightness(255);

	def turn_off(self):
		self.set_brightness(0)

	def ease_to(self,brightness,duration):
		'''
		brightness: The brightness of the light, 0 - 255
		duration: The duration to change the brightness from current to target, in milliseconds
		'''
		delta = brightness - self.brightness
		if delta == 0 :
			time.sleep(duration*1.0/1000)
			return

		timespan = abs(duration *1.0 / delta)
		for i in range(abs(delta)):
			self.set_brightness(self.brightness + delta)
			time.sleep(timespan / 1000)

		pass

	def ease_to_async(self,brightness,duration):
		'''
		Non-blocking version of function easeTo
		'''
		p = multiprocessing.Process(target=self.ease_to,args=(brightness,duration))
		p.start()
		pass


class LightSystem(object):
	def __init__(self):
		self.lights = [Light(i) for i in range(18)]

	def __flash__(self,lights,brightness,interval):
		'''
		interval: flashing interval, in milliseconds
		'''

		pass

	def __ease__(self,lights,brightness,duration):
		pass

	def __immediate__(self,lights,brightness):
		pass

	def show_number(self,number, effect):
		pass



	def show_IP(self,ipaddr,effect):
		pass
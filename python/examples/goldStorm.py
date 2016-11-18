# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time

from neopixel import *


# LED strip configuration:
LED_COUNT      = 280      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
	"""Draw rainbow that fades across all pixels at once."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def point(strip, wait_ms=20):
	"""single point on the line """

	for i in range(strip.numPixels()):
		clear(strip, i - 1)
		strip.setPixelColor(i, wheel(i & 255))
		strip.show()
		time.sleep(wait_ms / 1000.0)

def storm(strip, color=Color(255,255,255), wait_ms=20):
	""" Draw a storm """
	
	Imax = strip.numPixels() / 2.0
	for i in range(0, strip.numPixels()):
		strip.setPixelColor(i, color)
	
	times = [0.1, 0.1, 0.3, 0.6, 1]
	brightN = [20, 50, 100, 150, 255]
	for i in range(0, 5):
		strip.setBrightness(brightN[i])
		strip.show()
		time.sleep(times[i])
		strip.setBrightness(0)
		strip.show()
                time.sleep(0.1)



def clear(strip, n = -1):
	""" Clear the strip. If n > -1 then we clear only the 'n' LED. Otherwise,
	we'll clear the whole strip"""

	start = 0 if n == -1 else n
	stop = strip.numPixels() if n == -1 else n + 1

	for i in range(start, stop): 
		strip.setPixelColor(i, Color(0, 0, 0))
		strip.setBrightness(255)
	
	if n == -1: strip.show()


def rainbowCycle(strip, wait_ms=20, iterations=5):
	"""Draw rainbow that uniformly distributes itself across all pixels."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel(((i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)
	clear(strip)

def theaterChaseRainbow(strip, wait_ms=50):
	"""Rainbow movie theater light style chaser animation."""
	for j in range(256):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, wheel((i+j) % 255))
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)
	clear(strip)


	
# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
        # Intialize the library (must be called once before other functions).
	strip.begin()
	gold = Color(255,230,0)
        storm(strip,gold)
	#theaterChaseRainbow(strip)
	#rainbowCycle(strip,1,3)
	print ('Press Ctrl-C to quit.')

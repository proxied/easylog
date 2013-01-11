#!/usr/bin/env python

class EasyLog:
	# Usage: EasyLog(fname="log.txt",defType="INFO",showTime=True)
	def __init__(self, **attrs):
		self.__dict__.update(**attrs)
	def __getattr__(self, attr):
		return self.__dict__.get(attr, None)

	def setFname(self, fname):
		# The fname variable is the file that the log messages will be logged to.
		# Defaults to the string log.txt
		self.fname = fname

	def setDefType(self, defType):
		# The defType variable is the default log message type.
		# Defaults to the string INFO
		self.defType = defType

	def setShowTime(self, showTime):
		# The showTime variable determines whether a time stamp should be included in log messages.
		# Defaults to the boolean True
		self.showTime = showTime

	def log(self, text=""):
		print "DEBUG VERSION:"
		print "File:", self.fname, "- Type:", self.defType, "- Show Time: ", self.showTime, "- Text:", text
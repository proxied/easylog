#!/usr/bin/env python

from time import localtime, strftime

class EasyLog:
	# Usage: EasyLog(fname="log.txt",defType="INFO",showTime=True)

	def __init__(self, **attrs):
		self.__dict__.update(**attrs) # Add the given parameters into the dictionary

		defaultVariables = ["fname","defType","showTime","showType"] # Default variable list
		defaultValues = ["log.txt", "INFO", True, True] # Default values list

		for var in defaultVariables:
			if var not in self.__dict__:
				self.__dict__.update({var:defaultValues[defaultVariables.index(var)]}) # Add the variable (from defaultVariables) as the key, and the 
                                                                                                                                                                      # corresponding value from defaultValues into the dictionary
                                                                                                                                                                       
	def __getattr__(self, attr):
		return self.__dict__.get(attr, None) # Return the variable from the dictionary

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

	def setShowType(self, showType):
		# The showType variable determines whether the type of the log message should be included.
		# Defaults to the boolean True
		self.showType = showType

	def setVar(self, **attrs):
		# Edits any number of variables you want.
		# Example usage:    mylog.setVar(fname="logfile.txt", showTime=False)
		self.__dict__.update(**attrs)

	def log(self, text="", msgType=""):
		if  msgType == "": msgType = self.defType # If msgType not specified, set to the default
		curtime = strftime("%Y-%m-%d %H:%M:%S", localtime()) # Loads the current time into a string

		with open(self.fname, "a") as log: # Opens the log file for appending
			if self.showTime: log.write("(" + curtime + ") ")
			if self.showType: log.write("[" + msgType + "] ")
			log.write(text + "\n")
#!/usr/bin/env python

from time import localtime, strftime

class EasyLog:
	# Usage: EasyLog(fname="log.txt",defType="INFO",showTime=True)

	def __init__(self, **attrs):
		self.__dict__.update(**attrs) # Add the given parameters into the dictionary

		defaultVariables = ["fname","defType","showTime","showType","printLogs","defSubType"] # Default variable list
		defaultValues = ["log.txt", "INFO", True, True, False, "GENERAL"] # Default values list

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

	def setPrintLogs(self, printLogs):
		# The printLogs variable determines whether to print out log messages when they are written.
		# Defaults to the boolean False
		self.printLogs = printLogs

	def setDefSubType(self, defSubType):
		# The defSubType variable is the default log message subtype.
		# Defaults to the string GENERAL
		self.defSubType = defSubType

	def setVar(self, **attrs):
		# Edits any number of variables you want.
		# Example usage:    mylog.setVar(fname="logfile.txt", showTime=False)
		self.__dict__.update(**attrs)

	def log(self, text="", msgType="", subType=""):
		# Logs to fname a message in the following format:
		# (YYYY-MM-DD HH-MM-SS) [TYPE] Your message here.

		if  msgType == "": msgType = self.defType # If msgType not specified, set to the default
		if  subType == "":  subType = self.defSubType # If msgType not specified, set to the default

		curtime = strftime("%Y-%m-%d %H:%M:%S", localtime()) # Loads the current time into a string

		message = "(%s) [%s] {%s} %s\n" % (curtime, msgType, subType, text)

		with open(self.fname, "a") as log: # Opens the log file for appending
			log.write(message)

		if self.printLogs: print message # Prints out the log message if we are supposed to
 
	def search(self, text=""):
		# Searches through the log file and returns a list of lines that contain a string.

		with open(self.fname, "r") as log: # Opens the log file for reading
			loglist = log.readlines() # Put the log file into array, one line per index
			matches = []

			for line in loglist:
				if text in line: 
					matches.append(line)
			return matches

	def searchTime(self, hour=None, minute=None, second=None):
		# Searches through the log file and returns a list of lines that have specified time stamp
		# Note: hour, minute, and second must be strings

		with open(self.fname, "r") as log: # Opens the log file for reading
			loglist = log.readlines()
			oldloglist = loglist
			loglist = [line.split(")")[0] for line in loglist] # Seperate into just time & date stamp
			loglist = [line.split(" ")[1] for line in loglist] # Seperate into just time stamp
			loglist = [line.split(":") for line in loglist] # Seperate by hours, minutes, and seconds
			matches = []

			for line in loglist:
				if hour and not minute and not second:  # If hour specified, minute not specified, and second not specified:
					if hour==line[0]: matches.append(oldloglist[loglist.index(line)]) # Append the unedited loglist at the current index
				if hour and minute and not second: # Same style as above
					if hour==line[0] and minute==line[1]: matches.append(oldloglist[loglist.index(line)])
				if hour and not minute and second:
					if hour==line[0] and second==line[2]: matches.append(oldloglist[loglist.index(line)])
				if hour and minute and second: 
					if hour==line[0] and minute==line[1] and second==line[2]: matches.append(oldloglist[loglist.index(line)])
				if not hour and minute and not second: 
					if minute==line[1]: matches.append(oldloglist[loglist.index(line)])
				if not hour and minute and second: 
					if minute==line[1] and second==line[2]: matches.append(oldloglist[loglist.index(line)])
				if not hour and not minute and second: 
					if second==line[2]: matches.append(oldloglist[loglist.index(line)])

			return matches

	def searchDate(self, year=None, month=None, day=None):
		# Searches through the log file and returns a list of lines that have specified date stamp
		# Note: year, month, and day must be strings

		with open(self.fname, "r") as log: # Opens the log file for reading
			loglist = log.readlines()
			oldloglist = loglist
			loglist = [line.split(")")[0] for line in loglist] # Seperate into just time & date stamp
			loglist = [line.split(" ")[0] for line in loglist] # Seperate into just date stamp
			loglist = [line.replace("(", "") for line in loglist] # Get rid of the beginning parenthesis
			loglist = [line.split("-") for line in loglist] # Seperate by year, month, and day
			matches = []

			for x in range(len(loglist)):
				line = loglist[x]

				if year and not month and not day:  # If year specified, month not specified, and day not specified:
					if year==line[0]: matches.append(oldloglist[loglist.index(line)]) # Append the unedited loglist at the current index
				if year and month and not day: # Same style as above
					if year==line[0] and month==line[1]: matches.append(oldloglist[loglist.index(line)])
				if year and not month and day:
					if year==line[0] and day==line[2]: matches.append(oldloglist[x])
				if year and month and day: 
					if year==line[0] and month==line[1] and day==line[2]: matches.append(oldloglist[loglist.index(line)])
				if not year and month and not day: 
					if month==line[1]: matches.append(oldloglist[loglist.index(line)])
				if not year and month and day: 
					if month==line[1] and day==line[2]: matches.append(oldloglist[loglist.index(line)])
				if not year and not month and day: 
					if day==line[2]: matches.append(oldloglist[loglist.index(line)])

			return matches

	def searchTypes(self,format="tuple"):
		# Searches through the log file and returns a dictionary in the format {TYPE: OCCURENCES}

		with open(self.fname, "r") as log: # Opens the log file for reading
			loglist = log.readlines() # Put the log file into array, one line per index
			types, occurences = [], []

			loglist = [line.split("]")[0] for line in loglist] # Seperate into just the type
			loglist = [line.split("[")[1] for line in loglist] # Seperate into just the type

			for line in loglist:
				if not line in types: types.append(line); occurences.append(1) # Add this type to the list if needed
				elif line in types: occurences[types.index(line)]+=1 # Update the corresponding value

			if format == "dict": return dict(zip(types,occurences))
			elif format == "tuple": return (types,occurences)

	def searchSubTypes(self, format="tuple"):
		# Searches through the log file and returns a dictionary in the format {SUBTYPE: OCCURENCES}

		with open(self.fname, "r") as log: # Opens the log file for reading
			loglist = log.readlines() # Put the log file into array, one line per index
			types, occurences = [], []

			loglist = [line.split("}")[0] for line in loglist] # Seperate into just the subtype
			loglist = [line.split("{")[1] for line in loglist] # Seperate into just the subtype

			for line in loglist:
				if not line in types: types.append(line); occurences.append(1) # Add this subtype to the list if needed
				elif line in types: occurences[types.index(line)]+=1 # Update the corresponding value

			if format == "dict": return dict(zip(types,occurences))
			elif format == "tuple": return (types,occurences)


	def clear(self):
		# Completely clears out the log file.
		with open(self.fname, "w"): pass
		print canChart

	def read(self):
		# Returns the contents of the log file as a single string.
		# If you want to get it as an array, use search() with no
		# parameters instead.
		with open(self.fname, "r") as log: return log.read()

	def chart(self, pname="log.png"):
		# If you have pygooglechart, will create a file pname which has a chart of the used types
		# and their number of occurences.
		# If you want it, get it at:

		# pygooglechart.slowchop.com

		try:
			from pygooglechart import PieChart3D
			chart = PieChart3D(300,100)
			typedata = self.searchTypes() # Get the types and corresponding occurences
			typedatadict = self.searchTypes('dict')

			chart.add_data(typedata[1]) # Fill in the occurences
			chart.set_pie_labels([s + "[" + str(typedatadict[s]) + "]" for s in typedata[0]]) # Fill in the labels
			chart.download(pname)
		except:
			return False # You probably don't have pygooglechart


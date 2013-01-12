===========
Easy Log
===========

Easy Log is a Python package intended to make it simple to create and manage a program's log file(s). 

It supports multiple instances of logs, which allows you to use an update multiple log files with different configurations.

Installation
===========
Easy Log can be installed with the following command:

::

	python setup.py install

Usage
===========
You can import the library with the code:

::

	from easylog import *

Then, create an object which will be your 'logger'.

::

	mylog = easylog.EasyLog()

Configuration Options
---------------------
You can set the configuration variables with certain functions:

::

	mylog.setFname("mylog.txt")
	print mylog.fname
	
	mylog.setDefType("WARNING")
	print mylog.defType
	
	mylog.setShowTime(False)
	print mylog.showTime
	
	mylog.setShowType(True)
	print mylog.showType
	
	mylog.setPrintLogs(True)
	print mylog.printLogs
	
	mylog.setVar(fname="mylogV2.txt", showType=True)
	print mylog.fname, mylog.showType
	

It is also possible to give your log object these parameters when you create it:

::

	mylog = easylog.EasyLog(fname="mylog.txt", showTime=False)


To log a message, use the following syntax: ``mylog.log(message, msgType)``
With message being your message (obviously) and msgType being the type, I.E., "WARNING".

Searching
---------
Easy Log also makes it possible to search through your log file for certain things.

There are three different search functions: ``search(text)``, ``searchTime(hour,minute,second)``, and ``searchDate(year,month,day)``.

``search(text)`` will go through every line in the log and return an array of lines which conain ``text``.

``searchTime(hour,minute,second)`` will return an array of lines which contain the given hour/minute/second, if they were
given. To get any of one of the variables, I.E., any second, put ``None``.

``searchDate(year,month,day)`` works just like ``searchTime()``, but returns array of matching dates.

Search Examples
---------------

::

	# Imagine that we have a log.txt file which looks like this:
	#
	# (2013-01-11 21:14:30) [INFO] This is a test.
	# (2013-01-12 11:14:12) [ERROR] This is a second test.
	
	from easylog import *
	mylog = easylog.EasyLog()
	
	mylog.search("test") # Returns array with both lines
	mylog.search("second") # Returns array with only second line
	mylog.searchTime("21") # Returns first line
	mylog.searchTime(None,"14") # Returns both lines
	mylog.searchDate(None,None,"11") # Returns first line
	mylog.searchDate("2013","01") # Returns both lines

Other Functions
---------------

You can easily completely erase your log file by calling ``mylog.clear()``.

You can read the contents of your log file as a single string with ``mylog.read()``.


Variables
===========

Here is a table of the different variables you are able to configure:

=========  ===========  =============================================
  Name      Default                     Description
=========  ===========  =============================================
fname      "log.txt"    The file name to store the logs.
defType    "INFO"       The default message type.
showTime   True         Determines whether to add time stamp to logs.
showType   True         Determines whether to add the type to logs.
printLogs  False        Determines whether to print out log messages.
=========  ===========  =============================================
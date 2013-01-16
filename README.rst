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
	
	mylog.setDefSubType("IOERROR")
	print mylog.defSubType
	
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


To log a message, use the following syntax: ``mylog.log(message, msgType, subType)``
With message being your message (obviously) and msgType being the type, I.E., "WARNING".
Note that specifying msgType and subType is optional and can be ommited. If the fields are
left as empty strings (which is the default if not specifyed), the msgType or subType will
be whatever defType or defSubType is.

Searching
---------
Easy Log also makes it possible to search through your log file for certain things.

There are four different search functions: ``search(text)``, ``searchTime(hour,minute,second)``, ``searchDate(year,month,day)``, and ``searchTypes(format)``.

``search(text)`` will go through every line in the log and return an array of lines which conain ``text``.

``searchTime(hour,minute,second)`` will return an array of lines which contain the given hour/minute/second, if they were
given. To get any of one of the variables, I.E., any second, put ``None``.

``searchDate(year,month,day)`` works just like ``searchTime()``, but returns array of matching dates.

``searchTypes(format)`` returns the message types in the log file and their occurences. Specifying ``format`` is optional.
By default, it is 'tuple' which will return a tuple (types,occurences) with types and occurences both being lists. Alternatively,
you can specify the format as ``'dict'`` to get a dictionary in the form ``{TYPE:OCCURENCES}``.

``searchSubTypes(format)`` is a direct copy of ``searchTypes()``, but will search through the subtypes.

Search Examples
---------------

::

	# Imagine that we have a log.txt file which looks like this:
	#
	# (2013-01-11 21:14:30) [INFO] {GENERAL} This is a test.
	# (2013-01-12 11:14:12) [ERROR] {OTHER} This is a second test.
	
	from easylog import *
	mylog = easylog.EasyLog()
	
	mylog.search("test") # Returns array with both lines
	mylog.search("second") # Returns array with only second line
	mylog.searchTime("21") # Returns first line
	mylog.searchTime(None,"14") # Returns both lines
	mylog.searchDate(None,None,"11") # Returns first line
	mylog.searchDate("2013","01") # Returns both lines
	mylog.searchTypes() # Returns ['INFO','ERROR'],[1,1]
	mylog.searchTypes('dict') # Returns {'INFO':1, 'ERROR':1}
	mylog.searchSubTypes() # Returns ['GENERAL','OTHER'],[1,1]

Other Functions
---------------

You can easily completely erase your log file by calling ``mylog.clear()``.

You can read the contents of your log file as a single string with ``mylog.read()``.

You can generate a chart of the different message types in your log file with chart(pname) with
pname being the name of the generated picture file (if not specified, will use log.png).
NOTE: Generating charts requires [pygooglechart](http://pygooglechart.slowchop.com/ "pygooglechart")


Variables
===========

Here is a table of the different variables you are able to configure:

=============  ===========  =============================================
 Name           Default                     Description
=============  ===========  =============================================
fname          "log.txt"    The file name to store the logs.
defType        "INFO"       The default message type.
defSubType     "GENERAL"    The default message subtype.
showTime       True         Determines whether to add time stamp to logs.
showType       True         Determines whether to add the type to logs.
printLogs      False        Determines whether to print out log messages.
=============  ===========  =============================================
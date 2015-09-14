STAGES = [
	{'title': 'Stage 1: Webpages, Documents, and Structure',
		'lessons': [
			{'title': 'Lesson 1.1: Introduction to HTML',
			'concepts': [
				{'title': 'Workings of the Web',
				'description': 'The web connects computers togehter when a computer '
							   'sends a HTTP Request to a server. The servers grabs the '
							   'correct HTML document and displays it in a web browser.'},
				{'title': 'HTML',
				'description': 'HTML stands for <em>Hypertext Markup Language.</em> '
							   'Text content describes what you see. Markup describes how it looks. '
							   'HTML consists of elements designated by tags. '
							   'Elements can be either inline or block (with a box).'},
				{'title': 'Why Computers Are Stupid',
				'description': 'Computers interpret instructions literally so small mistakes '
							   'make them go crazy.'}
				]
			},
			{'title': 'Lesson 1.2: Creating a Structured Document with HTML',
			'concepts': [
				{'title': 'The Structure of HTML',
				'description': 'HTML uses a tree-like structure (elements can be nested inside each other).'},
				{'title': 'Indentation',
				'description': 'HTML documents use indentation to help visualize the tree structure.'}
				]
			},
			{'title': 'Lesson 1.3: Adding CSS Style to HTML',
			'concepts': [
				{'title': 'Repitition',
				'description': 'Avoiding repetition allows us to avoid errors (by not needing to make '
							   'the same change multiple times) and allows for consistency.'},
				{'title': 'CSS',
				'description': 'CSS stands for Cascading Style Sheets. It allows us to define the style '
							   'of HTML elements by assigning them to classes.'}
				]
			}
		]
	},

	{'title': 'Stage 2: Introduction to Computer Science',
		'lessons': [
			{'title': 'Lesson 2.1: Introduction to Serious Programming',
			'concepts': [
				{'title': 'Programming Languages',
				'description': 'Programming languages are how people tell computers what to do. '
							   'Examples: Python, C, Java, Scheme'},
				{'title': 'Grammar',
				'description': 'Grammar is very important in computer programming. People can understand '
							   'natural language sentences with bad grammar, but computers can not.'}
				]
			},
			{'title': 'Lesson 2.2: Variables and Strings',
			'concepts': [
				{'title': 'Variables',
				'description': 'Variables give names to values. They make managing data easier.'},
				{'title': 'Strings',
				'description': 'Strings are designated by putting characters in between single or double '
							   'quotes (or triple quotes for multi-line strings). '
							   'We can get part of a string using indexing.'}
				]
			},
			{'title': 'Lesson 2.3: Input->Function->Output',
			'concepts': [
				{'title': 'Functions (Procedures)',
				'description': 'Functions take something (value, string, etc.) as input, do something '
							   '(maybe) and produce an output (if we define it to do so).'}
				]
			},
			{'title': 'Lesson 2.4: Control Flow and Loops',
			'concepts': [
				{'title': 'If Statements',
				'description': 'If statements allow our programs to make decisions. It evaluates an '
							   'expression and executes a block of code if that expression evaluates '
							   'to true. We can add an else statement to execute different code if '
							   'the expression is false.'},
				{'title': 'While Loops',
				'description': 'While loops execute a block of code repeatedly while a defined expression '
							   'is true. If the expression ever evaluates to false, then the loop stops. '
							   'We can terminate a loop early using the keyword break.'}
				]
			},
			{'title': 'Lesson 2.5: Debugging',
			'concepts': [
				{'title': 'Strategies for Debugging',
				'description': '1) Examine Error Messages <br>'
            				   '2) Work from a Working Example <br>'
            				   '3) Make Sure Examples Work! <br>'
            				   '4) Check Intermediate Results <br>'
            				   '5) Keep and Compare Old Versions'}
				]
			},
			{'title': 'Lesson 2.6: Structured Data',
			'concepts': [
				{'title': 'Lists',
				'description': 'Lists are a kind of data structure. In Python, lists can contain many '
							   'different data types (such as strings and integers). Operations on '
							   'lists include append, +, and len. Lists can be mutated (we can '
							   	'change individual elements) and are aliased (setting something '
							   	'equal to a list makes a pointer to the list).'},
				{'title': 'For Loops',
				'description': 'For loops are similar to while loops but instead of looping until an '
							   'expression becomes false, we loop through a list or range of values.'}
				]
			},
			{'title': 'Lesson 2.7: How to Solve Problems',
			'concepts': [
				{'title': "Pythonista's Guide to All Problems in the Galaxy",
				'description': "0) Don't panic! <br>"
				               "1) What are the inputs? <br>"
				               "2) What are the outputs? <br>"
				               "3) Work through some examples by hand <br>"
				               "4) Simple mechanical solution <br>"
				               "5) Develop incrementally as you go"}
				]
			}
		]
	},

	{'title': 'Stage 3: Abstraction',
		'lessons': [
			{'title': 'Lesson 3.1: Introduction to Abstraction',
			'concepts': [
				{'title': 'Classes and Object Oriented Programming',
				'description': 'Object oriented programming is one way we can use abstraction to '
							   'minimize repitition in our code. In Python, we usually do this by '
							   'defining classes and creating instances of those classes.'}
				]
			},
			{'title': 'Lesson 3.2: Use Functions',
			'concepts': [
				{'title': 'Modules and the Python Standard Library',
				'description': 'The Python Standard Library comes with many modules that contain '
							   'definitions of functions we can use in our code. In order to use '
							   'these functions we have to import the modules at the start of our '
							   'code. For example, "import os" imports the os module to allow us '
							   'to use functions such as rename. Some functions, such as open '
							   'do not need a module to be imported. We can even install additional '
							   'libraries, like twilio, to do all kinds of crazy stuff.'}
				]
			},
			{'title': 'Lesson 3.3: Using and Making Classes',
			'concepts': [
				{'title': 'Creating Instances of Classes',
				'description': 'Turtle is an example of a class. It is included in the module turtle '
							   'and we can create instances of the class in order to make simple '
							   'computer graphics.'},
				{'title': 'Importing Classes from Modules',
				'description': 'Once we install additional modules to Python, we can import them '
							   'and use functions and classes defined by them. We can use the Python '
							   'keyword from to import specific classes from a module.'},
				{'title': 'Defining Classes',
				'description': 'When writing Python code, it is standard to include all class definitions '
							   'in a separate file from the rest of your code. It is also standard to '
							   'capitalize the names of all classes. We define a class using the Python '
							   'keyword class.'},
				{'title': 'Inheritance',
				'description': 'Inheritance lets us make classes that inherit attributes from other '
							   'classes. For example we can define a class Child that inherits '
							   'attributes last_name and eye_color from a class Parent. This allows '
							   'us to reuse code and thus further decrease repitition!'}
				]
			}
		]
	},

	{'title': 'Stage 4: Web Applications',
		'lessons': [
			{'title': 'Lesson 4.1: Introduction to Networks',
			'concepts': [
				{'title': 'Networks',
				'description': 'A <em>network</em> is a group where all members can communicate '
							   'even if not all members are directly connected.'},
				{'title': 'Latency vs Bandwidth',
				'description': '<em>Latency</em> is the time a message takes to get from source '
							   'to destination. It is typically measured in milliseconds.<br>'
							   '<em>Bandwidth</em> is the amount of information that can be '
							   'transmitted per unit time. It is typically measured in '
							   'bits per second (Mbps = million bits per second)'}
				]
			},
			{'title': 'Lesson 4.2: Make the Internet Work for You',
			'concepts': [
				{'title': 'URLs',
				'description': 'URL stands for <em>Uniform Resource Locator</em>. A URL always '
							   'consists of a protocol (usually HTTP), a host, and a path. '
							   'They may also contain query parameters which are of the form ?NAME=VALUE '
							   'and fragments of the form #FRAGMENT which are not sent to the server.'},
				{'title': 'HTTP Requests',
				'description': 'HTTP requests are how we retrieve documents from a server. '
							   'The request line consist of a method (either GET or POST), a path, '
							   'and a version. The server then sends an HTTP response '
							   'which includes a status code (like 404).'}
				]
			},
			{'title': 'Lesson 4.3: Forms',
			'concepts': [
				{'title': 'User Input',
				'description': 'HTML forms allow us to get input from users. HTML forms can be '
							   'text fields, buttons, checkboxes, radio boxes, password fields, and more!'}
				]
			},
			{'title': 'Lesson 4.4: Modulus & Dictionaries',
			'concepts': [
				{'title': 'The Modulus Operator',
				'description': 'The modulus operator is a useful arithmetic operator that performs '
							   'modular arithmetic between two expressions. This more or less means it '
							   'takes the remainder from dividing the two expressions.'},
				{'title': 'Dictionaries',
				'description': 'Python dictionaries establish mutable key-value pairs. We can then '
							   'look up values in the dictionary via their keys. Note that dictionaries '
							   'are not printed in the same order as we define them due to hashing.'}
				]
			},
			{'title': 'Lesson 4.5: Working with Google App Engine',
			'concepts': [
				{'title': 'Google App Engine',
				'description': 'Google App Engine is a tool we can use to host our websites publicly. '
							   'It makes heavy use of classes and OOP.'}
				]
			},
			{'title': 'Lesson 4.6: Validation',
			'concepts': [
				{'title': 'Checking User Inputs',
				'description': 'Validation is very important for a number of reasons. Firstly, '
							   'it improves the user experience by alerting users when they input something '
							   'invalid or unexpected. Secondly, it protects our website from '
							   'bad data and hacks. An example of this would be if a user submitted HTML '
							   'to a form, which could be wrongly interpreted if it is not escaped.'}
				]
			},
			{'title': 'Lesson 4.7: HTML Templates',
			'concepts': [
				{'title': 'Template Libraries',
				'description': 'Using a template library helps us to automate the building of '
							   'long HTML documents. This really helps us cut out repitition!'},
				{'title': 'Variable Substitution',
				'description': 'Tools like jinja2 (built into GAE) allow us to include variables '
							   'and code in our HTML templates. That way we can iterate through '
							   'lists or access dictionaries of content, among other things.'}
				]
			},
			{'title': 'Lesson 4.8: Databases',
			'concepts': [
				{'title': 'What is a Database?',
				'description': 'A database is a program that allows us to store and retrieve '
							   'large amounts of structured data. The word database can refer to '
							   'the program managing the data or the machine(s) that are '
							   'running the program.'},
				{'title': 'Types of Databases',
				'description': 'Types of databases include relational (SQL), GAE Datastore, '
							   'Amazon Dynamo, and NoSQL. As with everything in computer '
							   'science, there are tradeoffs for each.'},
				{'title': 'Database Lookup',
				'description': 'We can access the information in a database using a database '
							   'query. This can be done in a language like SQL. We can also '
							   'index our data using unique identifiers to increase lookup speed'}
				]
			}
		]
	},

	{'title': 'Stage 5: Where It Goes From Here',
		'lessons': []
	}
]

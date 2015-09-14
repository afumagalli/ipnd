def get_title(concept):
	start = concept.find('TITLE:')
	finish = concept.find('DESCRIPTION:')
	title = concept[start+7:finish-1]
	return title

def get_description(concept):
	start = concept.find('DESCRIPTION:')
	description = concept[start+13:]
	return description

def get_concept_by_number(text, concept_number):
	counter = 0
	while counter < concept_number:
		counter += 1
		start = text.find('TITLE:')
		finish = text.find('TITLE', start+1)
		concept = text[start:finish]
		text = text[finish:]
	return concept

def generate_concept(title, desc):
	html = '''
<div class="concept">

	<div class="concept-title">
		''' + title + '''
	</div>

	<div class="concept-description">
		<p>
			''' + desc + '''
		</p>
	</div>
</div>'''

	return html

def generate_all_concepts(text):
	current = 1
	concept = get_concept_by_number(text, current)
	all_html = ''
	while concept != '':
		title = get_title(concept)
		desc = get_description(concept)
		con_html = generate_concept(title, desc)
		all_html = all_html + con_html
		current += 1
		concept = get_concept_by_number(text, current)
	return all_html

print generate_concept("Python", "Programming")
print get_concept_by_number("", 1)

def make_html(concept):
	title = concept[0]
	desc = concept[1]
	return generate_concept(title, desc)

def make_html_for_many_concepts(list_of_concepts):
	html = ''
	for c in list_of_concepts:
		html = html + make_html(c)
	return html


TEST_TEXT = """TITLE: Why Computers are Stupid
DESCRIPTION: The phrase "computers are stupid" refers
to how they interpret instructions literally. This
means that small typos can cause big problems.
TITLE: Python
DESCRIPTION: Python is a "programming language." It
provides programmers a way to write instructions for a
computer to execute in a way that the computer can understand.
TITLE: While Loops
DESCRIPTION: A while loop repeatedly executes the body of
the loop until the "test condition" is no longer true."""

print generate_all_concepts(TEST_TEXT)


EXAMPLE_LIST_OF_CONCEPTS = [ ['Python', 'Python is a Programming Language'],
                             ['For Loop', 'For Loops allow you to iterate over lists'],
                             ['Lists', 'Lists are sequences of data'] ]

print make_html_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)

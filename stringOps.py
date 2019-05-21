# replace character with '#' if char within range of r (examples: 'a-d', 'h-q', 'f-n')

def replace(txt, r):
	low, high = r.split('-')
	return ''.join(['#' if low <= i <= high else i for i in txt])

# move all instances of el to the end of lst

def move_to_end(lst, el):
	return [i for i in lst if i != el] + [el] * lst.count(el)
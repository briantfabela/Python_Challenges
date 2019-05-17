# return the reverse case of a string

def reverse_case(txt):
	return "".join(map(lambda i: i.lower() if i.isupper() else i.upper(), txt))

# check that all chars in a string are of equal case

def same_case(txt):
	if txt[0].isupper():
		return len(txt) == sum(1 for i in txt if i.isupper()) # txt.isupper()
	else:
		return len(txt) == sum(1 for i in txt if i.islower()) # txt.islower()

def main():
    print(reverse_case("hAPPY bIRTHDAY!"))
    print('Jonny', same_case('Jonny'))
    print('jonny', same_case('jonny'))

if __name__ == "__main__":
    main()
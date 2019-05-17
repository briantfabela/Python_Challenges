# checks for perfect numbers
def check_perfect(num):
    # if odd return False, else check if sum of factorials == num
	return False if num%2==1 else sum([i for i in range(1, num) if num%i==0]) == num

# check if number is palindrome
def is_palindrome(n):
	if len(str(n)) < 2 or str(n)[0] is str(n)[1]:
		return True
	else:
		return is_palindrome(int(str(n)[1:-1])) if str(n)[0] is str(n)[-1] else False

# check that all numbers in a list are even
def check_all_even(lst):
  return False if [n for n in lst if n%2 != 0] else True

# check that a string is of length 5 and made only of digits
def is_valid(zip_code):
	return True if len(zip_code) == 5 and zip_code.isdigit() else False 
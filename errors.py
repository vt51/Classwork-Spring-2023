# a = "The sky is blue"
# print(a)

# for letter in a:
# 	print(letter)

# def calc_square_root(n):
# 	# creates an error
# 	try: 
# 		from my_calculator import calc_square_root
# 	except ModuleNotFoundError:
# 		from math import sqrt

# 	answer = sqrt(n)
# 	return answer

def my_function(alphabet):
	try:
		return letters
	except NameError:
		print("error -- name not defined")
		return alphabet


def main():
	# print(calc_square_root(2))
	print(my_function("a"))


if __name__ == '__main__':
	main()
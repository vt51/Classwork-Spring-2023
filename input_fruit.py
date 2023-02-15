# in_file = open("input_data.txt", "r")
# fruits = in_file.readlines()
# print(fruits)
# in_file.close()
# print(fruits)


# in_file = open("input_data.txt", "r")
# # for line in in_file:
# # 	print(line)

# first_fruit = in_file.readline()
# second_fruit = in_file.readline()

def analyze_ID(input_line):
	patient_data = input_line.strip("\n").split("=")
	patient_id = int(patient_data[1])
	return patient_id


def read_file(filename):
	in_file = open(filename, "r")
	first_line = in_file.readline()
	ID = analyze_ID(first_line)


def test_read_file():
	from module import read_file
	filename = "my_test_data.txt"
	answer = read_file(filename)
	expected = 50
	assert == expected
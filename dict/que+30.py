#Write a Python program to get the top three items in a shop
def highest_3_values_1(my_dict):
	result_dict = {}
	sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
	for i in range(3):
		result_dict[sorted_dict[i][0]] = sorted_dict[i][1]
	return result_dict

my_dict = {'A': 67, 'B': 23, 'C': 45, 'D': 56, 'E': 12, 'F': 69}
print(highest_3_values_1(my_dict))
doubt
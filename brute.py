from itertools import product


def get_passwords(pass_file):
    pass_obj = open(pass_file, 'r')
    pass_list = []

    for word in pass_obj.readlines():
    	word      = word.strip('\n')
        pass_list.append(word)
    return pass_list

def generate_any_chars(iter_len):
    #this can be extended to non-number characters, but will not make numbers
    #with fewer places - e.g if iter_len is 3 you can create 001 but not 1
    chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    char_combs = [''.join(i) for i in product(chars, repeat = iter_len)]
    return char_combs

def generate_all_numbers(iter_to):

    number = 0
    number_list = []

    while number <= iter_to:
        number_list.append(number)
        number += 1

    return number_list

def append_any_chars(password_list, iter_len):

	pass_plus = []
	char_list = generate_any_chars(iter_len)
	#tries all passwords without numbers with all combinations of numbers
	#within the character length specified in iter_len
	for chars in char_list:
		for password in password_list:
			pass_plus.append(password + chars)
	return pass_plus

    
def main():
    
    passwords = get_passwords('../password-dictionaries/dictionaries/combined')
    
    pass_chars = append_any_chars(passwords, 2)
    pass_all = passwords + pass_chars
    print generate_all_numbers(999)
    return pass_all

if __name__ == "__main__":
    main()

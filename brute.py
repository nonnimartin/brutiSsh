from itertools import product


def get_passwords(pass_file):
    pass_obj = open(pass_file, 'r')
    pass_list = []

    for word in pass_obj.readlines():
        word      = word.strip('\n')
        pass_list.append(word)
    return pass_list

def generate_chars(iter_len):

    char       =  0
    char_combs = []

    while len(str(char)) <= iter_len:
       char_combs.append(str(char))
       char += 1 
    return char_combs

def append_chars(password_list, iter_len):

    pass_plus = []

    for password in password_list:
        pass_plus.append(password)

    char_list = generate_chars(iter_len)
    #tries all passwords without numbers with all combinations of numbers
    #within the character length specified in iter_len
    for chars in char_list:
        for password in password_list:
            pass_plus.append(password + chars)
    return pass_plus
    
def main():
    
    passwords = get_passwords('../password-dictionaries/dictionaries/combined')
    pass_chars = append_chars(passwords, 2)
    
    return pass_chars

if __name__ == "__main__":
    main()

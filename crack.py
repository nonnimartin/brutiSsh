import crypt
import hashlib
from passlib.hash import sha512_crypt

# def crackShadow(line):
    # /etc/shadow password alg can be determined
    # by the following prefixes following the unsername : 
    # 
    # $1$
    # md5
    # $2a$
    # Blowfish
    # $2y$
    # Blowfish, with correct handling of 8 bit characters
    # $5$
    # sha256
    # $6$
    # sha512

def testShadowPassword(password, alg):
    #check unix password against word list in file
    #confirmed cracks ubuntu
    salt      = password[0:2]
    #test file
    pass_obj = open('../password-dictionaries/dictionaries/combined', 'r')
    
    if alg == "unix":
        for word in pass_obj.readlines():
            word      = word.strip('\n')
            encrypted = crypt.crypt(word, salt)

            if encrypted == password:
                print "Found password: " + word
                return
        print "Password not found"
    elif alg == "sha512":
        if len(password.split("$")) > 1:

            if password.split("$")[1] == str(6):
                for word in pass_obj.readlines():

                    word      = word.strip('\n')
                    pass_hash_split = password.split("$")
                    shad_salt       = pass_hash_split[2]
                    shad_pass       = pass_hash_split[3]

                    sha512_word     = sha512_crypt.encrypt(word, salt=shad_salt, rounds=5000)

                    if sha512_word == password:
                        print "Found Password: " + word
                        return

            print "Password not found"


def getShadowPass(shadow, user):
    lines = open(shadow).readlines()
    
    for line in lines:
        line   = line.split(":")
        shad_user   = line[0]
        
        if user == shad_user:
            shad_pass   = line[1].split("$6$")[1]
            return shad_pass



def main():
    #test file
    pass_list = open('examples/Chapter-1/passwords5.txt')
    for line in pass_list.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            testShadowPassword(cryptPass, "sha512")

if __name__ == "__main__":
    main()

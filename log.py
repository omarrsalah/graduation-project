# Python program to check validation of password
# Module of regular expression is used with search()
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def check1(email,password):
    if(re.fullmatch(regex, email)):
        print("Valid Email")
    else:
        print("invalid email")
#         else:
# 		print("Invalid Email")
    flag = 0
    while True:
	    if (len(password)<8):
		    flag = -1
		    break
	    elif not re.search("[a-z]", password):
		    flag = -2
		    break
	    elif not re.search("[A-Z]", password):
		    flag = -3
		    break
	    elif not re.search("[0-9]", password):
		    flag = -4
		    break
#         elif not re.search("[_@$]", password):
# 		    flag = -5
# 		    break
# 	elif re.search("\s", password):
# 		flag = -6
# 		break
	    else:
		    flag = 0
		    print("Valid Password")
		    break

    if flag ==-1:
	    print("should enter 8 characters")
    
    if flag ==-2:
        print("should enter small letter")
    
    if flag ==-3:
        print("should enter capital letter")

    if flag ==-4:
        print("should enter number")
    
    # if flag ==-5:
    #     print("should enter symbols")
    
    
if __name__ == '__main__':
    password = "Lm@_f0rtu9e$"
    email = "jggfj"
    check1(email,password)
    
    
# if flag ==-6:
# 	print("should enter ")
    

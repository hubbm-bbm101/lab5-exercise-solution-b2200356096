mail = input("Email:")


def check(mail):

    a = 0
    b = 0
    for ab in mail:
        if (ab == '@'):
            a += 1
        if (ab == '.'):
            b += 1
    if (a == 1 and b >= 1):
        return True
    else:
        return False

if (check(mail) == True):
    print("that is an email")
if (check(mail) == False):
    print("that is not an email")





class AgeException(Exception):
    pass

class AgeTooHighException(AgeException):
    pass

class AgeTooLowException(AgeException):
    pass

def getAge(prompt)->int:
    while True:
        try:
            age = int(input(prompt))
            if (age<1):
                raise AgeTooLowException()
            if (age>128):
                raise AgeTooHighException()
        except ValueError as ex:
            print('Invalid age entry')
        except AgeTooLowException as ex:
            print('Age too low')
        except AgeException:
            print('Age Exception')
        except: #Last line of defence
            print('Unknow error!')
        else:
            print('Else block')
            break
        finally:
            print('Finally block')
    return age

age = getAge('Enter your age>>')

print("Your age is {}".format(age))


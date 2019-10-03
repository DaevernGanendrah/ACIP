import ManageDepartmentModule
import MyExceptionModule

def RunCompany():
    print('In the RunCompany function')
    try:
        ManageDepartmentModule.ManageDepartment()
    except MyExceptionModule.ProgrammerDie:
        print('The boss arrange a press conference')


RunCompany()


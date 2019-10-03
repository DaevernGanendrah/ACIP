import DoProjectModule
import MyExceptionModule


def ManageDepartment():
    print('In the ManageDepartment function')
    try:
        DoProjectModule.DoProject()
    except MyExceptionModule.ProgrammerResign:
        print('Department settle the payroll')
    except MyExceptionModule.ProgrammerDie:
        print('settle the all for the programmer who die')
        raise

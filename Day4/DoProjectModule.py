from MyExceptionModule import *

def DoProject():
    print('In the DoProject function')
    try:
        'During project execution, there might be different abnormal situation occur'
        raise ProgrammerDie()
    except ProgrammerAugue as ex:
        print('Project Manager settle this....')
    except ProgrammerResign:
        print('Project Manager assign the task to another programmer')
        raise
    except ProgrammerDie:
        print('Project Manager assign the task to another programmer')
        raise




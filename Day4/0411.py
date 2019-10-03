#Debugging Example #2

def opX():
    print('opX()----1')
    print('opX()----2')
    opY()
    print('opX()----3')
    print('opX()----4')


def opY():
    print('opY()----1')
    print('opY()----2')
    print('opY()----3')
    opZ()
    print('opY()----4')


def opZ():
    print('opZ()----1')
    print('opZ()----2')
    print('opZ()----3')
    print('opZ()----4')

opX()




#Default Argument Values

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'): return True
        if ok in ('n', 'no', 'nop', 'nope'): return False
        retries = retries - 1
        if retries < 0: raise ValueError('invalid user response')
        print(reminder)

#ask_ok("What is your answer?")
#ask_ok("What is your answer?",2)
#ask_ok("What is your answer?",3,"Cuba Lagi!")
#ask_ok("What is your answer?",reminder="Cuba Lagi!")
ask_ok("What  your answiser?",reminder="Cuba Lagi!",retries=2)

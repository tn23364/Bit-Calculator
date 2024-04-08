# generates headings (eg: ---- Heading ----)

def statement_generator(statement, decoration):
    print(f'\n{decoration * 5} {statement} {decoration * 5}')

# displays instructions
def instructions():
    statement_generator("instructions", "-")

    print('''
Instructions go here.
- instruction 1
- instruction 2 
- etc
    ''')

# main routine goes here

# display instructions if requested
want_instructions = input('Press <enter> to read the instructions '
                          'or any key to continue ')

if want_instructions == "":
    instructions()

print('program continues')
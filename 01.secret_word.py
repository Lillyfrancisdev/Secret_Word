# Secret_Word

secret_Word = ('B', 'E', 'A', 'U', 'T', 'I','F','U','L') 
discovered_letters = []

print ( '\n *** SECRET WORD *** \n' )

print ( 'Clue: Color' )

for i in range ( 0, len ( secret_Word ) ):
    discovered_letters.append ( '-' )

hit = False

while not hit:
    letter = str(input ( 'type the letter:' ) )

    for i in range ( 0, len ( secret_Word ) ):
        if letter == secret_Word[i]:
            discovered_letters[i] = letter
        print ( discovered_letters[i] )

    hit = True

    for x in range ( 0, len ( discovered_letters ) ):
        if discovered_letters[x] == '-':
            hit = False
print ( 'Congratulations,You Won!' )
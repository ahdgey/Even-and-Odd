#Alexza Jean R. Catanoy
#BSCPE 1-4
#Even and Odd

#Title
print("\033[0;36m*" * 70)
print("\033[1;97mA Program that Reads Text File".center(77))
print("\033[0;36m*" * 70)

print("\033[1;32m\nHello! Your programmers name is Alexza Jean.")
print("\033[1;32m\nShe's from BSCPE 1-4.")
print("-" * 70)

#Open numbers.txt (read), even.txt (append), odd.text (append)
with open("Numbers.txt") as input_data, open("Even.txt", "a") as output_even, open("Odd.txt", "a") as output_odd:

    #From the first line up to the end, read numbers.txt 
    for line in input_data:
        input_data = int(line)

        #If the number is even
        if input_data % 2 == 0:
        
            #Calculate for its square
            square = input_data + input_data
        
            #Type it to Even.txt
            output_even.write(str(square) + "\n")

        #If the number is odd
        else:

            #Calculate for its cube
            cube = input_data + input_data + input_data

            #Type it to Odd.txt
            output_odd.write(str(cube) + "\n")
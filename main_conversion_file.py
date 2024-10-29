
#Name of the function
def main():
    print("Welcome to JSON to SQL exporter!")
    print("""
Press 1 to continue
Press 2 to see the credits
Press q to quit
          """)
    inputmain = input()         #User input
    if inputmain == str(1):     #Go to the main file
        import databaseconnect
        databaseconnect.dataconnect()
    elif inputmain == str(2):   #See the credits
        print("This program was created by Filip Vašíček as his side project for the main project of his league of legends analysis.")
        print("Press enter to continue.\n")
        inputcredit = input()

        if inputcredit == "":
            main()
        else:
            print("I've said enter!\n")
            main()

    elif inputmain == "q":      #Quit the program
        exit() 
    else: 
        print("Can't read the input!\n")
        main()
#call the function
main()

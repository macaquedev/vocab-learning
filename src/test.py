def input_validate():
    while True:
        inp = input()
        try:
            inp = int(inp)
            return inp
        except:
            print("Invalid input. Please enter an integer.")


input_validate()
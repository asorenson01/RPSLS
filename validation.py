class Validation:
    def input_number(self, message):
        while True:
            try:
                user_input = int(input(message))
            except ValueError:
                print("That is not a Number, Please Try again.")
                continue
            else:
                return user_input
                break

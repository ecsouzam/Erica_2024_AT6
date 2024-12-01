class UserInputValidator:

    def validate_positive_integers(self, inputs):

        valid_integers = []
        for item in inputs:
            if item.isdigit() and int(item) > 0:
                valid_integers.append(int(item))
        return valid_integers

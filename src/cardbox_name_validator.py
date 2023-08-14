from PyInquirer import Validator, ValidationError
from string import ascii_letters


class CardboxNameValidator(Validator):
    def validate(self, document):
        try:
            assert all([i == i.title() and j in ascii_letters for i in document.text.split() for j in i])
        except AssertionError:
            raise ValidationError(
                message='Please enter a valid cardbox name',
                cursor_position=len(document.text))

import re

from django.core.exceptions import ValidationError


def validate_number_car(value):
    result = re.search('^[A-Z]\d\d\d[A-Z][A-Z](\d\d|\d\d\d)', value)

    if not result:
        raise ValidationError('Номер машины введён в неправильном формате')

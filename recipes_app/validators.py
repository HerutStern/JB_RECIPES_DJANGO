from rest_framework.exceptions import ValidationError


def validate_level(value):
    if value not in ['easy', 'medium', 'hard']:
        raise ValidationError(f'{value} id not a valid level')
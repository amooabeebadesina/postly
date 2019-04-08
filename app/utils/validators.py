from schema import Schema, And

def validate_create_user(data):
    data_schema = {
        'first_name': And(str, lambda s: len(s) > 3),
        'last_name': And(str, lambda s: len(s) > 3),
        'email': lambda s: len(s) > 3,
        'password': lambda s: len(s) > 6
    }
    return Schema(data_schema).is_valid(data)
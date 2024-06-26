def hello_decorator(func):
    def wrapper(*args, **kwargs):
        print("hello world")
        return func(*args, **kwargs)

    return wrapper


def is_admin(user):
    return user.is_staff

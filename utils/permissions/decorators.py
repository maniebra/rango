import telepot

from . import classes
def permission_class(class_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            bot: telepot.Bot = args[0]
            chat_id = args[1]
            permission = classes.__classnames__[class_name](chat_id)
            if permission.has_permission():
                return func(*args, **kwargs)
            else:
                return "UNAUTHORIZED!"

        return wrapper
    return decorator
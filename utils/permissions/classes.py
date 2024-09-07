from models import User

class BasePermission:
    def __init__(self, chat_id):
        self.user = User.get_or_none(User.tg_id == chat_id)

    def has_permission(self):
        return True

class AdminPermission(BasePermission):
    def has_permission(self):
        return self.user.is_admin

class StaffPermission(BasePermission):
    def has_permission(self):
        return self.user.is_staff

class ActivePermission(BasePermission):
    def has_permission(self):
        return self.user.is_active

__classnames__ = {
    "base": BasePermission,
    "admin": AdminPermission,
    "staff": StaffPermission,
    "active": ActivePermission
}
from ..models.user import Users


class UserRepository():
    @staticmethod
    async def get_all_users() -> Users:
        all_users = []
        return all_users

MOCK_USERS = {'334086023@qq.com': '123456'}


class MockDBHelper:

    def get_user(self, email):
        if email in MOCK_USERS:
            return MOCK_USERS[email]
        return None

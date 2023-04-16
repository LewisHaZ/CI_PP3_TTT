import unittest
import validation as val


class TestValidate(unittest.TestCase):
    """
    A test case of the user email and user
    name inputs/types
    """
    def test_validate_email(self):
        self.assertTrue(val.validate_user_input('test-email@gmail.com'), True)

    def test_incorrect_email(self):
        self.assertEqual(val.validate_user_input('999999'), None)
    
    def test_validate_username(self):
        self.assertTrue(val.validate_username('Lewis'), True)

    def test_validate_incorrect_username(self):
        self.assertEqual(val.validate_username('A2'), None)
        self.assertEqual(val.validate_username('TooLongOfANameForGame'), None)
        self.assertEqual(val.validate_username(666), False)


class TestUserSignUpAndLogIn(unittest.TestCase):
    """
    A test case of the input for sign up
    and log ins
    """
    def test_log_in(self):
        self.assertTrue(val.existing_acc(['User1', 'User2']), True)
        self.assertEqual(val.existing_acc(123), None)

    def test_sign_up_players(self):
        self.assertTrue(val.register_new_players(['User1', 'User2']), True)
        self.assertEqual(val.register_new_players(123), None)


if __name__ == '__main__':
    unittest.main()

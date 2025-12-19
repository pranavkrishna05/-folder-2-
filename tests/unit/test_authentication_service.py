import unittest
from services.authentication import AuthenticationService

class TestAuthenticationService(unittest.TestCase):
    def test_authenticate_success(self):
        result = AuthenticationService.authenticate('username', 'password')
        self.assertTrue(result)

    def test_authenticate_failure(self):
        result = AuthenticationService.authenticate('username', 'wrongpassword')
        self.assertFalse(result)

if __name__':
    unittest.main()

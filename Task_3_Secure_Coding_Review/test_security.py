import unittest
from secure_login import hash_password, verify_password

class SecurityTests(unittest.TestCase):
    def test_correct_password(self):
        salt, digest = hash_password('sample-strong-password')
        self.assertTrue(verify_password('sample-strong-password', salt, digest))
    def test_wrong_password(self):
        salt, digest = hash_password('sample-strong-password')
        self.assertFalse(verify_password('wrong-password', salt, digest))
    def test_random_salts(self):
        self.assertNotEqual(hash_password('same-password')[0], hash_password('same-password')[0])

if __name__ == '__main__':
    unittest.main()

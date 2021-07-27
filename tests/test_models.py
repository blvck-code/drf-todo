from rest_framework.test import APITestCase
from authentication.models import User

class TestModel(APITestCase):

    def test_creates_user(self):
        user = User.objects.create_user('maurice', 'maurice@demo.com', 'password@123')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'maurice@demo.com')

    def test_creates_super_user(self):
        user = User.objects.create_superuser('maurice', 'maurice@demo.com', 'password@123')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'maurice@demo.com')

    def test_raises_error_when_no_username_supplied(self):
        # Procedure 1

        """self.assertRaises(
            ValueError,
            User.objects.create_superuser,
            username='', email='maurice@demo.com', password='password@123'
        )
        self.assertRaisesMessage(ValueError, 'The given username must be set')
        """

        # Procedure 2
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_superuser(username='', email='maurice@demo.com', password='password@123')


    def test_raises_error_when_no_email_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given email must be set'):
            User.objects.create_superuser(username='oluoch', email='', password='password@123')


    def test_creates_super_user_with_is_staff_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(username='oluoch', email='maurice@demo.com', password='password@123', is_staff=False)

    def test_creates_super_user_with_super_user_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(username='oluoch', email='maurice@demo.com', password='password@123', is_superuser=False)



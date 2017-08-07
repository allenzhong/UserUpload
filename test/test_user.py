import unittest
from processors.user import User

class TestUser(unittest.TestCase):

  def test_create_user(self):
    name = 'John'
    surname = 'Allen'
    email = "johnallen@email.com"
    user = User(name, surname, email)
    self.assertEqual(name, user.name)
    self.assertEqual(surname, user.surname)
    self.assertEqual(email, user.email)

  def test_capitalize_name(self):
    name1 = 'john'
    surname = 'Allen'
    email = "johnallen@email.com"
    user = User(name1, surname, email)
    self.assertEqual(user.capitalize_name(name1), 'John')
    name2 = "O'connor"
    self.assertEqual(user.capitalize_name(name2), "O'Connor")
    name3 = 'Allen'
    self.assertEqual(user.capitalize_name(name3), "Allen")

  def test_downcase_email(self):
    name = 'john'
    surname = 'Allen'
    email1 = "Johnallen@email.com"
    user = User(name, surname, email1)
    self.assertEqual(user.downcase_email(email1), 'johnallen@email.com')
    email2 = "JOHNALLEN@EMAIL.COM"
    self.assertEqual(user.downcase_email(email2), 'johnallen@email.com')

    email3 = "John.alLEN123@EMAIL.COM"
    self.assertEqual(user.downcase_email(email3), 'john.allen123@email.com')

  def test_verify_email(self):
    name = 'john'
    surname = 'Allen'
    email1 = "johnallen@email.com"
    user = User(name, surname, email1)
    self.assertEqual(user.verify_email(email1), True)
    email2 = "johnallen@email.com"
    self.assertEqual(user.verify_email(email2), True)
    email3 = "xxxx@asdf@asdf"
    self.assertEqual(user.verify_email(email3), False)
    email4 = "@email.com"
    self.assertEqual(user.verify_email(email4), False)

  def test_valid_and_invalid_user(self):
    name1 = 'john'
    surname1 = 'allen'
    email1 = "Johnallen@email.com" 

    user1 = User(name1, surname1, email1)
    self.assertEqual(user1.name, 'John')
    self.assertEqual(user1.surname, 'Allen')
    self.assertEqual(user1.email, 'johnallen@email.com')

    name2 = 'john'
    surname2 = 'allen'
    email2 = "@Johnallen@email" 

    with self.assertRaises(Exception) as context:
      user1 = User(name2, surname2, email2)

      self.assertTrue(email2 in context.exception)



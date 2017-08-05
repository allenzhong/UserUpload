import unittest
from processor.user import User

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
    self.assertEqual(user.capitalize_name(name1), "O'Connor")
    name3 = 'Allen'
    self.assertEqual(user.capitalize_name(name1), "Allen")

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
    email1 = "Johnallen@email.com"
    user = User(name, surname, email1)
    self.assertEqual(user.verify_email(email1), true)
    email2 = "JOHNALLEN@EMAIL.COM"
    self.assertEqual(user.verify_email(email2), true)
    email3 = "xxxx@asdf@asdf"
    self.assertEqual(user.verify_email(email3), false)
    email4 = "@email.com"
    self.assertEqual(user.verify_email(email4), false)





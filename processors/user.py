import re

class User(object):
  def __init__(self, name="", surname="", email=""):
    self._name = name
    self._surname = surname
    self._email = email

  @property
  def name(self):
    return self._name;

  @name.setter
  def name(self, value):
    self._name = value

  @property
  def surname(self):
    return self._surname

  @surname.setter  
  def surname(self, value):
    self._surname = value

  @property
  def email(self):
    return self._email

  @email.setter
  def email(self, value):
    self.email = value

  def capitalize_name(self, name):
    if name.find('\'') > 0:
      names = [x.capitalize() for x in name.split("'")]
      return "'".join(names)
    else:
      return name.capitalize()

  def downcase_email(self, email):
    return email.lower()

  def verify_email(self, email):
    regx = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
    return re.match(regx, email) != None

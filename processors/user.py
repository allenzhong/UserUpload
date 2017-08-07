import re

class EmailInvalidError(Exception):
  def __init__(self, message, errors):
    super(EmailInvalidError, self).__init__(message)
    self.errors = errors

class User(object):
  def __init__(self, name="", surname="", email=""):
    self.set_attributes(name, surname, email)

  def set_attributes(self, name="", surname="", email=""):
    self._name = self.capitalize_name(name) 
    self._surname = self.capitalize_name(surname)
    self._email = self.downcase_email(email)
 
    if not self.verify_email(self._email):
      raise EmailInvalidError("The given email '{0}' is invalid.".format(value)) 

  @property
  def name(self):
    return self._name;

  @name.setter
  def name(self, value):
    self._name = self.capitalize_name(value)

  @property
  def surname(self):
    return self._surname

  @surname.setter  
  def surname(self, value):
    self._surname = self.capitalize_name(value)

  @property
  def email(self):
    return self._email

  @email.setter
  def email(self, value):
    value = self.downcase_email(value)
    if self.verify_email(value):
      self.email = value
    else:
      raise EmailInvalidError("The given email '{0}' is invalid.".format(value))

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

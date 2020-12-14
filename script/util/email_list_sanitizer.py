
class email_list_sanitizer(object)
  def __init__(self, email_list):
    self.email_list = email_list 

  def sanitize(self):
    email_list = remove_special_chars_from_list(self.email_list)
    email_list = remove_webmasters_from_list(email_list)
    email_list = remove_blanks_from_list(email_list)
    email_list = list(set(email_list)) # make uniq
    return email_list

  def remove_special_chars_from_list(email_list):
    new_list = []
    for item in email_list:
      item = item.strip()
      new_list.append(item.replace('?',''))
    return new_list

  def remove_webmasters_from_list(email_list):
    new_list = []
    for item in email_list:
      if 'webmaster' in item.lower():
        continue
      else:
        new_list.append(item)
    return new_list

  def remove_blanks_from_list(email_list):
    new_list = []
    for item in email_list:
      if item == '' or item == ' ' or item is None:
        continue
      else:
        new_list.append(item)
    return new_list

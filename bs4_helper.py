# V3 - accepts url argument from user, is not cnn specific

import bs4

class bs4_helper(object):
  def __init__(self, html):
    self.html = html
    self.soup = bs4.BeautifulSoup(self.html, features="html.parser")

  def get_hrefs_for_a_tag(self):
    link_elements = self.soup.find_all('a', href=True)
    hrefs = []
    for link_element in link_elements:
      hrefs.append(link_element['href'])
    return hrefs

  def get_text_for_a_tag(self):
    link_elements = self.soup.find_all('a', href=True)
    texts = []
    for link_element in link_elements:
      texts.append(link_element.text)
    return texts

  def get_text_for_p_tags(self):
    elements = self.soup.find_all('p')
    texts = []
    for element in elements:
      texts.append(element.text)
    return texts

  def get_text_for_tds(self):
    tds = self.soup.findAll("td")    
    texts = []
    for td in tds:
      texts.append(td.text)
    return texts

  def get_text_for_strong_in_a_tag(self):
    link_elements = self.soup.find_all('a')
    texts = []
    for link_element in link_elements:
      children = link_element.findChildren("strong" , recursive=False)
      for child in children:
        texts.append(child.text)
    return texts 

  def get_src_for_input_tag(sefl):
    link_elements = self.soup.find_all('input', src=True)
    hrefs = []
    for link_element in link_elements:
      hrefs.append(link_element['href'])
    return hrefs

  def get_hrefs_for_class(self, class_name):
    link_elements = self.soup.findAll("a", {"class": class_name})
    hrefs = []
    for link_element in link_elements:
      hrefs.append(link_element['href'])
    return hrefs

  def get_hrefs_for_a_tags_in_div_by_class(self, class_name):
    div_elements = self.soup.findAll("div", {"class": class_name})
    hrefs = []
    for div_element in div_elements:
      a_tags = div_element.findAll("a")
      for tag in a_tags:
        hrefs.append(tag['href'])
    return hrefs

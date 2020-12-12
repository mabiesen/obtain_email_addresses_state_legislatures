from html_helper import  html_helper
from bs4_helper import bs4_helper

class state_helper(object):
  def __init__(self, url):
    self.url = url

  def prepare_soup(self):
    self.html_helper =  html_helper(self.url)
    self.bs4_helper = bs4_helper(self.html_helper.get_html())

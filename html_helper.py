from urllib.parse import urlparse
import requests

class html_helper(object):

  def __init__(self, url):
    self.url = url
    self.base_url = self.get_base_url()
    self.html = self.get_html() 

  def get_base_url(self):
    parsed_url = urlparse(self.url)
    base_url = parsed_url.netloc
    return base_url

  def get_html(self):
    result = requests.get(self.url, verify = False)
    result.raise_for_status()
    return result.text #we dont need the result status detail, just html

  def get_full_urls_from_hrefs(self, href_array):
    return_array = []
    for href in href_array:
      if ('http' in href) or ('www' in href):
        return_array.append(href)
      else:
        return_array.append(self.base_url + href)
    return return_array

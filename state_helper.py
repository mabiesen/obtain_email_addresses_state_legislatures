from html_helper import  html_helper
from bs4_helper import bs4_helper
from xlsx_helper import xlsx_helper
import tempfile
import csv

class state_helper(object):
  def __init__(self, url):
    self.url = url
    self.html_helper =  html_helper(self.url)

  def prepare_soup(self):
    self.bs4_helper = bs4_helper(self.html_helper.get_html())

  def parse_xlsx_file_column_by_index(self, page_index, column_index, pop_rows=False):
    ret_array = []
    with tempfile.NamedTemporaryFile(suffix='.xlsx') as fp:
      fp.write(self.html_helper.get_file_contents()) 
      self.xlsx_helper = xlsx_helper(fp.name)
      ret_array = self.xlsx_helper.get_data_from_column_by_index(page_index, column_index, pop_rows)
    return ret_array
      
  def parse_csv_column_by_index(self, column_index):
    ret_array = []
    unparsed_rows = self.html_helper.get_html().split("\n")
    for row in unparsed_rows:
      parts = row.split(",")
      if (len(parts) - 1) >= column_index:
        ret_array.append(parts[column_index])
    return ret_array


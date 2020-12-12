import openpyxl

class xlsx_helper(object):
  def __init__(self, workbook_path):
    self.workbook_path = workbook_path

  def get_data_from_column_by_index(self, page_index, column_letter, pop_rows):
    if isinstance(column_letter, int):
      column_letter = chr(ord('@')+number)
    wb = openpyxl.load_workbook(self.workbook_path)
    sheet = wb.worksheets[page_index]
    column = sheet[column_letter]
    ret_array = []
    for x in range(len(column)):
      ret_array.append(column[x].value) 
    if pop_rows:
      for x in range(pop_rows):
        ret_array.pop(0)
    return ret_array

import xlrd

class xls_helper(object):
  def __init__(self, workbook_path):
    self.workbook_path = workbook_path

  def get_data_from_column_by_index(self, page_index, column_index, pop_rows):
    if isinstance(column_index, str):
      column_index = ord(column_index) - 97
    wb = xlrd.open_workbook(self.workbook_path)
    sheet = wb.sheet_by_index(page_index)
    ret_array = sheet.col_values(column_index)
    if pop_rows:
      for x in range(pop_rows):
        ret_array.pop(0)
    return ret_array

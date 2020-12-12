import xlrd

class xlsx_helper(object):
  def __init__(self, workbook_path):
    self.workbook_path = workbook_path

  def get_data_from_column_by_index(self, page_index, column_index):
    wb = xlrd.open_workbook(workbook_path)
    sheet = wb.sheet_by_index(page_index)
    for i in range(sheet.nrows):
      print(sheet.cell_value(i, column_index))

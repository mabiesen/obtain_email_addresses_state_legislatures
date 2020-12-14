from lib.state_helper import state_helper

#BONUS_URL = 'https://floridafaf.org/legislature/contact-your-legislator/'
# this url contains xlsx downloads of senator/house email addresses

def run():
  HOUSE_XLSX_URL = 'https://floridafaf.org/wp-content/uploads/2020/08/House-Contact-List-82020.xlsx'
  SENATE_XLSX_URL = 'https://floridafaf.org/wp-content/uploads/2020/08/Senate-Contact-List-82020.xlsx'

  house_sh = state_helper(HOUSE_XLSX_URL)
  house_arr = house_sh.parse_xlsx_file_column_by_index(0,'U',2)
  for item in house_arr:
    print(item)

  senate_sh = state_helper(SENATE_XLSX_URL)
  sen_arr = senate_sh.parse_xlsx_file_column_by_index(0,'U',2)
  for item in sen_arr:
    print(item)
  return (house_arr + sen_arr)

if __name__ == "__main__":
  run()

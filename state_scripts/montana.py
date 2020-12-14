from lib.state_helper import state_helper

def run():
  primary_url = 'https://leg.mt.gov/legislator-information/csv'

  sh = state_helper(primary_url)
  email_addresses = sh.parse_csv_column_by_index(8)
  for addr in email_addresses:
    print(addr)

  return email_addresses

if __name__ == "__main__":
  run()

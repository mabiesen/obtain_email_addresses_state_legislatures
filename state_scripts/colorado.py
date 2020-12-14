from lib.state_helper import state_helper

def run():
  primary_url = 'https://leg.colorado.gov/legislators'

  # this link contains both house and senate
  # it is in a data table
  # to their kudos, they do have an excel output; but ideally this is csv

  all_sh = state_helper(primary_url)
  all_sh.prepare_soup()
  addresses = all_sh.bs4_helper.get_text_for_tds()
  addrs = []
  for address in addresses:
    if  '@' in address:
      addr = address.strip()
      addrs.append(addr)
      print(addr)
  return addrs

if __name__ == "__main__":
  run()

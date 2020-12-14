from lib.state_helper import state_helper

def run():
  PRIMARY_SENATORS_URL = 'https://malegislature.gov/Legislators/Members/Senate'
  PRIMARY_REPRESENTATIVES_URL = 'https://malegislature.gov/Legislators/Members/House'

  sen_sh = state_helper(PRIMARY_SENATORS_URL)
  sen_links = sen_sh.get_mailto_addresses()
  for link in  sen_links:
    print(link.replace('mailto:',''))

  rep_sh = state_helper(PRIMARY_REPRESENTATIVES_URL)
  rep_links = rep_sh.get_mailto_addresses()
  for link in  rep_links:
    print(link.replace('mailto:',''))

  return (sen_links + rep_links)

if __name__ == "__main__":
  run()

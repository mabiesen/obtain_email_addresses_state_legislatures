from lib.state_helper import state_helper

def run():
  senators_url = 'https://malegislature.gov/Legislators/Members/Senate'
  representatives_url = 'https://malegislature.gov/Legislators/Members/House'

  sen_sh = state_helper(senators_url)
  sen_links = sen_sh.get_mailto_addresses()
  for link in  sen_links:
    print(link.replace('mailto:',''))

  rep_sh = state_helper(representatives_url)
  rep_links = rep_sh.get_mailto_addresses()
  for link in  rep_links:
    print(link.replace('mailto:',''))

  return (sen_links + rep_links)

if __name__ == "__main__":
  run()

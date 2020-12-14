from lib.state_helper import state_helper

def run():
  PRIMARY_REPRESENTATIVES_URL = 'https://www.house.leg.state.mn.us/members/list'
  PRIMARY_SENATORS_URL = 'https://www.senate.mn/members/'

  sen_sh = state_helper(PRIMARY_SENATORS_URL)
  sen_links = sen_sh.get_mailto_addresses()
  for link in  sen_links:
    print(link)

  rep_sh = state_helper(PRIMARY_REPRESENTATIVES_URL)
  rep_links = rep_sh.get_mailto_addresses()
  for link in  rep_links:
    print(link)

  return (rep_links + sen_links)

if __name__ == "__main__":
  run()

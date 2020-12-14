from lib.state_helper import state_helper

def run():
  representatives_url = 'https://www.house.leg.state.mn.us/members/list'
  senators_url = 'https://www.senate.mn/members/'

  sen_sh = state_helper(senators_url)
  sen_links = sen_sh.get_mailto_addresses()
  for link in  sen_links:
    print(link)

  rep_sh = state_helper(representatives_url)
  rep_links = rep_sh.get_mailto_addresses()
  for link in  rep_links:
    print(link)

  return (rep_links + sen_links)

if __name__ == "__main__":
  run()

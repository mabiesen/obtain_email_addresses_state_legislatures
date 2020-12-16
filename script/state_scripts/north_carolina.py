from state_scripts.lib.state_helper import state_helper

def run():
  senators_url = 'https://www.ncleg.gov/Members/MemberInfoReport/S'

  sen_sh = state_helper(senators_url, True)
  sen_addrs = sen_sh.get_mailto_addresses()
  for addr in sen_addrs:
    print(addr)

  # the best solution is a messy one
  # house addrs will require a change of tactic
  # we need to simulate button clicking on the site and download to a designated folder

if __name__ == "__main__":
  run()

from state_scripts.lib.state_helper import state_helper

def run():
  senators_url = 'https://www.leg.state.nv.us/App/Legislator/A/Senate/'
  representatives_url = 'https://www.leg.state.nv.us/App/Legislator/A/Assembly/'

  # unfortunately these sites seem to use javascript, will have to wait

  sen_sh = state_helper(senators_url)
  rep_sh = state_helper(representatives_url)

  rep_addrs = rep_sh.get_mailto_addresses()
  for addr in rep_addrs:
    print(addr)

  sen_addrs = sen_sh.get_mailto_addresses()
  for addr in sen_addrs:
    print(addr)

  return (rep_addrs + sen_addrs)

if __name__ == "__main__":
  run()

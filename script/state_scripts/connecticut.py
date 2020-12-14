from state_scripts.lib.state_helper import state_helper

def run():
  representatives_url =  'https://www.cga.ct.gov/asp/menu/hlist.asp'
  senators_url = 'https://www.cga.ct.gov/asp/menu/slist.asp'

  # each of these pages has mail-to links included in primary page

  rep_sh = state_helper(representatives_url)
  sen_sh = state_helper(senators_url)

  rep_addrs = rep_sh.get_mailto_addresses()
  for addr in rep_addrs:
    print(addr)

  sen_addrs = sen_sh.get_mailto_addresses()
  for addr in sen_addrs:
    print(addr)

  return (rep_addrs + sen_addrs)

if __name__ == "__main__":
  run()

from lib.state_helper import state_helper

def run():
  PRIMARY_REPRESENTATIVES_URL = 'http://akleg.gov/house.php'
  PRIMARY_SENATORS_URL = 'http://akleg.gov/senate.php'

  # each of these pages has mail-to links included in primary page

  rep_sh = state_helper(PRIMARY_REPRESENTATIVES_URL)
  sen_sh = state_helper(PRIMARY_SENATORS_URL)

  rep_addrs = rep_sh.get_mailto_addresses()
  for addr in rep_addrs:
    print(addr)

  sen_addrs = sen_sh.get_mailto_addresses()
  for addr in sen_addrs:
    print(addr)

  return (sen_addrs + rep_addrs)

if __name__ == "__main__":
  run()

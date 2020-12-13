from lib.state_helper import state_helper

PRIMARY_SENATORS_URL = 'https://legislature.idaho.gov/senate/membership/'
PRIMARY_REPRESENTATIVES_URL = 'https://legislature.idaho.gov/house/membership/'

rep_sh = state_helper(PRIMARY_REPRESENTATIVES_URL)
sen_sh = state_helper(PRIMARY_SENATORS_URL)

rep_addrs = rep_sh.get_mailto_addresses()
for addr in rep_addrs:
  print(addr)

sen_addrs = sen_sh.get_mailto_addresses()
for addr in sen_addrs:
  print(addr)

from lib.state_helper import state_helper

PRIMARY_REPRESENTATIVES_URL =  'https://www.cga.ct.gov/asp/menu/hlist.asp'
PRIMARY_SENATORS_URL = 'https://www.cga.ct.gov/asp/menu/slist.asp'

# each of these pages has mail-to links included in primary page

rep_sh = state_helper(PRIMARY_REPRESENTATIVES_URL)
sen_sh = state_helper(PRIMARY_SENATORS_URL)

rep_addrs = rep_sh.get_mailto_addresses()
for addr in rep_addrs:
  print(addr)

sen_addrs = sen_sh.get_mailto_addresses()
for addr in sen_addrs:
  print(addr)

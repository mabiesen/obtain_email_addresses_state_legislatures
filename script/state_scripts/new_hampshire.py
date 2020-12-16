from state_scripts.lib.state_helper import state_helper

def run():
  representatives_url = 'http://gencourt.state.nh.us/downloads/Members.txt'
  senators_url = 'http://gencourt.state.nh.us/Senate/members/senate_roster.aspx'

  sen_sh = state_helper(senators_url, True)
  rep_sh = state_helper(representatives_url)

  rep_addrs = rep_sh.parse_csv_column_by_index(14, "\t")
  for addr in rep_addrs:
    print(addr)

  sen_addrs = sen_sh.get_mailto_addresses()
  for addr in sen_addrs:
    print(addr)

  return (rep_addrs + sen_addrs)

if __name__ == "__main__":
  run()

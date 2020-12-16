from state_scripts.lib.state_helper import state_helper

def run():
  senators_url = 'https://www.nysenate.gov/senators-committees'
  representatives_url = 'https://nyassembly.gov/mem/'

  sen_sh = state_helper(senators_url)
  sen_sh.prepare_soup()
  sen_links = sen_sh.bs4_helper.get_hrefs_for_a_tag()
  for link in sen_links:
    if '/senators/' in  link:
      temp_sh = state_helper('https://www.nysenate.gov' + link + '/contact')
      sen_addrs = temp_sh.get_mailto_addresses()
      for addr in sen_addrs:
        print(addr)

  rep_sh = state_helper(representatives_url)
  rep_addrs = rep_sh.get_mailto_addresses()
  for addr in rep_addrs:
    print(addr)

  return (sen_addrs)


# Im not finding anything for state representatives!!!

if __name__ == "__main__":
  run()

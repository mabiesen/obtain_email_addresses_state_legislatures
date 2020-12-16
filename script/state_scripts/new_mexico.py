from state_scripts.lib.state_helper import state_helper

def run():
  representatives_url =  'https://www.nmlegis.gov/members/Legislator_List?T=R'
  senators_url =  'https://www.nmlegis.gov/Members/Legislator_List?T=S'

  rep_sh = state_helper(representatives_url)
  rep_sh.prepare_soup()
  rep_links = rep_sh.bs4_helper.get_hrefs_for_a_tag()
  rep_addrs = []
  for link in rep_links:
    if 'Legislator?' in link:
      temp_sh = state_helper('https://www.nmlegis.gov/members/' + link)
      rep_addrs = temp_sh.get_mailto_addresses()
      for rep_addr in  rep_addrs:
        print(rep_addr)

  sen_sh = state_helper(senators_url)
  sen_sh.prepare_soup()
  sen_links = sen_sh.bs4_helper.get_hrefs_for_a_tag()
  sen_addrs = []
  for link in sen_links:
    if 'Legislator?' in link:
      temp_sh = state_helper('https://www.nmlegis.gov/Members/' + link)
      sen_addrs = temp_sh.get_mailto_addresses()
      for sen_addr in  sen_addrs:
        print(sen_addr)

if __name__ == "__main__":
  run()

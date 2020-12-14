from lib.state_helper import state_helper

def run():
  PRIMARY_SENATORS_URL = 'http://www.senate.ga.gov/senators/en-US/SenateMembersList.aspx'
  PRIMARY_REPRESENTATIVES_URL = 'http://www.house.ga.gov/Representatives/en-US/HouseMembersList.aspx'

  rep_sh = state_helper(PRIMARY_REPRESENTATIVES_URL)
  rep_sh.prepare_soup()
  sen_sh = state_helper(PRIMARY_SENATORS_URL)
  sen_sh.prepare_soup()

  sen_links = sen_sh.bs4_helper.get_hrefs_for_a_tag()
  sen_links = sen_sh.html_helper.get_full_urls_from_hrefs(sen_links)
  sen_addrs = []
  for link in sen_links:
    if 'Member=' in link:
      massaged_link = ('http://' + link).replace('./','/Senators/en-US/')
      tmp_rep_sh = state_helper(massaged_link)
      tmp_rep_sh.prepare_soup()
      links = tmp_rep_sh.bs4_helper.get_hrefs_for_a_tag()
      for link in links:
        if 'mailto:' in link:
          addr = link.replace('mailto:','')
          sen_addrs.append(addr)
          print(addr)

  rep_links = rep_sh.bs4_helper.get_hrefs_for_a_tag()
  rep_links = rep_sh.html_helper.get_full_urls_from_hrefs(rep_links)
  rep_addrs = []
  for link in rep_links:
    if 'Member=' in link:
      massaged_link = ('http://' + link).replace('./','/Representatives/en-US/')
      tmp_rep_sh = state_helper(massaged_link)
      tmp_rep_sh.prepare_soup()
      links = tmp_rep_sh.bs4_helper.get_hrefs_for_a_tag()
      for link in links:
        if 'mailto:' in link:
          addr = link.replace('mailto:','')
          sen_addrs.append(addr)
          print(addr)
  return (rep_addrs + sen_addrs)

if __name__ == "__main__":
  run()

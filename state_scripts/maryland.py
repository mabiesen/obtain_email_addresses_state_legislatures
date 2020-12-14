from lib.state_helper import state_helper

def run():
  senators_url = 'https://msa.maryland.gov/msa/mdmanual/05sen/html/sene.html'
  representatives_url = 'https://msa.maryland.gov/msa/mdmanual/06hse/html/hsee.html'

  sen_sh = state_helper(senators_url)
  sen_sh.prepare_soup()
  sen_links = sen_sh.bs4_helper.get_hrefs_for_a_tag()
  sen_addrs = []
  for link in  sen_links:
    if 'mailto:' in link:
      addr = link.replace('mailto:','')
      sen_addrs.append(addr)
      print(link.replace('mailto:',''))

  rep_sh = state_helper(representatives_url)
  rep_sh.prepare_soup()
  rep_links = rep_sh.bs4_helper.get_hrefs_for_a_tag()
  rep_addrs = []
  for link in  rep_links:
    if 'mailto:' in link:
      addr = link.replace('mailto:','')
      rep_addrs.append(addr)
      print(addr)

  return (sen_addrs + rep_addrs)

if __name__ == "__main__":
  run()

from state_scripts.lib.state_helper import state_helper

def run():
  house_democrats_url = 'https://indianahousedemocrats.org/members'
  house_republicans_url = 'https://www.indianahouserepublicans.com/members/'
  senate_democrats_url = 'https://www.indianasenatedemocrats.org/senators/'
  senate_republicans_url = 'https://www.indianasenaterepublicans.com/senators'

  # house dems do not appear to expose email addresses
  # senate dems appear to use javascript to populate email address

  #hd_sh = state_helper(house_democrats_url)
  #hd_sh.prepare_soup()
  hr_sh = state_helper(house_republicans_url)
  hr_sh.prepare_soup()
  sd_sh = state_helper(senate_democrats_url, True)
  sd_sh.prepare_soup()
  sr_sh = state_helper(senate_republicans_url)
  sr_sh.prepare_soup()


  hr_links = hr_sh.bs4_helper.get_hrefs_for_class('member-link')
  hr_addrs = []
  for link in hr_links:
    massaged_link = 'https://' + hr_sh.html_helper.base_url + '/' + link
    temp_sh = state_helper(massaged_link)
    temp_sh.prepare_soup()
    links = temp_sh.bs4_helper.get_hrefs_for_a_tag()
    for s_link in links:
      if 'mailto:' in s_link:
        addr = s_link.replace('mailto:','')
        hr_addrs.append(addr)
        print(addr)

  sd_links = sd_sh.bs4_helper.get_hrefs_for_class('eg-senators-grid-element-24')
  sd_addrs = []
  for link in sd_links:
    temp_sh = state_helper(link, True)
    temp_sh.prepare_soup()
    links = temp_sh.bs4_helper.get_hrefs_for_a_tag()
    for s_link in links:
      if 'mailto:' in s_link:
        addr = s_link.replace('mailto:','')
        sd_addrs.append(addr)
        print(addr)

  sr_links = sr_sh.bs4_helper.get_hrefs_for_a_tags_in_div_by_class('senator-item')
  sr_addrs = []
  for link in sr_links:
    temp_sh = state_helper('https://' + sr_sh.html_helper.base_url + link)
    temp_sh.prepare_soup()
    links = temp_sh.bs4_helper.get_hrefs_for_a_tag()
    for s_link in links:
      if 'mailto:' in s_link:
        addr = s_link.replace('mailto:','')
        sr_addrs.append(addr)
        print(addr)

  return (sr_addrs + sd_addrs + hr_addrs)

if __name__ == "__main__":
  run()

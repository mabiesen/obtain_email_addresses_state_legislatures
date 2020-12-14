from lib.state_helper import state_helper

def run():
  PRIMARY_SENATORS_URL = 'https://legislature.ky.gov/Legislators/senate'
  PRIMARY_REPRESENTATIVES_URL = 'https://legislature.ky.gov/Legislators/house-of-representatives'

  sen_sh = state_helper(PRIMARY_SENATORS_URL)
  sen_sh.prepare_soup()
  links =  sen_sh.bs4_helper.get_hrefs_for_a_tag()
  sen_addrs = []
  for link in links:
    if '/Legislators/Pages/Legislator-Profile.aspx' in link:
      massaged_link  =  'https://' + sen_sh.html_helper.base_url + link
      temp_sh = state_helper(massaged_link)
      temp_sh.prepare_soup()
      texts = temp_sh.bs4_helper.get_text_for_p_tags()
      for text in texts:
        if '@' in text and text[0] != '@':
          sen_addrs.append(text)
          print(text)

  rep_sh = state_helper(PRIMARY_REPRESENTATIVES_URL)
  rep_sh.prepare_soup()
  links =  rep_sh.bs4_helper.get_hrefs_for_a_tag()
  rep_addrs = []
  for link in links:
    if '/Legislators/Pages/Legislator-Profile.aspx' in link:
      massaged_link  =  'https://' + rep_sh.html_helper.base_url + link
      temp_sh = state_helper(massaged_link)
      temp_sh.prepare_soup()
      texts = temp_sh.bs4_helper.get_text_for_p_tags()
      for text in texts:
        if '@' in text and text[0] != '@':
          rep_addrs.append(text)
          print(text)
  
  return (rep_addrs + sen_addrs)

if __name__ == "__main__":
  run()

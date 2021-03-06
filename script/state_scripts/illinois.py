from state_scripts.lib.state_helper import state_helper

def run():
  representatives_url =  'https://www.ilga.gov/house/'
  senators_url = 'https://www.ilga.gov/senate/'

  #senators_url defunct

  rep_sh = state_helper(representatives_url)
  rep_sh.prepare_soup()


  links = rep_sh.bs4_helper.get_hrefs_for_a_tag()
  links = rep_sh.html_helper.get_full_urls_from_hrefs(links)
  rep_addrs = []
  for link in links:
    if 'MemberID=' in link and 'Rep.asp?' in link:
      massaged_link = ('https://' + link).replace('./','/')
      tmp_rep_sh = state_helper(massaged_link, True)
      tmp_rep_sh.prepare_soup()
      texts = tmp_rep_sh.bs4_helper.get_text_for_tds()
      for text in texts:
        if '@' in text and len(text) < 70:
          text = text.split()[-1]
          rep_addrs.append(text)
          print(text)

  return rep_addrs

if __name__ == "__main__":
  run()

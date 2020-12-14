from lib.state_helper import state_helper

def run():
  primary_url = 'https://www.arkleg.state.ar.us/Legislators/List'

  # this url contains both senate and house

  all_sh = state_helper(primary_url)
  all_sh.prepare_soup()
  hrefs = all_sh.bs4_helper.get_hrefs_for_a_tag()
  addrs = []
  for href in hrefs:
    if 'mailto' in href:
      if '?' not in href: # preventing capturing webmaster email
        addr = href.replace('mailto:','')
        addrs.append(addr)
        print(addr)
  return addrs

if __name__ == "__main__":
  run()

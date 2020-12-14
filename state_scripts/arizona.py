from lib.state_helper import state_helper

def run():
  primary_url = 'https://www.azleg.gov/memberroster/'
  # I had discovered that the usernames on this page correspond with email addresses
  # that end in 'azleg.gov'
  # "The email address is built by combining the legislator's userId and @azleg.gov. For example a legislator with a userId of jjones, would be jjones@azleg.gov"

  all_sh = state_helper(primary_url)
  all_sh.prepare_soup()

  all_text_for_links = all_sh.bs4_helper.get_text_for_a_tag()
  addrs = []
  for link in all_text_for_links:
    if 'Email' in link:
      email = link.replace('Email: ','').lower() + '@azleg.gov'
      addrs.append(email)
      print(email)
  return addrs 

if __name__ == "__main__":
  run()

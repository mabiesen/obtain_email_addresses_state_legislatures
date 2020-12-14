from lib.state_helper import state_helper

def run():
  PRIMARY_URL =  'https://www.utla.net/resources/contact-your-legislators'

  # BINGO
  # with this page we can get all email addresses, including governor
  # well.....
  # maybe. the email addresses listed are links, but they feign email address format

  all_sh = state_helper(PRIMARY_URL)
  all_sh.prepare_soup()
  addresses = all_sh.bs4_helper.get_text_for_strong_in_a_tag()

  addrs = []
  for address in addresses:
    if 'Expand'  not in address:
      addrs.append(address)
      print(address)
  return addrs

if __name__ == "__main__":
  run()

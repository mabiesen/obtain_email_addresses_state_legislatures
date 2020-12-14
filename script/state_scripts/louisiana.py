from state_scripts.lib.state_helper import state_helper

def run():
  representatives_url = 'https://house.louisiana.gov/H_Reps/H_Reps_Email'
  senators_url = 'http://senate.la.gov/Senators/Offices.asp'

  rep_sh = state_helper(representatives_url)
  rep_sh.prepare_soup()
  sen_sh = state_helper(senators_url)
  sen_sh.prepare_soup()

  rep_texts = rep_sh.bs4_helper.get_text_for_span_tags()
  rep_addrs =  []
  for text in rep_texts:
    if '@' in text:
      rep_addrs.append(text)
      print(text)

  sen_addrs = sen_sh.get_mailto_addresses()
  for addr in sen_addrs:
    print(addr)

  return (rep_addrs + sen_addrs)

if __name__ == "__main__":
  run()

# obtain_email_addresses_state_legislatures

Creating an easy method to determine state emails

What compelled me to create this?

1.  I had an issue recently  where I desired contacting representatives from multiple states, I soon learned that it is difficult to obtain representatives email addresses.
2.  From experience I can say that most representatives do not respond, or offer a horribly generic response which indicates your email was not read.  Therefore,  if you really wish to be heard, it is clear that you need to speak with a bullhorn: let every representative know your desire.
3.  Online forms often are terrible.  They often force you to categorize your  concern but do not offer an appropriate category (sometimes they  dont even offer the 'other' or 'misc' categories!).  There is really no great way  to know if the email was successful, whereas if you send it yourself you receive a mailer daemon error. Etc.
4.  There has been some talk in the news at different times of politicians using non-government email addresses.  This is important, the '.gov' email address to insure our concerns have documentation that could be made available via FOIA request(from what i understand).
5.  Its 2020: why aren't representative contact methdologies centralized/standardized?

FYI I know the code is bad at the moment.  This is early stages, trying to find common webscraping patterns that can be reused.  Also I need a brushup on  python package structure, but the output of the script(s) is more important to me than form.

## Prerequisites (what you need to run the scripts)

## Layout

1. /script/emails_fetcher.py : This is how you access all other scripts
2. emails_fetcher.py imports all state_scripts in the /scripts/state_scripts/ directory
3. each state script is designed with a single method 'run'. Each state script is expected to print its results.  The state scripts inherit their functionality from /scripts/state_scripts/lib/state_helper/
4. state_helper in turn inherits its functionality from files in /scripts/state_scripts/lib/util/

Not entirely proud of this layout.  With my current import methodology I cannot run state scripts directly, only through /scripts/emails_fetcher.py

But it works.

## Usage

Ultimately, this project is just a glorified web scraper :)

The  glory is in the fact that your representatives will be more accessible to you.

#### Available /script/emails_fetcher.py Bash Arguments

1. Print emails for state
```
./script/emails_fetcher.py alaska
```

2. Print emails for all states
```
./script/emails_fetcher.py all
```

3. Save all state email addresses to /output 
```
./scripts/emails_fetcher.py save
```

Optionally: If you want to make certain that emails are completely sanitized, add 'true' as a second argument.  So to sanitize alaska output:
```
./scripts/emails_fetcher.py alaska true
```

^^ This  is highly  recommended.  The goal of each state script was NOT to be pure, it was to get the job done.  Thus there are duplicates, blanks, webmaster addresses, etc.  (WIP)

Kinda a dumb way to do this.  I intend to come up with a better strategy both as regards bash arguments and as regards when/where to sanitize output.


# About Analysis Scripts

I am looking for quick-and-easy one offs

I will later manually compile the information and send to appropriate congressmen (and potentially their webmasters.... and potentially lawyers to bring these issues in line)

In order for these scripts to be run, the 'output' folder must first have data.

If it does not have data, please run:
```
<root_repo_dir>/scripts/email_fetcher.py save
```

This script will take a bit to complete as it gathers email data.  Once completed, the 
```
<root_repo_dir>/output
```
directory will be populated and you should be able to run the analysis scripts.


NOTE:  Any directory which shows as None represents a failure on my part to find a way to gather email addresses.

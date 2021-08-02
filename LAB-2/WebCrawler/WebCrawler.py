
import re
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import pandas as pd
# starting url. replace google with your own url.
url_website = input("Enter the website url: ")
print("\n")
# a queue of urls to be crawled
unprocessed_urls = deque([url_website])

# set of already crawled urls for email
processed_urls = set()

# a set of fetched emails
emails = set()

# process urls one by one from unprocessed_url queue until queue is empty
while len(unprocessed_urls):

    # move next url from the queue to the set of processed urls
    url = unprocessed_urls.popleft()
    processed_urls.add(url)

    # extract base url to resolve relative links
    parts = urlsplit(url)
    base_url = "{0.scheme}://{0.netloc}".format(parts)
    path = url[:url.rfind('/')+1] if '/' in parts.path else url

    # get url's content
    print("Crawling URL %s" % url)
    try:
        response = requests.get(url)
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        # ignore pages with errors and continue with next url
        continue

    # extract all email addresses and add them into the resulting set
    # You may edit the regular expression as per your requirement
    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
    emails.update(new_emails)

emails = list(emails)
#print(emails)
# remove duplicate emails
final_emails = []
for i in emails:
    if i not in final_emails:
        final_emails.append(i)
print("**********************************************************")
print("List of Email addresses crawled: ")
print("**********************************************************")
print(final_emails)
# Saving scrapped emails in CSV file
data = pd.DataFrame(emails, columns=["Email"])
data.to_csv('email.csv', index=False)
print("\n")
print("----------------------------------------------------------")
print(data)
# writing scrapped emails in text file
file = open("email.txt","w")
for element in final_emails:
    file.write(element + "\n")
# Reading scrapped emails from text file
file = open("email.txt","r")
print("**********************************************************")
print("Reading from Text file: ")
print("**********************************************************")
for items in file:
  print(items)
  


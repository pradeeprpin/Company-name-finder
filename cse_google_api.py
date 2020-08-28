import sys
import urllib.request
import urllib.parse
import re
from urllib.request import urlopen as ureqs
from bs4 import BeautifulSoup as soup
from googleapiclient.discovery import build


my_api_key = "AIzaSyDN5aXOu0vNHvn4I5r7SW-9NRXA0OIions"
my_cse_id = "33b91a4c8bd96facc"

def google_search(search_term, api_key, cse_id, **kwargs):
	service = build("customsearch", "v1", developerKey=api_key)
	res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
	#print(res)
	return res
	
query = input("Enter the query\n")

results = google_search(query, my_api_key, my_cse_id)
query_string=urllib.parse.urlencode({"search_query" : query})
html_content=urllib.request.urlopen("http://www.youtube.com/results?"+query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
print("\n*********Google Search Results*********\n")
print("Title == " +results['items'][0]['title'])


#Method : Fetching company name from CSE Google Api
#Not even 2 or 3 is  Accuracy while trying this,because it fecthing the domain name.
#some of the comapnies are registered with alias name. 

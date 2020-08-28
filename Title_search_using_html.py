import tldextract
from selenium import webdriver 
driver = webdriver.Chrome('C:/Users/PRADEEP P/Desktop/chromedriver.exe')
url = input("Enter The URL: ")
info = tldextract.extract(url)
print("Details:" , info)
domain_name=info.domain
print("Domain Name: ", domain_name)
get_title = driver.title 
driver.get(url) 
get_title = driver.title 
print("Title in HTML Page: ",get_title) 


#Method : Fetching company name from HTML title tag
#Not Much More Accuracy while trying this, 
#2 to 5 out of 10 may be correct while tring this mecthod

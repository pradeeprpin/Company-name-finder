import tldextract
from selenium import webdriver 
import json
import requests
driver = webdriver.Chrome('C:/Users/PRADEEP P/Desktop/chromedriver.exe')


#clearbit and url concaternation
str1=input("Enter The URL: ")
str3=input("Enter the company name to check Accuracy: ")
str2 = 'https://autocomplete.clearbit.com/v1/companies/suggest?query='
url = str2 + str1
driver.get(url) 
info = tldextract.extract(str1)

#Domain Details
print("Details:" , info)
print()
domain_name=info.domain
print("Domain Name: ", domain_name)
print()


#Accurate_name
r = requests.get(url)
val=r.json()
print ("Name of the Company: ",val[0]['name'])
print()
print("The Original Name of Company: ",str3)
print()

from similar_text import similar_text

match_case = similar_text(str3,val[0]['name'])
print("The Confidence Level of Output: ",match_case,"%")


#Clear-Bit API Method(Free Use)
#In,This Apporach the Comapny is Maximym of 90 to 100 % is same as we Expect
#As a result I found this as the best one to use
#In, This I have just joined the two strings and searching in Google
#If we want we can use Python ClearBit Module for Future purpose.
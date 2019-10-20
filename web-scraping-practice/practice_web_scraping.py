
from bs4 import BeautifulSoup
import requests
# import time
# from user_agent import generate_user_agent
# import mysql.connector
# import csv

#   .select()
#	.find()
#	.



def main():
	print('This is the main function')
	page_link = 'http://coreyms.com'
	headers = {'User-Agent':'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.63 Safari/537.36'}

	#page_response = requests.get(page_link,timeout=5,headers=headers)
	#page_content = BeautifulSoup(page_response.content,'html.parser')
	#print(page_content.prettify())
	#prices = page_content.find_all(class_='main_price')
	#prices = page_content.find_all('div',attrs={'class':'main_price'})

	try:
		page_response = requests.get(page_link,timeout=5,headers=headers)
		if page_response.status_code == 200:
			page_content = BeautifulSoup(page_response.content,'html.parser')
			# print(page_content)

		else:
			print(page_content.status_code)
	except requst.Timeout as e:
		print("It is time to timeout")
		print(str(e))
	else:
		for article in page_content.find_all('article'):
			headerline = article.header.h2.a.text
			# print(headerline)

			summary = article.div.p.text
			# print(summary)
			# time.sleep(1)
			
			vid_link = article.header.h2.a['href']
			# print(vid_link)

		for link in page_content.select('script[src]'):
			# print(link)
			print(link['src'])
				
			# print(link.keys())
			# if 'src' in link.keys():
			# 	print(link['src'])



if __name__ == '__main__':
	main()
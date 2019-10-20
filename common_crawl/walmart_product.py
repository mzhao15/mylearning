
import requests
# import argparse
import time
import json
from io import BytesIO
import gzip
# import boto3
from bs4 import BeautifulSoup

# import sys
# # reload(sys)
# sys.setdefaultencoding('utf8')

domain = 'walmart.com'

index_list = ['2018-30']#["2017-39"]#,"2017-43","2017-47"]

# Downloads full page
#
def download_page(record):

	offset, length = int(record['offset']), int(record['length'])
	offset_end = offset + length - 1

	# We'll get the file via HTTPS so we don't need to worry about S3 credentials
	# Getting the file on S3 is equivalent however - you can request a Range
	prefix = 'https://commoncrawl.s3.amazonaws.com/'

	# We can then use the Range header to ask for just this set of bytes
	resp = requests.get(prefix + record['filename'], headers={'Range': 'bytes={}-{}'.format(offset, offset_end)})

	# The page is stored compressed (gzip) to save space
	# We can extract it using the GZIP library
	raw_data = BytesIO(resp.content)
	f = gzip.GzipFile(fileobj=raw_data)

	# What we have now is just the WARC response, formatted:
	data = f.read().decode("utf8")
	response = ""
	
	if len(data):
		try:
			warc, header, response = data.strip().split('\r\n\r\n', 2)
		except:
			print('Not a good html response')
	# print(response)
	return response

def search_item(html_res):

	soup = BeautifulSoup(html_res,'html.parser')
	# print(soup.title.get_text())
	category = ""
	title = ""
	price =""

	try:
		category = soup.find('ol',{'class':'breadcrumb-list'}).contents[0].a.get_text().strip()
		print('Product category: %s' %category)
	except:
		pass

	try:
		searchresults = soup.find('div',{'id':'searchProductResult'}).ul.find_all('li')

		# for child in searchresults.children:
		for num,child in enumerate(searchresults):
			
			title = child.find('a',{'class':'product-title-link'})
			if title:
				print('Product title: %s'%title['aria-label'])

			price = child.find('div',{'class':'price-main-block'})
			if 'class' in price.div.attrs:
				subcls = price.div['class']
			else:
				subcls = ''
			# print(subcls)
			if price:
				price = price.find_all('span',{'class':'price-group'})
				# find_all returns a list not tag class
				if len(price) > 1 and subcls == ['product-variant-price']:
					price = price[0]['aria-label'] + '-' + price[1]['aria-label']
					print('Product price: %s' %price)
				else:
					print('Product price: %s' %price[0]['aria-label'])		
	except:
		pass

	# for single item page
	# try:
	# 	title = soup.find('div',{'class':'ProductTitle'}).h1['content']
	# except:
	# 	pass

	# try:
	# 	price = soup.find('span',{'class':'product-offer-price hf-BotRow'}).find('span',{'class':'price-group'})['aria-label']
	# except:
	# 	pass

def main():
	record_list = []
	print("Trying target domain: %s" % domain)

	for index in index_list:
		print("Trying index %s" % index)
		cc_url  = "http://index.commoncrawl.org/CC-MAIN-%s-index?" % index
		cc_url += "url=%s&matchType=domain&output=json" % domain

		response = requests.get(cc_url)

		if response.status_code == 200:
			records = response.content.splitlines()
			for record in records:
				record_list.append(json.loads(record))  
			print("Added %d results." % len(records))
		print("Found a total of %d hits." % len(record_list))

	# print(record_list[11065]['url'])
	# html_res = download_page(record_list[11065])
	# if html_res:
	# 	search_item(html_res)
	# with open('walmart.txt','w') as fout:
	# 	fout.write(html_res)

	for i in range(10000,11120):
		print(i)
		print(record_list[i]['url'])
		html_res = download_page(record_list[i])
		if html_res:
			search_item(html_res)

if __name__ == "__main__":
	main()
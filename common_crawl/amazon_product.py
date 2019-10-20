
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

domain = 'amazon.com'

index_list = ['2017-39']#['2018-30']#["2017-39"]#,"2017-43","2017-47"]

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
	# print(data)
	if len(data):
		try:
			warc, header, response = data.strip().split('\r\n\r\n', 2)
		except:
			print('Not a good html response')
	# print(response)
	return response

def search_item(html_res):

	soup = BeautifulSoup(html_res,'html.parser')

	category = ''
	title = ''
	price = ''

	category = soup.find('div',{'id':'nav-subnav'})
	# print(category)
	try:
		category = category['data-category'].strip()
	except:
		pass
	
	if type(category) is not str:
		category = 'None'

	print('Product category: %s'%category)

	title = soup.find('span',{'id':'productTitle'})
	if not title:
		title = soup.find('span',{'id':'ebooksProductTitle'})

	try:
		title = title.get_text().strip()
	except:
		pass
	print('Product title: %s'%title)

	# if title:
	# 	print('Product title: %s'%title.get_text().strip())
	# else:
	# 	print('Product does not have a title')

	try:
		# check the offer price
		price = soup.find('span',{'id':'priceblock_ourprice'})

		# check the deal price
		price = soup.find('span',{'id':'priceblock_dealprice'})

		# check buybox price
		if not price:
			price = soup.find('span',{'id':'price_inside_buybox'})

		# check new buy price
		if not price:
			price = soup.find('span',{'id':'newBuyBoxPrice'})

		# check the list prices
		if not price:
			tmmSwatches = soup.find('div',{'id':'tmmSwatches'})
			if tmmSwatches:
				base = tmmSwatches.find('span',{'class':'a-color-base'})
				if base:
					price = base.span
		elif not price:
			# print('Product does not have a price')
			pass
		price = price.get_text().strip()
	except:
		pass
	# price = soup.find('span',{'id':'price_inside_buybox'})
	# print(price)
	print('Product price: %s'%price)

def main():
	record_list = []
	# print("Trying target domain: %s" % domain)

	for index in index_list:
		# print("Trying index %s" % index)
		cc_url  = "http://index.commoncrawl.org/CC-MAIN-%s-index?" % index
		cc_url += "url=%s&matchType=domain&output=json" % domain

		response = requests.get(cc_url)

		if response.status_code == 200:
			records = response.content.splitlines()
			for record in records:
				record_list.append(json.loads(record))  
			print("Added %d results." % len(records))
		print("Found a total of %d hits." % len(record_list))

	print(record_list[5013]['url'])
	html_res = download_page(record_list[5013])
	if html_res:
		search_item(html_res)
	try:
		with open('amazon.txt','w') as fout:
			fout.write(html_res)
	except:
		pass

	# for i in range(5000,6015):
	# 	print(i)
	# 	print(record_list[i]['url'])
	# 	html_res = download_page(record_list[i])
	# 	if html_res:
	# 		search_item(html_res)

if __name__ == "__main__":
	main()
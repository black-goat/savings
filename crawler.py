import sys
import extract
import codecs

def crawl(page_name):
	#The file we will write sale info to
	file = codecs.open('sale_info.txt', 'w', 'UTF-8')

	menu = extract.extract_sales_pages(page_name)
	for m_item in menu:
		temp_m_item = m_item

		while temp_m_item != None:
			items = extract.extract_items(temp_m_item)

			for item in items[0]:
				print('On item: {}'.format(item))
				item_info = extract.extract_savings(item)
				if(item_info != None):
					file.write('{} on sale for {} at -{} discount\r\n'.format(*item_info))

			temp_m_item = items[1]


def crawl_test(page_name):
	#The file we will write sale info to
	file = codecs.open('sale_info.txt', 'w', 'UTF-8')

	temp_m_item = page_name

	while temp_m_item != None:
		items = extract.extract_items(temp_m_item)

		for item in items[0]:
			print('On item: {}'.format(item))
			item_info = extract.extract_savings(item)
			if(item_info != None):
				file.write('{} on sale for {} at -{} discount\r\n'.format(*item_info))

		temp_m_item = items[1]

p = input()
crawl_test(p)

#p = input()
#s = extract.extract_savings(p)
#print('{} on sale for {} at -{} discount'.format(*s))
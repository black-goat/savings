import sys
import requests
import bs4

def extract_sales_pages(page_name):
	"""Extracts links to sales pages"""
	page = requests.get(page_name)
	page.raise_for_status()

	soup = bs4.BeautifulSoup(page.text, 'lxml')
	pages = soup.find_all('a', class_='ty-menu__item-link', href=True)

	return [p.get('href') for p in pages]

def extract_items(page_name):
	"""Extracts only links to items from a webpage"""
	page = requests.get(page_name)
	page.raise_for_status()

	soup = bs4.BeautifulSoup(page.text, 'lxml')
	divs = soup.find_all('div', class_ = 'ty-grid-list__image')

	next_page = get_next_page(soup)

	return [d.find_next('a').get('href') for d in divs], next_page

def get_next_page(page_soup):
	"""Gets next sales page. Returns url if such exists and None otherwise"""
	nxt = page_soup.find('a', class_='ty-pagination__next', href=True)
	if(nxt != None):
		return nxt.get('href')
	else:
		return None


def extract_savings(page_name):
	"""Extracts name, price and savings % of product (if product is on sale)"""
	page = requests.get(page_name)
	page.raise_for_status()

	soup = bs4.BeautifulSoup(page.text, 'lxml')

	dc = soup.find('div', class_='ty-product-block__img-wrapper')
	dc = dc.find('span', class_='ty-discount-label__value')

	if dc == None:
		return None
	else:
		name = soup.title.string
		price = soup.find('span', class_ = 'ty-price-num').string
		discount = get_percent_savings(dc.string)

		return (name, price, discount)

def get_percent_savings(savings_string):
	"""Extracts only % savings from string"""
	for word in savings_string.split():
		if word[0].isdigit():
			return word
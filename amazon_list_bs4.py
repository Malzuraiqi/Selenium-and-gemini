import requests
from bs4 import BeautifulSoup as bs

response = requests.get('https://www.amazon.com/shop/johnfish/list/252AOEG17NIJ1?ref_=aip_sf_list_spv_ofs_mixed_d')
soup = bs(response.content, 'html.parser')
section = soup.find('div', class_='a-section list-spv-container')
items = section.find_all('div', class_='single-product-item list-spv')
for item in items:
    details = item.find('div', class_='product-detail-container')
    author = details.find('span', class_='product-brand-text')
    title = details.find('span', class_='product-title-text')
    print(f"{title.getText()} by {author.getText()} ssssssss")
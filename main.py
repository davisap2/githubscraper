# -*- coding: utf-8 -*-
"""
Created on Tue May 31 21:30:18 2022

@author: Austin Davis
"""

import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input Github User: ')
url = 'https://github.com/'+github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image = soup.find('img', {'alt': 'Avatar'})['src']
print(profile_image)
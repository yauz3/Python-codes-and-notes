import os
from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET
import mygene
import pandas as pd
import xlsxwriter
import textwrap
import requests
from bs4 import BeautifulSoup
from pymol.cgo import *
import sys
import argparse
import timeit
import datetime
from argparse_color_formatter import ColorHelpFormatter
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


def beautiful_soup():
    page = requests.get(e3_url)
    soup = BeautifulSoup(page.content, "html.parser")
    df_list = pd.read_html(soup)
    df = df_list[-2]
    df.to_csv("deneme.csv")
    data = []
    table = soup.find('table', attrs={'class':'table table-condensed table-bordered'})
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    print(data)
    """for link in soup.find_all('a',href = True):
        print(link)"""




def selenium(e3_url):

    driver = webdriver.Chrome(ChromeDriverManager().install())
    # get geeksforgeeks.org
    driver.get(e3_url)
    time.sleep(7)
    html = driver.page_source
    df_list = pd.read_html(html)
    for df in df_list:
        if "YOUR_STRING_TO_ELIMINATE_OTHER_TABLES" in df:
            number=e3_url.split("=")[-1] # change here to save your files in diffent names
            os.chdir("PATH_TO_SAVE_WHERE_YOU_WANT")
            df.to_csv(f'{number}_e3_to_protac.csv')
            driver.close()

def linker_to_protac():
    for i in range(1,1502):
        id_number=i
        link_url = f"YOUR_URL_HERE{id_number}"
        selenium(link_url)

linker_to_protac()
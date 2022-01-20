from setuptools import setup # Need this to handle modules
import pandas as pd
import os
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlsplit, parse_qs

import py2exe 
chromedriverPath = os.path.abspath(os.getcwd())+'\exe\chromedriver.exe'
exe_files = [('.', [chromedriverPath])]
setup(
    console=['mostactivestocks.py'],
    data_files = exe_files,
    )
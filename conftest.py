import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language",
                     action="store",
                     default="ru",
                     help="Choose language: en, fr, es, ru")
    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     help="Choose browser: chrome or firefox")

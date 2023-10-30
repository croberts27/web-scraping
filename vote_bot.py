from selenium import webdriver
import time

class VoteBot():
  def __init__(self):
      self.driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")
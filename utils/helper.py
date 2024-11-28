from selenium import webdriver
from selene import browser
from appium.options.android import UiAutomator2Options
import os

def create_driver():
  value = 'apis'#os.environ.get('browser')
  if value == 'chrome':
    driver = browser
    return driver
  elif value == 'firefox':
    firefox = browser.with_(driver_name='firefox')
    return firefox
  elif value == 'android':
    android_options = UiAutomator2Options()
    android_options.new_command_timeout = 60
    android_options.app_activity = 'org.wikipedia.main.MainActivity'
    android_options.app_package = 'org.wikipedia.alpha'  # not mandatory
    android_options.platform_name ='Android'
    browser.config.driver_remote_url = 'http://127.0.0.1:4723'
    browser.config.driver_options = android_options
    driver_android = browser
    return driver_android
  elif value == 'apis':
    return None
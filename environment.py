from utils.helper import *
from selene import browser

#def before_all(context):
  #context.driver = None

def before_scenario(context, scenario):
  context.driver = create_driver()

def after_scenario(context, scenario):
  browser.quit

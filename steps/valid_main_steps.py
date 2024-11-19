from behave import *

from selene import by, have, be
from appium.webdriver.common.appiumby import AppiumBy

by_id = lambda id: (AppiumBy.ID, f'org.wikipedia.alpha:id/{id}')

@given('user open browser')
def user_open_browser(context):  
  context.driver.open('https://www.validecd.com.co/')

@when('user search valid solutions')
def user_search_valid_solutions(context):
  context.driver.element(by.xpath("//a[contains(text(),'Quiénes Somos')]")).click()

@then('the system should display valid results')
def the_system_should_display_valid(context): 
  context.driver.element(by.xpath("//span[contains(text(),'Somos Valid')]")).should(be.visible)

@given('user open app wikipedia')
def user_open_app_wikipedia(context):
  context.driver.open()
  context.driver.element(by_id('fragment_onboarding_skip_button')).click()

@when('user search appium')
def user_search_appium(context):
  context.driver.element((AppiumBy.ACCESSIBILITY_ID, 'Buscar en Wikipedia')).click()
  context.driver.element(by_id('search_src_text')).type('Appium')

@then('the system should display appium results')
def the_system_should_display_appium_results(context):
  context.driver.all(by_id('page_list_item_title')).should(have.size_greater_than(0))
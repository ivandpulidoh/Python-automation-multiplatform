from utils.helper import *
from selene import browser
import pyautogui
import io
import os

from behavex_images import image_attachments
from behavex_images.image_attachments import AttachmentsCondition

def before_all(context):
  image_attachments.set_attachments_condition(context, AttachmentsCondition.ALWAYS)

def before_scenario(context, scenario):
  context.driver = create_driver()

def after_scenario(context, scenario):
  browser.quit

def after_step(context, step):
  if context.driver:
    screenshot = pyautogui.screenshot()

    # Convertir a formato binario
    screenshot_binary = io.BytesIO()
    screenshot.save(screenshot_binary, format="PNG")
    image_attachments.attach_image_binary(context, screenshot_binary.getvalue())
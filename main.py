



from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
from datetime import datetime

import DifferencesBetweenLists
import SendDiscordMessage

import ScrapeWebPage

#All feed
#url = 'https://rpilocator.com/feed/'
#US specific Feed for rpilocator
url = 'https://rpilocator.com/feed/?country=US'

existing_item_list = []

print("Starting up")

#US specific Feed for rpilocator and only for Raspberry Pi 4
#url = 'https://rpilocator.com/feed/?country=US&cat=PI4'


while 1!=0:
    print("Current Time: ")
    print(datetime.now())

    driver = ScrapeWebPage.open_the_driver(url)
    driver, page_content = ScrapeWebPage.scrape_web_page(driver, url)
    list_of_items_available = ScrapeWebPage.search_page_content(page_content)

    print("existing_item_list: ")
    print(existing_item_list)

    print("list_of_items_available")
    print(list_of_items_available)


    newly_added_items = DifferencesBetweenLists.differences_between_lists(existing_item_list, list_of_items_available)

    print("Newly Added Items:")
    print(newly_added_items)

    if newly_added_items != []:
        #Something is in stock
        SendDiscordMessage.sendDiscordMessage("message goes here")

    #all done, close the page
    ScrapeWebPage.close_the_driver(driver)

    print("Sleeping")
    time.sleep(10) #sleep for 90 (1 1/2 minutes)




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
#url = 'https://rpilocator.com/feed/?country=US'
url = 'https://rpilocator.com/feed/'

existing_item_list = []

print("Starting up")

#US specific Feed for rpilocator and only for Raspberry Pi 4
#url = 'https://rpilocator.com/feed/?country=US&cat=PI4'

first_time_through = True #

while 1!=0:
    print("Current Time: ")
    print(datetime.now())

#    driver = ScrapeWebPage.open_the_driver(url)
#    driver, page_content = ScrapeWebPage.scrape_web_page(driver, url)
    page_content = ScrapeWebPage.scrape_web_page(url)
    list_of_items_available = ScrapeWebPage.search_page_content(page_content)

    # print("existing_item_list: ")
    # print(existing_item_list)
    #
    # print("list_of_items_available")
    # print(list_of_items_available)


    newly_added_items = DifferencesBetweenLists.differences_between_lists(existing_item_list, list_of_items_available)

    # print("newly_added_items:")
    # print(newly_added_items)

    if newly_added_items != []:
        #Something is in stock
        items_in_stock = ScrapeWebPage.get_list_of_in_stock_items(newly_added_items)

        print("items_in_stock")
        print(items_in_stock)


        #If this is the first time executing, I don't want to get an alert about something being in stock, since it's just the first list
        if first_time_through == True:
            pass
        else:
            SendDiscordMessage.sendDiscordMessage("Something is in stock: ")
            for each_item in items_in_stock:
                SendDiscordMessage.sendDiscordMessage(each_item)

    #all done, close the page
#    ScrapeWebPage.close_the_driver(driver)

    existing_item_list = list_of_items_available

    first_time_through = False

    time_to_sleep = 90
    print("Sleeping for " + str(time_to_sleep) + " seconds")
    time.sleep(time_to_sleep) #sleep for 90 (1 1/2 minutes)
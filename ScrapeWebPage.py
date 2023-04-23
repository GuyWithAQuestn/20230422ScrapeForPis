from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

import requests


def get_list_of_in_stock_items(newly_added_items):

    # print("newly_added_items")
    # print(newly_added_items)

    all_new_items_available = []

    for each_item in newly_added_items:
        # print("each_item")
        # print(each_item)
        description = each_item.find('description').text
        link = each_item.find('link').text

        string_of_description_and_link = str(description) + " " + str(link)
        all_new_items_available.append(string_of_description_and_link)

    return all_new_items_available



    # # For each of the items in the XML code...
    # for each_item in all_items:
    #     #            print ("in for loop")
    #     title = each_item.find('title').text
    #     description = each_item.find('description').text
    #     link = each_item.find('link').text
    #     published = each_item.find('pubDate').text
    #     single_item = {
    #         'title': title,
    #         'description': description,
    #         'link': link,
    #         'published': published
    #     }



def check_webpage_source_for_security_block(webpage_source, security_block):

    soup = BeautifulSoup(webpage_source, 'html.parser')
    if soup.findAll(text="Security Block!"):
        print("Found a security block page. We can't move on yet and will need to search it again")
    else:
        security_block = False

    return security_block


def Scrape_Website_Code(website_url):

    # If it thinks your a bot, will block the scraper. So set up headers to make it look like you're coming from Chrome (e.g. area human)
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    }

    #try to scrape the site for code and return it
    try:
        r = requests.get(website_url,headers=header)
        soup = BeautifulSoup(r.content, features='xml')
        return soup
    #if something goes wrong with the scrape, return the error and throw an error
    except Exception as e:
        print('The scraping job failed. See exception: ')
        print(e)
        return 1


def search_page_content(page_source):
    list_of_items_available = []

#    soup_of_page_source = BeautifulSoup(page_source, 'lxml')

#    print("soup_of_page_source: ")
#    print(soup_of_page_source)

    list_of_items_available = page_source.findAll('item')

    # print("list_of_items_available: ")
    # print(list_of_items_available)


    # # For each of the items in the XML code...
    # for each_item in all_items:
    #     #            print ("in for loop")
    #     title = each_item.find('title').text
    #     description = each_item.find('description').text
    #     link = each_item.find('link').text
    #     published = each_item.find('pubDate').text
    #     single_item = {
    #         'title': title,
    #         'description': description,
    #         'link': link,
    #         'published': published
    #     }

    return list_of_items_available

def Scrape_Website_Code(website_url):

    # If it thinks your a bot, will block the scraper. So set up headers to make it look like you're coming from Chrome (e.g. area human)
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    }

    #try to scrape the site for code and return it
    try:
        r = requests.get(website_url,headers=header)
        soup = BeautifulSoup(r.content, features='xml')
        return soup
    #if something goes wrong with the scrape, return the error and throw an error
    except Exception as e:
        print('The scraping job failed. See exception: ')
        print(e)
        return 1

#def scrape_web_page(driver, url):
def scrape_web_page(url):

    # # Navigate to the URL
    # driver.get(url)

    r = requests.get(url)
    page_content = BeautifulSoup(r.content, features='xml')

    # # Get the page content
    # page_content = driver.page_source

#    print("Here's some page_content")
#    print(page_content)

    # Print the page content
    # print(page_content)

    # Get the page content
    # page_content = driver.execute_script("return document.documentElement.outerHTML")
    # # Save the page content to a file
    # with open('/Users/bryan/Downloads/output.html', 'w', encoding='utf-8') as f:
    #     f.write(page_content)

    return page_content


def open_the_driver(url):
    # Generate a random user agent header using fake_useragent library
    ua = UserAgent()
    headers = {'User-Agent': ua.random}

    # Define the proxy you want to use
    proxy = 'http://p.webshare.io:9999'

    # Set up the Selenium driver with the proxy and headers
    options = Options()
    #    options.add_argument('--proxy-server={}'.format(proxy))  # Comment in/out for use of proxy
    #    options.add_argument('user-agent={}'.format(headers['User-Agent']))  # Comment in/ out for change of headers
    # options.add_argument('user-agent={}'.format(headers))
    driver = webdriver.Chrome(options=options)

    return driver


def close_the_driver(driver):
    # Close the driver
    driver.quit()
    print("driver closed")

    return 0


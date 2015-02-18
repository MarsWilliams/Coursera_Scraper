from splinter import Browser
from bs4 import BeautifulSoup
import json
import string






def parse_soup(soup):
    courses = []
    course_blocks = soup.findAll('div', {'class': 'c-courseList-entry'})
    print course_blocks
    






def make_soup(html):
    soup = BeautifulSoup(html)
    return soup





def get_html():
    with Browser('chrome') as browser:
        # Visit URL
        url = "https://www.coursera.org/courses?languages=en"
        browser.visit(url)
        # Find and click the 'load_more' button
        content = browser.find_link_by_partial_href('#')
        #trick browser into waiting
        browser.is_element_present_by_tag('a', wait_time=5)
        # Interact with elements
        return (browser.html)






def main():
    course_list = get_html()
    soup = make_soup(course_list)
    course_details = parse_soup(soup)




    




if __name__ == '__main__':
   
    main()





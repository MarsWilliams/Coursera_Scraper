from splinter import Browser
from bs4 import BeautifulSoup
import json
import string






def parse_soup(soup):
    """Parses the soup object by finding elements and extracting inner element text"""

    # create array to store courses
    courses = []
    # identify all course information elements
    course_blocks = soup.findAll('div', {'class': 'c-courseList-entry'})

    # iterrate through courses to parse course details
    for course in course_blocks:

        # initialize a course object
        course_details = {}
        
        authors = []

        course_details['organization'] = str(course.find('div', {'class': 'c-courseList-entry-university'}).find('a').text)
        course_details['title'] = str(course.find('div', {'class': 'c-courseList-entry-title'}).find('a').text)
        author_list = course.find('div', {'class': 'c-courseList-entry-instructor'}).findAll('a')

        # iterrate through authors to store individual names in the author array
        for author in author_list:
            name = str(author.text)
            authors.append(name)

        course_details['authors'] = authors

        # parse irregular formatting of schedule information; necessary to store as string because selection of text element removes '<br/>' tag
        schedule_information = str(soup.find('div', {'class': 'bt3-col-xs-3 bt3-text-right'}).find('p')).replace('<p>','').replace('</p>', '')
        
        # differentiate between courses with a defined start and end date and those with indeterminate or passed schedules
        if '<br/>' in schedule_information:
            schedule_pieces = schedule_information.split('<br/>')
            course_details['start_date'] = schedule_pieces[0]
            course_details['duration'] = schedule_pieces[1]
            course_details['notes'] = None
        else:
            course_details['start_date'] = None
            course_details['duration'] = None
            course_details['notes'] = schedule_information

        # append each course object with detail attributes to the courses array
        courses.append(course_details)

    return courses





def make_soup(html):
    """Creates a BeautifulSoup object, which represents the document as a nested data structure"""

    # convert html string to BeautifulSoup object
    soup = BeautifulSoup(html)
    return soup





def get_html():
    """Mimic browser behavior so async loading is complete before html content is extracted"""

    with Browser('chrome') as browser:
        # Visit URL
        url = "https://www.coursera.org/courses?languages=en"
        browser.visit(url)
        # # Find and click the 'load_more' button
        content = browser.find_link_by_partial_href('#')
        #trick browser into waiting
        browser.is_element_present_by_tag('a', wait_time=6)
        # Interact with elements
        return (browser.html)






def main():
    course_list = get_html()
    soup = make_soup(course_list)
    courses = parse_soup(soup)




    




if __name__ == '__main__':
   
    main()





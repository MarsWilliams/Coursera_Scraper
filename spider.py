from splinter import Browser
from bs4 import BeautifulSoup
import json
import string






def parse_soup(soup):
    courses = []
    course_blocks = soup.findAll('div', {'class': 'c-courseList-entry'})

    for course in course_blocks:

        
        course_details = {}
        
        authors = []

        course_details['organization'] = str(course.find('div', {'class': 'c-courseList-entry-university'}).find('a').text)
        course_details['title'] = str(course.find('div', {'class': 'c-courseList-entry-title'}).find('a').text)
        author_list = course.find('div', {'class': 'c-courseList-entry-instructor'}).findAll('a')

        for author in author_list:
            name = str(author.text)
            authors.append(name)

        course_details['authors'] = authors

        schedule_information = str(soup.find('div', {'class': 'bt3-col-xs-3 bt3-text-right'}).find('p')).replace('<p>','').replace('</p>', '')
        
        if '<br/>' in schedule_information:
            schedule_pieces = schedule_information.split('<br/>')
            course_details['start_date'] = schedule_pieces[0]
            course_details['duration'] = schedule_pieces[1]
            course_details['notes'] = None
        else:
            course_details['start_date'] = None
            course_details['duration'] = None
            course_details['notes'] = schedule_information

        courses.append(course_details)

    return courses



def make_soup(html):
    soup = BeautifulSoup(html)
    return soup





def get_html():
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





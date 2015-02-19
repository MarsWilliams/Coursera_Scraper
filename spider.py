from splinter import Browser
from bs4 import BeautifulSoup
from selenium.common.exceptions import ElementNotVisibleException






def format_course(course):
    formatted_course = ''
    print (type(course['authors']))
    try:
        formatted_course = formatted_course + course['organization'] + '\t'
    except TypeError:
        formatted_course = formatted_course + 'None' + '\t'

    try:
        formatted_course = formatted_course + course['title'] + '\t'
    except TypeError:
        formatted_course = formatted_course + 'None' + '\t'

    try:
        if len(course['authors']) > 1:
            print ('hell0', course['authors'])
            authors = '; '.join(course['authors'])
            print (authors)
            formatted_course = formatted_course + authors + '\t'
        else:
            authors = ''.join(course['authors'])
            formatted_course = formatted_course + authors + '\t'
    except TypeError:
        formatted_course = formatted_course + 'None' + '\t'

    try:
        formatted_course = formatted_course + course['start_date'] + '\t'
    except TypeError:
        formatted_course = formatted_course + 'None' + '\t'

    try:
        formatted_course = formatted_course + course['duration'] + '\t'
    except TypeError:
        formatted_course = formatted_course + 'None' + '\t'

    try:
        formatted_course = formatted_course + course['schedule_notes']
    except TypeError:
        formatted_course = formatted_course + 'None'
    
    formatted_course = formatted_course + '\n'

    return formatted_course






def write_courses_document(courses):
    document = open("/Users/marswilliams/coursera/courses.txt", "w")
    for course in courses:
        formatted_course = format_course(courses[course])
        document.write(formatted_course)
    document.close()






def parse_html(soup):
    """Parses the soup object by finding elements and extracting inner element text"""

    # create array to store courses
    courses = {}
    # identify all course information elements
    course_blocks = soup.findAll('div', {'class': 'c-courseList-entry'})

    # iterrate through courses to parse course details
    for course in course_blocks:

        course_id = course['data-course']

        course_details = {}

        authors = []

        course_details['organization'] = course.find('div', {'class': 'c-courseList-entry-university'}).find('a').text
        course_details['title'] = course.find('div', {'class': 'c-courseList-entry-title'}).find('a').text
        
        try:
            author_list = course.find('div', {'class': 'c-courseList-entry-instructor'}).findAll('a')

            # iterrate through authors to store individual names in the author array
            for author in author_list:
                name = author.text
                authors.append(name)

            course_details['authors'] = authors

        except AttributeError:
            course_details['authors'] = None

        schedule_p = str(course.find('div', {'class': 'bt3-col-xs-3 bt3-text-right'}).find('p'))

        schedule_information = schedule_p.replace('<p>', '').replace('<p class="c-courseList-entry-tagline">', '').replace('<p class="c-courseList-entry-noOpenSessions">', '').replace('</p>', '')

        # differentiate between courses with a defined start and end date and those with indeterminate or passed schedules
        if '<br/>' in schedule_information:
            schedule_pieces = schedule_information.split('<br/>')
            course_details['start_date'] = schedule_pieces[0]
            course_details['duration'] = schedule_pieces[1]
            course_details['schedule_notes'] = None
        else:
            course_details['start_date'] = None
            course_details['duration'] = None
            course_details['schedule_notes'] = schedule_information


        # append each course object with detail attributes to the courses array
        courses[course_id] = course_details   

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

        more_content = True

        # while more_content:
        while more_content:
            # looks for load more text
            load_more = browser.is_text_present("Load more courses...", wait_time=6)

            try:
                # looks for load more link
                load_more_link = browser.find_link_by_href('#')
                load_more_link.click()
                continue
            except ElementNotVisibleException:
                html = str(browser.html)
                more_content = False
            
                return html






def main():
    course_list = get_html()
    soup = make_soup(course_list)
    courses = parse_html(soup)
    course_list_document = write_courses_document(courses)



    




if __name__ == '__main__':
   
    main()





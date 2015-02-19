import model

import datetime

def load_courses(session):
    # use u.user
    #reads in file and parses data
    users_table = open("../output/courses.txt", "r")
    for line in users_table:
        aline = line.split('\t')
        organization, title, authors, start_date, duration, schedule_notes = aline
        
        #creates instance of user
        course = model.Course()
        course.title = title
        course.organization = organization
        course.authors = authors

        starting = start_date.split()

        try:
            # parse dates
            month, day, year = starting
            day = day.replace(',', '').replace('st', '').replace('th', '').replace('nd', '').replace('rd', '')
            months = {"Jan":1,"Feb":2, "Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7, "Aug":8, "Sep":9, "Oct":10,"Nov":11,"Dec":12}
            date = datetime.date(int(year), months[month], int(day))

            course.start_date = date

            converted_duration = duration.replace('st', '').replace(' weeks long', '').replace('th', '').replace('nd', '').replace('rd', '')
            lasting = datetime.timedelta(days=((int(converted_duration))*7))

            course.end_date = lasting + date

        except ValueError:
            course.start_date = None
            course.end_date = None
 

        try:
            course.duration = duration

        except ValueError:
            course.duration = None

        if schedule_notes == None:
            course.schedule_notes = None
        else:
            course.schedule_notes = schedule_notes


        # adds course to session
        session.add(course)
    
    #commits session changes
    session.commit()


def main(session):
    # You'll call each of the load_* functions with the session as an argument
    load_courses(session)

if __name__ == "__main__":
    s= model.connect()
    main(s)
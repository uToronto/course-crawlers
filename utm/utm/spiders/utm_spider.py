import scrapy

class UtmSpider(scrapy.Spider):
    name = "utm"
    allowed_domains = ["utoronto.ca"]
    start_urls = ["https://student.utm.utoronto.ca/timetable/"]

    def parse(self, response):
        root = "https://student.utm.utoronto.ca/timetable/formatCourses2.php"
        timetable_format = root + "?yos=0%%2C1%%2C2%%2C3%%2C4&subjectarea=%s&session=%s"
        sessions = response.css("#sessionSelect option::attr(value)")
        subjects = response.css("#subjectarea option::attr(value)")
        session_values = [session.extract() for session in sessions if
                session.extract() != '0']
        subject_values = [subject.extract() for subject in subjects if
                subject.extract() != '0']
        timetable_urls = [timetable_format % (subject, session) for session in
                session_values for subject in subject_values]
        print(len(timetable_urls))

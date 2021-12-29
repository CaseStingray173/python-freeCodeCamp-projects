from bs4 import BeautifulSoup

file = "basic.html"
with open(file, "r") as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, "lxml")
    course_cards = soup.find_all("div", class_="card")
    for course in course_cards:
        course_names = course.h5.text
        course_prices = course.a.text.split()[-1]
        print(f"{course_names} course costs {course_prices}")

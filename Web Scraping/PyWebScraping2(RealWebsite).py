from bs4 import BeautifulSoup
import requests
import time

print("Enter skills that you are not familiar with")
unfamiliar_skills = input(">")

print(f"Filtering Out: {unfamiliar_skills}")


def find_jobs():
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.find_all("li", class_ = "clearfix job-bx wht-shd-bx")
    for index, job in enumerate(jobs):
        published_date = job.find("span", "sim-posted").span.text
        if "few" in published_date:
            company_name = job.find("h3", class_ = "joblist-comp-name").text.replace(" ", "")
            skills = job.find("span", class_ = "srp-skills").text.replace(" ", "")
            more_info = job.header.h2.a["href"]
            if unfamiliar_skills not in skills:
                with open("job_posts.txt", "a") as f:
                    f.write(f"\n\nCompany Name: {company_name.strip()}")
                    f.write(f"\nRequired Skills: {skills.strip()}")
                    f.write(f"\nMore Info: {more_info}\n")
                print("Job saved to file: job_post.txt")


if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes....")
        time.sleep(time_wait * 60)



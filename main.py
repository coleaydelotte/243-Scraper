import requests as req
from bs4 import BeautifulSoup
import pandas as pd

url = "https://realpython.github.io/fake-jobs/"

response = req.get(url)
soup = BeautifulSoup(response.text, "html.parser")

collective_job_data = []

job_cards = soup.find_all("div", class_="card-content")

for card in job_cards:
    job_data = {}
    if card.find("time"):
        job_data["date"] = card.find("time").text.strip()
    if card.find("h2", class_="title"):
        job_data["title"] = card.find("h2", class_="title").text.strip()
    if card.find("p", class_="location"):
        job_data["location"] = card.find("p", class_="location").text.strip()
    if card.find("h3", class_="subtitle is-6 company"):
        job_data["company"] = card.find("h3", class_="subtitle is-6 company").text.strip()
    collective_job_data.append(job_data)

data = pd.DataFrame(collective_job_data)
data.to_csv("jobs.csv", index=False)

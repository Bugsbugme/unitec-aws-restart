import requests

url = "https://www.tmsandbox.co.nz/home-living/lounge-dining-hall/other/listing-"
idnum = 2149451447
suffix = ".htm"

for i in range(50):
    new_id = idnum + i
    response = requests.get(url + str(new_id) + suffix)
    start_title = response.text.find("<title>") + 7
    end_title = response.text.find("</title>") - 11
    title = response.text[start_title:end_title]
    print(f"{new_id} : {title}")

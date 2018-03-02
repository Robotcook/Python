from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

url = 'https://scrapebook22.appspot.com/'
response = urlopen(url).read()
soup = BeautifulSoup(response)

csv_file = open("email_list.csv", "w")

for link in soup.findAll("a"):
    if link.string == "See full profile":
        link_url = "https://scrapebook22.appspot.com/" + link["href"]
        link_html = urlopen(link_url).read()
        link_soup = BeautifulSoup(link_html)
        name = link_soup.findAll("h1")[1].string
        email = link_soup.find("span", attrs={"class": "email"}).string
        city = link_soup.find("span", attrs={"data-city": True}).string
        csv_file.write(name + "," + email + "," + city + "\n")
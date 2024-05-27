# Internshala Remote Job/Internship Web Scraper

This project is a web scraping script that extracts information about remote jobs and internships from [Internshala](https://internshala.com/internships/). The script uses BeautifulSoup to parse the HTML and retrieve details such as the company name and job location.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have Python 3 installed.
- You have `pip` installed for managing Python packages.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/bitscurrent/web-scrapping.git
   cd web-scrapping

2. Install the required Python packages:

```bash
   pip install -r requirements.txt
```

## Usage
To run the script, execute the following command:

```bash
python index.py
```
This will output the company names and locations of remote jobs/internships listed on Internshala.


## Script Explanation
The script index.py performs the following steps:

#Fetch the Web Page:
The script sends an HTTP GET request to the Internshala internships page and retrieves the HTML content.

```bash
url = "https://internshala.com/internships/"
html_text = requests.get(url).text

```
Parse HTML:
The script uses BeautifulSoup to parse the HTML content.

```bash
soup = BeautifulSoup(html_text, "lxml")
```
Extract Job Information:
The script locates all the job listings and extracts the company name and location.


```bash

jobs=soup.find_all("div",class_="internship_meta")


for job in jobs:

    companys=job.find("div", class_="individual_internship_header")
    
    posted = job.find("div", class_="tags_container_outer").div.div.div.div.text
  

    locations = job.find("div", class_="individual_internship_details")
    location=locations.find("div", id="location_names").span.a.text
    # print(location)

    company = companys.find("div", class_="company")
    profile=company.h3.text.strip()
    company_name = company.find("div", class_="heading_6 company_name").text.strip()


    if "home" in location:

    

        print(f'''
        Company: {company_name}
        Location: {location}
        Posted On: {posted}
        Profile: {profile}

        ''')

```
## License
This project is licensed under the MIT License. See the LICENSE file for more information.

Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code follows the project's coding standards and is well-documented.

Contact
If you have any questions or suggestions, feel free to open an issue or contact me at [dilipboidya.office@gmail.com].

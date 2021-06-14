from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#This is the scraper for the challenges.gov site 
govchal_link = 'https://www.challenge.gov/'

#OPENING UP CONNECTION, GRABBING PAGE
homepg_request = uReq(govchal_link)
homepg_html = homepg_request.read()
homepg_request.close()

#HTML PARSING
page_soup = soup(homepg_html, "html.parser")

#CREATE CSV
filename = "test.csv"
f = open(filename, "w")
headers = "project_name, description, link, sponsors_name, funding, submission_date\n"
f.write(headers)


#FIND ARCHIVE AND MAKE LIST OF YEARS TO LOOP THROUGH
archive_button = page_soup.body.find("ul",{"id":"primary-nav-5"})
archive_accordion = archive_button.findAll("li",{"class":"usa-nav__submenu-item"})
years = [govchal_link]
for li in archive_accordion:
    if li.a["href"][0] == '/':
        years.append("https://www.challenge.gov" + li.a["href"])
#print(years)

#LOOP THROUGH EACH YEAR IN ARCHIVE
for year_link in years:

    #oOPEN CONNECTION TO THAT YEAR
    year_request = uReq(year_link)
    year_html = year_request.read()
    year_request.close()

    #HTML PARSING
    year_soup = soup(year_html, "html.parser")
    #print(year_link)

    #LOOP THROUGH LISTED CHALLENGES FOR EACH YEAR
    #find list of links
    chals = year_soup.findAll("div",{"class":["card__action card__action-block position-absolute", "card__action card__action-block"]})
    for chal in chals:
        #TO DO: for now, skip the ones that go to external links by checking if they start with https, if so, go to next iteration
        chal_link = "https://www.challenge.gov" + chal.a["href"]

        #OPEN CONNECTION TO THAT CHALLENGE'S DETAILS
        chal_request = uReq(chal_link)
        chal_html = chal_request.read()
        chal_request.close()
        
        #HTML PARSING
        chalpg_soup = soup(chal_html, "html.parser")

        #GRAB NAME OF CHALLENGE
        chal_name = chalpg_soup.main.h1.text
        print(chal_name)


        #gGRAB DESCRIPTION
        chal_desc = chalpg_soup.main.find("h3", {"class":["challenge-tagline", "text-primary"]}).text
        #print(chal_desc)

        #GRAB TOTAL CASH PRIZE (in USD. parse only number, no $symbol)
        #QUESTION: should we acctually make this an int or leave it as a string?
        challenge_details = chalpg_soup.find("div", {"class":"text-base-darker"}).text
        #find substring of number from paragraph of info
        line1_end = challenge_details[1:].find("\n")#start at 1 because first char is \n
        index_of_dollar = challenge_details.find("$", 0, line1_end)
        chal_funds = challenge_details[index_of_dollar+1: line1_end+1]
        #take comma out of number if present so it can be converted to integer
        chal_funds = chal_funds.replace(',','')
        #print(chal_funds)

        #GRAB SUBMISSION END
        start = challenge_details.find("Submission End: ")
        time_str = challenge_details[start+16:]#16 is the length of "Submission End:  "
        end = time_str.find(" ")
        chal_end_date = time_str[0:end]
        #print(chal_end_date)

#TO DO: something to streamline the code would be to make a function for parsing strings from challenge details
#       (as done to get the submission date, cash prize, and agencies) so that there is less repeating/similar code.


        #GRAB FEDERAL AND NON-FEDERAL AGENCIES
        #search through paragraph of challenge details to find right substrings
        #federal
        fed_start = challenge_details.find("Partner Agencies | Federal: ")+28 #len = 28
        fed_agencies = challenge_details[fed_start:]
        fed_end = fed_agencies.find("\n")
        fed_agencies = fed_agencies[0:fed_end]
        #non federal
        nfed_start = challenge_details.find("Non-federal: ")+13 #len = 13
        nfed_agencies = challenge_details[nfed_start:]
        nfed_end = nfed_agencies.find("\n")
        nfed_agencies = nfed_agencies[0:nfed_end]
        #concatenate
        chal_agencies = fed_agencies + "; " + nfed_agencies
        chal_agencies = chal_agencies.replace(',', ';')
        #print(chal_agencies)

        #GRAB LINK TO CHALLENGE
        chal_link2 = chal_link
        link_list = chalpg_soup.main.find("div",{"class":"desktop:grid-col-9 usa-prose usa-section challenge-main"}).findAll("a")
        if link_list != []:
            chal_link2 =chal_link2 + "; " + link_list[0]["href"] #decide which number is best to pull.
        print(chal_link2)


        #how_to_enter_h3 = chalpg_soup.find("h3",{"id":"how-to-enter"})
        #print(how_to_enter_h3)
        #nexts = how_to_enter_h3.next_siblings
        #print(nexts)
        #chal_link2 = chal_link
        #print(sib.name)
        #while sib.name != 'h3':
        #    link = sib.find("a")
        #    print(link)
        #    if (link != -1) and (link is not None):
        #        chal_link2 = sib.a["href"]
        #        print(chal_link)
        #        break
        #    sib = sib.next_element


        #how_to_enter_section = chalpg_soup.find("h3",{"id":"how-to-enter"}).next_element.next_element.next_element
        #if how_to_enter_section is not None:
        #    chal_link2 = how_to_enter_section.a['href']
        #else: chal_link2 = "NA"
        #print(chal_link2)

        #TO DO: Grab subject (optimally more specific then "STEM")

        #WRITE DATA FOR THIS CHALLENGE IN CSV
        f.write(chal_name + "," + chal_desc + "," + chal_link2 + "," + chal_agencies + "," + chal_funds + "," + chal_end_date + "\n")
#end both loops

f.close()
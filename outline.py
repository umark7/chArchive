from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#This is the scraper for the challenges.gov site 
#govchal_link = 'https://www.challenge.gov/'

#opening up connection, grabbing the page
#homepg_request = uReq(govchal_link)
#homepg_html = homepg_request.read()
#homepg_request.close()

#html parsing
#page_soup = soup(homepg_html, "html.parser")

#TO DO: loop through years listed on archived challenges
# here is the html pathway
#  header class = "usa-header usa-header--extended"
#  nav class = "usa-nav"
#  ul class = "usa-nav__primary usa-accordion"
#  last li with class "usa-nav__primary-item"
#  ul class "usa-nav__submenu" (id = "primary-nav-5")
#  for each li with class = "usa-nav__submenu-item" open link a href = year_link as done for govchal_link





#TO DO: nested loop: loop through listed challenges on each year
#get link to open and read as done above for govchal_link
# here is the html pathway
#  section class = "usa-section bg=base-lightest"
#  div class = "grid-container"
#  div class = "tablet:gridcol-4 cards"
#  div class = "card"
#  a href = challenge_link





#TO DO: this will be exucuted for each challenge. This is a trial/example for Break the Ice Phase 1

chal_link = 'https://www.challenge.gov/challenge/break-the-ice-phase1/'

chalpg_client = uReq(chal_link)
chalpg_html = chalpg_client.read()
chalpg_client.close()

#html parsing
chalpg_soup = soup(chalpg_html, "html.parser")

#grab name of challenge
chal_name = chalpg_soup.h1.text
print(chal_name)

#grab description
chal_desc = chalpg_soup.find("h3", {"class":"challenge-tagline"}).text
print(chal_desc)

#grab total cash prize (in USD. parse only number, no $symbol)
#QUESTION: should we acctually make this an int or leave it as a string?
challenge_details = chalpg_soup.find("div", {"class":"text-base-darker"}).text
#find substring of number from paragraph of info
line1_end = challenge_details[1:].find("\n")#start at 1 because first char is \n
index_of_dollar = challenge_details.find("$", 0, line1_end)
chal_funds = challenge_details[index_of_dollar+1: line1_end+1]
#take comma out of number if present so it can be converted to integer
chal_funds = chal_funds.replace(',','')
print(chal_funds)

#grab submission end
start = challenge_details.find("Submission End: ")
time_str = challenge_details[start+16:]#16 is the length of "Submission End:  "
end = time_str.find(" ")
chal_end_date = time_str[0:end]
print(chal_end_date)

#TO DO: something to streamline the code would be to make a function for parsing strings from challenge details
#       (as done to get the submission date, cash prize, and agencies) so that there is less repeating/similar code.






#grab federal and non-federal agencies
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
print(chal_agencies)




#grab link to challenge
how_to_enter_section = chalpg_soup.find("h3",{"id":"how-to-enter"}).next_element.next_element.next_element
chal_link2 = how_to_enter_section.a['href']
print(chal_link2)




#TO DO: Grab subject (optimally more specific then "STEM")





#create CSV
filename = "test.csv"
f = open(filename, "w")
headers = "project_name, description, link, sponsors_name, funding, submission_date\n"
f.write(headers)
#Once we have loops the above will need to go above the loop, the below will need to go in the loop and close it after loop
f.write(chal_name + "," + chal_desc + "," + chal_link2 + "," + chal_agencies + "," + chal_funds + "," + chal_end_date + "\n")
f.close()

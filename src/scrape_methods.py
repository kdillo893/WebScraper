import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.ie.options import Options as IEOptions

topdriver = None

def openlinkedin():
    topdriver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    topdriver.implicitly_wait(1)
    topdriver.get("https://linkedin.com/jobs/search")

def linkedin_newpostings(
    driver=None,
    search="Software",
    searchLoc="Greater Chicago Area"):

    toCloseDriver=False
    if (driver==None):
        #instance driver and mention that it needs to close out... otherwise run it.
        driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        toCloseDriver = True
        #go to linkedin job search page        
        driver.get("https://linkedin.com/jobs/search")
        driver.implicitly_wait(1)
    
    time.sleep(1)

    #enter search terms and loc, then click button
    searchbox = None
    searchlocbox = None
    searchbutton = None
    signinbutton=driver.find_element(By.CSS_SELECTOR, "a.nav__button-secondary")

    isLoggedIn = signinbutton == None

    if (signinbutton):
        #search page is different if not logged in...
        searchbox = driver.find_element(By.NAME, "keywords")
        searchlocbox = driver.find_element(By.NAME, "location")
        searchbutton = driver.find_element(By.CSS_SELECTOR, "button.base-search-bar__submit-btn:nth-child(5)")

        # check to make sure the things grabbed match expectation..
        print(searchlocbox.text)
        assert(searchbutton.find_elements(By.CLASS_NAME, "base-search-bar__search-icon"))
    else:
        searchbox = driver.find_element(By.CLASS_NAME, "jobs-search-box__text-input")
        searchlocbox = driver.find_element(By.ID, "jobs-search-box-location-id-ember31")
        searchbutton = driver.find_element(By.CLASS_NAME, "jobs-search-box__submit-button")

    searchbox.click()
    searchbox.send_keys(search)
    time.sleep(1)
    #need to clear the loc box, since it contains "United States"
    searchlocbox.clear()
    time.sleep(0.5)
    searchlocbox.send_keys(searchLoc)
    time.sleep(1)

    searchbutton.click()
    time.sleep(3)

    #have searched, scroll through list of postings...
    #info contained in <ul class="jobs-search-results__list"> itemized by <li>

    #data organized for return:
    #   key = "company"
    #   value = List of tuples 
    #       length is "count of jobs";
    #       tuple content is (jobtitle, dateposted, )
    jobsdict = {}

    #DOING AS IS FOR NOW, will load more later.
    #selecting button to paginate... looks like searching through page needs to be loop
    jobslist = driver.find_element(By.CSS_SELECTOR, ".jobs-search__results-list")
    if (isLoggedIn):
        jobslist = driver.find_element(By.CLASS_NAME, "job-search-results__list")
    jobitems = jobslist.find_elements(By.TAG_NAME, "li")

    print(len(jobitems))

    for job in jobitems:
        #Logged in selectors...
        #"job-card-container__company-link"
        #"job-card-list__title"
        #"job-card-container__metadata-item"

        #not logged in selectors:
        #"base-search-card__title"
        #"base-search-card__subtitle"
        #"job-search-card__location"
        #"base-card__full-link"

        companyname = None
        jobtitle=None
        jobtitleelement=None
        joburl=None
        jobloc=None

        if (isLoggedIn):
            companyname = job.find_element(By.CLASS_NAME, "job-card-container__company-link").text
            jobtitleelement = job.find_element(By.CLASS_NAME, "job-card-list__title")
            jobtitle = jobtitleelement.text
            joburl = jobtitleelement.href
            jobloc = job.find_element(By.CLASS_NAME, "job-card-container__metadata-item").text
        else:
            companyname = job.find_element(By.CLASS_NAME, "base-search-card__subtitle").text
            jobtitle = job.find_element(By.CLASS_NAME, "base-search-card__title").text
            joburl = job.find_element(By.CSS_SELECTOR, "a.base-card__full-link").get_attribute("href")
            jobloc = job.find_element(By.CLASS_NAME, "job-search-card__location").text

        if jobsdict.get(companyname):
            jobsdict[companyname].append((jobtitle, jobloc, joburl))
        else:
            #create a list
            jobsdict[companyname] = [(jobtitle, jobloc, joburl)]


    #to end the method, close out 
    if (toCloseDriver):
        driver.close()

    return jobsdict


jobsgathered = linkedin_newpostings()

print(jobsgathered)
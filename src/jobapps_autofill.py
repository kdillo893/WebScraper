import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# TODO: what the hell was I doing here? Why is this a class with pre-defined values?

class ApplicationEntry():
    """Class containing methods and fields for how to enter data into a job
        application. This will employ Selenium to access a currently opened
        browser tab and fill common fields to hasten the entry process.

        Using this as reference:
        https://learn-automation.com/how-to-execute-selenium-scripts-on-already-opened-browser/

        ...
        Attributes
        -----------
        fname, lname : str
            First and last name
        myemail : str
            Email address, used for lots of things.
        resumefile : str
            Path to resume file; should place this on cloud somewhere...
        chromeDriver : WebDriver
            Selenium Chrome driver instance; persisted across instance

        ....
        Methods
        ---------
        connectbrowser(self)
            tbd
        fillapp(self)
            tbd
    """
    fname = "Kevin"
    lname = "Dillon"
    myemail = "kdillo893@gmail.com"
    resumefile = "/path/to/resume"

    vetstatus = "NOT A VETERAN"
    disabilitystatus = "DECLINE TO ANSWER"
    race = "WHITE"
    ethnicity = "NON HISPANIC"

    chromeDriver = None

    def __init__(self):
        pass

    def connectbrowser(self):
        """Locate browser; this will establish connection to the open browser.
        TODO: THIS CURRENTLY JUST OPENS THE BROWSER"""

        # options to select the browser port for "debugging", driver access..
        # chromeOpts = ChromeOptions
        # chromeOpts.add_experimental_option("debuggerAddress", "localhost:9222")

        # self.chromeDriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
        #                     options=chromeOpts)

        self.chromeDriver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
        pass

    def fillapp_greenhouse(self):
        """
        Filling fields for site \"greenhouse.io\". Can avoid clicking "apply with Linkedin"
        """

        # loads chromedriver... hopefully this actually works as I want.
        self.connectbrowser()
        driver = self.chromeDriver

        # go to the page for the application...

        fnamebox = driver.find_element(By.NAME, "job_application[first_name]")
        lnamebox = driver.find_element(By.NAME, "job_application[last_name]")

        # TODO: finish...

        return

    def fillapp_workday(self):

        self.connectbrowser()
        driver = self.chromeDriver

        # go to page, click apply button... will prompt for login
        # TODO: instead of xpath, make it less hyper-specific
        driver.get("https://factset.wd1.myworkdayjobs.com/en-US/FactSetCareers/job/Software-Engineer---Core-Application-Infrastructure_R11790?source=Linkedin")
        WebDriverWait(driver=driver, timeout=5).until(lambda d: d.find_element(
            By.XPATH, "/html/body/div[5]/div[2]/div[1]/section/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a"))
        applybutton = driver.find_element(
            By.XPATH, "/html/body/div[5]/div[2]/div[1]/section/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a")

        applybutton.click()
        WebDriverWait(driver=driver, timeout=2).until(lambda d: d.find_element(
            By.XPATH, "/html/body/div[6]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/a"))
        afillwresume = driver.find_element(
            By.XPATH, "/html/body/div[6]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/a")
        afillwresume.click()

        # wait until page loads next view...
        # TODO: THIS LOGS IN. If I have no account, this fails...
        # Change to create account by default
        WebDriverWait(driver=driver, timeout=6).until(
            lambda d: d.find_element(By.CSS_SELECTOR, "#input-6"))
        loginemail = driver.find_element(
            By.CSS_SELECTOR, "input[data-automation-id=\"email\"]")
        loginpw = driver.find_element(
            By.CSS_SELECTOR, "input[type=\"password\"][data-automation-id=\"password\"]")
        signinbtn = driver.find_element(
            By.CSS_SELECTOR, "button[data-automation-id=\"signInSubmitButton\"]")

        pw = os.getenv('kdill_wday_pw')
        loginemail.send_keys("kdillo893@gmail.com")
        loginpw.send_keys(pw)

        # move the overlapping div so we can press the button...
        signinbtn.parent.find_elememt(By.CSS_SELECTOR, "div")

        # "autofill with resume" step
        WebDriverWait(driver=driver, timeout=2).until(lambda d: d.find_element(
            By.CSS_SELECTOR, "input[data-automation-id=\"file-upload-input-ref\"]"))
        resumefileinput = driver.find_element(
            By.CSS_SELECTOR, "input[data-automation-id=\"file-upload-input-ref\"]")
        resumefileinput.send_keys(self.resumefile)

        # Hope that works...
        nextbutton = driver.find_element(
            By.CSS_SELECTOR, "button[data-automation-id=\"bottom-navigation-next-button\"]")
        nextbutton.click()

        time.sleep(10)

        self.chromeDriver.close()
        pass

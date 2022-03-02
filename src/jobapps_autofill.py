import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.ie.options import Options as IEOptions

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
    fname="Kevin"; lname="Dillon"
    myemail="kdillo893@gmail.com"
    resumefile="/path/to/resume"

    vetstatus="NOT A VETERAN"
    disabilitystatus="DECLINE TO ANSWER"
    race="WHITE"
    ethnicity="NON HISPANIC"

    chromeDriver=None

    def connectbrowser(self):
        """Locate browser; this will establish connection to the open browser.
        TODO: THIS CURRENTLY JUST OPENS THE BROWSER"""
        
        #options to select the browser port for "debugging", driver access..
        chromeOpts = ChromeOptions
        chromeOpts.add_experimental_option("debuggerAddress", "localhost:9222") 

        self.chromeDriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                            options=chromeOpts)
        return

    def fillapp(self):
        
        return
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re


class Cohort:
    """Gathers data for a given cohort"""
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", False)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def crawl_cohort(self, cohort, weblink):
        """Crawls a cohort and returns potential tournaments"""
        print(f"Processing {cohort} cohort")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(weblink)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "loadMoreSpinner")))
        self.driver.implicitly_wait(5)
        # WebDriverWait(cohortDriver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='elem_loadmore']"))).click()
        tournaments = self.driver.find_elements(By.XPATH, '//ul[@id="searchResultArea"]/li')
        # driver.quit()
        return tournaments


class Tournament:
    """Gathers data for a given tournament"""
    def __init__(self, element, cohort):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", False)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.element = element
        self.date = ""
        self.title = ""
        self.club = ""
        self.distance = ""
        self.closing_date = ""
        self.withdrawal_date = ""
        self.entries = ""
        self.players = []
        self.grade = ""
        self.age = ""
        self.cohort = cohort
        self.link = ""

    def crawl_tournament(self):
        """Crawls a tournament and returns all data"""
        try:
            self.crawl_tournament_overview()
            self.crawl_tournament_detail()
        except NoSuchElementException:
            pass
        tournament_data = {
            'Date': self.date,
            'Title': self.title,
            'Club': self.club,
            'Distance': self.distance,
            'ClosingDate': self.closing_date,
            'WithdrawalDate': self.withdrawal_date,
            'Entries': self.entries,
            'Players': self.players,
            'Grade': self.grade,
            'Age': self.age,
            'Cohort': self.cohort,
            'Link': self.link
        }
        # self.debug_output()
        if self.link:
            return tournament_data

    def crawl_tournament_overview(self):
        """Crawls a tournament and returns data from the original cohort list"""
        self.date = self.element.find_element(By.XPATH,
                                           "./div[contains(@class, 'media')]/div[contains(@class, 'media__wrapper')]/div[contains(@class, 'media__content')]/small[contains(@class, 'media__subheading--muted')]/span/span/time").text
        self.title = self.element.find_element(By.XPATH, "./div/div/div/h4/a").text
        location = self.element.find_element(By.XPATH,
                                               "./div[contains(@class, 'media')]/div[contains(@class, 'media__wrapper')]/div[contains(@class, 'media__content')]/small[contains(@class, 'media__subheading')]/span/span").text
        self.club = re.findall(r'[^(]*', location)[0]
        self.distance = re.findall(r'\([^)]*miles[^)]*\)', location)[0].replace('(', '').replace(')', '')
        self.age = self.cohort.split()[0]
        self.link = self.element.find_element(By.XPATH, "./div/div/a").get_attribute("href")

    def crawl_tournament_detail(self):
        """Crawls a tournament and returns data from the tournament page"""
        self.driver.get(self.link)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
        self.withdrawal_date = self.driver.find_element(By.XPATH,
                                                       "//li[contains(@class, 'list__item is-withdrawal-deadline')]/div[contains(@class, 'list__meta')]/time").text
        self.withdrawal_date = re.findall(r'[^(]*', self.withdrawal_date)[0]
        self.closing_date = self.driver.find_element(By.XPATH,
                                                    "//li[contains(@class, 'list__item is-entry-closed')]/div[contains(@class, 'list__meta')]/time").text
        self.closing_date = re.findall(r'[^(]*', self.closing_date)[0]

        # Get the count of players
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Events')]"))).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(),'{self.cohort}')]"))).click()
        self.entries = len(self.driver.find_elements(By.XPATH,
                                                           "//table/caption[contains(., 'entries')]/../tbody/tr"))

        # Get the player names
        players = self.driver.find_elements(By.XPATH,
                                                           "//table/caption[contains(., 'entries')]/../tbody/tr/td[1]")
        for player in players:
            self.players += [player.text]

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Overview')]"))).click()
        self.grade = self.driver.find_element(By.XPATH, "//*[@id='mediaContentSubinfo']/ul/li[2]/span").text

    def debug_output(self):
        """Additional data for debugging"""
        print("------------")
        print(f"Date: {self.date}")
        print(f"Title: {self.title}")
        print(f"Club: {self.club}")
        print(f"Distance: {self.distance}")
        print(f"ClosingDate: {self.date}")
        print(f"WithdrawalDate: {self.date}")
        print(f"Entries: {self.entries}")
        print(f"Players: {self.players}")
        print(f"Grade: {self.grade}")
        print(f"Age: {self.age}")
        print(f"Cohort: {self.cohort}")
        print(f"Link: {self.link}")
        print("------------")

    def crawler_closed(self):
        """Closes the chromium instance"""
        self.driver.quit()

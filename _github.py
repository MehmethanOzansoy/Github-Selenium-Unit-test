from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from _githubUserInfo import email, username, password
from selenium import webdriver
import requests
import time


class Github:
    browser: WebDriver

    def __init__(self, email, password, username):
        self.name = ""
        self.browser = webdriver.Chrome()
        self.email = email
        self.password = password
        self.username = username
        self.followers = []
        self.following = []
        self.repositories = []

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        email = self.browser.find_element(By.XPATH, '//*[@id="login_field"]')
        password = self.browser.find_element(By.XPATH, '//*[@id="password"]')
        email.send_keys(self.email)
        password.send_keys(self.password)

        time.sleep(2)
        element = self.browser.find_element(By.NAME, "commit")
        element.click()

        time.sleep(5)
        self.browser.maximize_window()

    def getFollowers(self):
        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        time.sleep(2)

        items = self.browser.find_elements(By.CSS_SELECTOR, ".d-table-cell.col-9.v-align-top.pr-3")
        itemising = len(items)
        for i in items:
            self.followers.append(i.find_element(By.CSS_SELECTOR, ".f4.Link--primary").text)

        print(github.followers)
        print(f"Takipçi sayınız" + itemising)
        self.browser.quit()

    def getFollowing(self):
        self.browser.get(f"https://github.com/{self.username}?tab=following")
        time.sleep(2)

        items2 = self.browser.find_elements(By.CSS_SELECTOR, ".d-table-cell.col-9.v-align-top.pr-3")

        for i in items2:
            self.following.append(i.find_element(By.CSS_SELECTOR, ".f4.Link--primary").text)

        print(github.following)
        print(len(self.following))
        self.browser.quit()

    def getRepo(self):
        self.browser.get(f"https://github.com/{self.username}?tab=repositories")
        time.sleep(5)

        repo = self.browser.find_elements(By.CSS_SELECTOR, ".col-10.col-lg-9.d-inline-block")

        for i in repo:
            self.repositories.append(i.find_element(By.CSS_SELECTOR, ".wb-break-all").text)

        print(github.repositories)
        print(len(self.repositories))
        self.browser.quit()

    def getOneRepo(self):
        self.browser.get(f"https://github.com/{self.username}?tab=repositories")
        repo = self.browser.find_element(By.XPATH,"/html/body/div[1]/div[6]/main/div[2]/div/div[2]/turbo-frame/div/div[2]/ul/li[2]/div[1]/div[1]/h3/a")
        repo.click()
        self.browser.save_screenshot("image.png")
        time.sleep(5)

    def dowloandRepo(self):
        self.getOneRepo()
        dowloandrepo = self.browser.find_element(By.CSS_SELECTOR,".d-none.d-md-flex.ml-2")
        dowloandrepo.click()

        dowloand = self.browser.find_element(By.XPATH,'//*[@id="local-panel"]/ul/li[4]/a')
        dowloand.click()
        self.browser.back()
        self.browser.find_element(By.CSS_SELECTOR,".header-search-button.placeholder.input-button.form-control").click()
        for i in range(0, 100):
            self.browser.find_element(By.NAME,"query-builder-test").send_keys(Keys.BACKSPACE)

        self.browser.find_element(By.NAME,"query-builder-test").send_keys(self.username)
        self.browser.find_element(By.CSS_SELECTOR, ".ActionListItem-label.text-normal").click()

        time.sleep(15)


github = Github(email, password, username)

github.signIn()
github.dowloandRepo()

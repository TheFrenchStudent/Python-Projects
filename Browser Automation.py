# Programme utilisant la méthode REST API pour automatiser le processus de connexion sur un site web (dans cet exemple, GitHub) et la vérification du compte.
# Avant d'utiliser ce script, il faut s'assurer que les bons drivers pour le navigateur correspondant soit installés.

from os import link
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://github.com")

signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()

username_box = browser.find_element_by_id("login_field")
username_box.send_keys("UserTEST")
password_box = browser.find_element_by_id("password")
password_box.send_keys("TEST")
password_box.submit()

assert "UserTEST" in browser.page_source

profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")

assert "UserTEST" in link_label

browser.quit()

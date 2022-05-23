#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
import sys

PATH = "C:\Program Files (x86)\chromedriver.exe"

s=Service(PATH)
driver = webdriver.Chrome(service=s)
url = "https://epicurious.com/recipes-menus"
driver.get(url)
time.sleep(2)


vegetarian = driver.find_element(By.LINK_TEXT, "VEGETARIAN")
gluten_free = driver.find_element(By.LINK_TEXT, "GLUTEN-FREE")
quick = driver.find_element(By.LINK_TEXT, "QUICK & EASY")
healthy = driver.find_element(By.LINK_TEXT, "HEALTHY")


def my_ingredients():
    lst = []
    lst = [item for item in input("What's in my fridge?  ").split()]
    return lst


def select_special_filters():
    filter = input("Select any special filters: Quick, Gluten-free, Healthy, Vegetarian  ")
    new_filter = filter.lower()
    if new_filter=="quick" or new_filter=="gluten-free" or new_filter=="healthy" or new_filter=="vegetarian":  #!!!!!!!!!!!!!!!!!!!!!!
        return new_filter
    else:
        print("Not a valid filter name, try again.")
        select_special_filters()


def select_meal():

    meal = input("Select desired meal: Breakfast, Lunch, Dinner, Snack, Sweet  ")
    new_meal = meal.lower()
    if new_meal=="breakfast" or new_meal=="lunch" or new_meal=="dinner" or new_meal=="snack" or new_meal=="sweet":
        return new_meal
    else:
        print("Not a valid name, try again.")
        select_meal()


def click_selected_filter(b):


    if b=="healthy":

        button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/main/div/div[1]/div[1]/div/div[1]/a[2]")
        driver.execute_script("arguments[0].click();", button)


    elif b=="quick":
        button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/main/div/div[1]/div[1]/div/div[1]/a[3]")
        driver.execute_script("arguments[0].click();", button)

    elif b=="gluten-free":
        button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/main/div/div[1]/div[1]/div/div[2]/a[2]")
        driver.execute_script("arguments[0].click();", button)

    elif b=="vegetarian":
        button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/main/div/div[1]/div[1]/div/div[2]/a[3]")
        driver.execute_script("arguments[0].click();", button)
    else:
        pass

def search_selected_meal(the_meal):
    #the_meal = select_meal()
    search_bar = driver.find_element(By.CLASS_NAME, "js-bound")
    search_bar.send_keys(the_meal)
    search_bar.send_keys(Keys.RETURN)


def match_ingredients():
    ing_button = driver.find_element(By.XPATH, "//*[@id='react-app']/span/div[1]/div[1]/div/button")
    driver.execute_script("arguments[0].click();", ing_button)



def main():

    click_selected_filter(select_special_filters())

    search_selected_meal(select_meal())
    match_ingredients()
    time.sleep(5)
    ing_bar = driver.find_element(By.XPATH, "//*[@id='react-app']/span/div[1]/div[1]/div/div[1]/form[1]/fieldset/input")

    for ingredient in my_ingredients():
        ing_bar.send_keys(ingredient)
        ing_bar.send_keys(" ")
    ing_bar.send_keys(Keys.RETURN)







main()

#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#PATH = "C:\Program Files (x86)\chromedriver.exe"
#driver = webdriver.Chrome(PATH)
#driver.get("https://www.epicurious.com/recipes-menus")

#vegetarian = driver.find_element(By.LINK_TEXT, "VEGETARIAN")
#gluten_free = driver.find_element(By.LINK_TEXT, "GLUTEN-FREE")
#quick = driver.find_element(By.LINK_TEXT, "QUICK & EASY")
#healthy = driver.find_element(By.LINK_TEXT, "HEALTHY")
#search_bar = driver.find_element(By.CLASS_NAME, "js-bound")

def my_ingredients():
    ingredients = input("What's in my fridge?  ")
    n_ingredients = []
    for ingredient in ingredients:
        ingredient.lower()
        n_ingredients += ingredient
    return n_ingredients

def select_special_filters():
    filter = input("Select any special filters: Quick, Gluten-free, Healthy, Vegetarian  ")
    new_filter = filter.lower()
    if new_filter=="quick" or new_filter=="gluten-free" or new_filter=="healthy" or new_filter=="vegetarian":  #!!!!!!!!!!!!!!!!!!!!!!
        return new_filter
    else:
        print("Not a valid filter name, try again.")
        select_special_filters()
        return null

def select_meal():
    meal = input("Select desired meal: Breakfast, Lunch, Dinner, Snack, Sweet  ")
    new_meal = meal.lower()
    if new_meal=="breakfast" or new_meal=="lunch" or new_meal=="dinner" or new_meal=="snack" or new_meal=="sweet":
        return new_meal
    else:
        print("Not a valid name, try again.")
        select_meal()
        return null

def click_selected_filter():
    if select_special_filters()=="healthy":
        healthy.click()
    elif select_special_filters()=="quick":
        quick.click()
    elif select_special_filters()=="gluten-free":
        gluten_free.click()
    elif select_special_filters()=="vegetarian":
        vegetarian.click()
    else:
        pass

def search_selected_meal(the_meal):
    the_meal = select_meal()
    search_bar.send_keys(the_meal)
    search_bar.send_keys(Keys.RETURN)


a = my_ingredients()
print(a)

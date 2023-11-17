import bs4
import requests
from bs4 import BeautifulSoup
# Let user input the url
url = "https://www.allrecipes.com/recipe/21261/yummy-sweet-potato-casserole/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text
body = soup.body.text

ingredient_list = []
ing_results = soup.find(id="mntl-structured-ingredients_1-0")
list_of_ing = ing_results.find_all("li")
for list in list_of_ing:
    ingredient_list.append(list.get_text().strip(' \n\r\t'))
print(ingredient_list)

steps = []
steps_results = soup.find(id="recipe__steps_1-0")
directions = steps_results.find_all("p", class_="comp mntl-sc-block mntl-sc-block-html")
for step in directions:
    steps.append(step.get_text().strip(' \n\r\t'))
print(steps)

ing_name = []
ing_quantity = []
ing_measurement = []
tools = []
cook_methods = []
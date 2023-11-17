import bs4
import requests
from bs4 import BeautifulSoup
# Let user input the url
url = "https://www.allrecipes.com/recipe/21261/yummy-sweet-potato-casserole/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text
body = soup.body.text

list_of_ing = []

ing_results = soup.find(id="mntl-structured-ingredients_1-0")
#print(results.prettify())
ingredient_list = ing_results.find_all("ul", class_="mntl-structured-ingredients__list")
for list in ingredient_list:
    tempList = []
    ingredient_items = ing_results.find_all("li", class_="mntl-structured-ingredients__list-item")
    for item in ingredient_list:
        print(len(item))
        item = item.text.strip()
        item = item.replace('\n','')
        tempList.append(item)
    #indiv_ingredients = ingredient.find("li", class_="mntl-structured-ingredients__list-item")
    #quantity_element = ingredient.find("p", span_="data-ingredient-quantity")
    #unit_element = ingredient.find("span", class_="data-ingredient-unit")
    #name_element = ingredient.find("span", class_="data-ingredient-name")
    #print(unit_element)
    #print(name_element)
    list_of_ing.append(tempList)
print(list_of_ing)


# Create top_items as empty list
ingredients = []
steps = []

# Extract and store in top_items according to instructions on the left
products = soup.select('div.list')
for elem in products:
    title = elem.select('h4 > a.title')[0].text
    review_label = elem.select('div.ratings')[0].text
    info = {
        "title": title.strip(),
        "review": review_label.strip()
    }
    ingredients.append(info)

print(ingredients)
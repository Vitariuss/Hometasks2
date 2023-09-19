import re
import requests
from bs4 import BeautifulSoup
from collections import Counter

user_input = input("Введите URL статьи или вставьте скопированный текст: ")

if user_input.startswith("http"):
    url = user_input
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.find(id="mw-content-text").get_text()
else:
    text = user_input

words = re.findall(r'\w+', text.lower())
word_counts = Counter(words)
top_10 = word_counts.most_common(10)

print("Слово", '"{}"'.format(top_10[0][0]), top_10[0][1], "раз")
for i in range(1, len(top_10)):
    print("Слово", '"{}"'.format(top_10[i][0]), top_10[i][1], "раз")
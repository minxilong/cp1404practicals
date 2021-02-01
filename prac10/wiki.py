import wikipedia

text = str(input('Search: '))
wikipedia.search(text, results=10)

try:
    wikipedia.summary(text)
except wikipedia.exceptions.DisambiguationError as e:
    print(e.options)

text_page = wikipedia.page(text)
print('Title: {}'.format(text_page.title))
print('URL: {}'.format(text_page.url))
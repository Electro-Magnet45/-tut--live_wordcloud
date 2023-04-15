import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

text = ''


while True:
    text = text + ' ' + input("Enter text to create a word cloud: ")
    
    wordcloud = WordCloud(background_color="black", stopwords=STOPWORDS).generate(text)
    
    img = wordcloud.to_image()

    plt.figure(figsize=(40,40))
    plt.imshow(img)
    plt.axis("off")
    plt.show()


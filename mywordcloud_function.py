# Import the wordcloud library
from wordcloud import WordCloud

def wordcloud(object_text):
    # Join the different processed titles together.
    long_string = ','.join(list(object_text.values)) # wordcloud of Xiami strings
    # Create a WordCloud object
    wordcloud = WordCloud(background_color="white", max_words=1000, contour_width=3, contour_color='steelblue')
    # Generate a word cloud
    wordcloud.generate(long_string)
    # Visualize the word cloud
    return wordcloud.to_image()
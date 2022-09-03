Web_Scraper project on JetBrains Academy.

URL parser is base on: "https://www.nature.com/nature/articles?sort=PubDate&year=2020" - Articles agregator

Description:

After finishing the project, we know how to send HTTP-requests and process the responses, how to work with BeautifulSoup
and how to use it for parsing the website data.
Also we found out how to make your program save results to a file with the help of Python.

1) The script can take 2 parameters from the user input: the number of pages (an integer) and the type of articles (a string). 
The integer with the number of pages specifies the number of pages on which the program should look for the articles.
2) Creates a directory named Page_N (where N is the page number corresponding to the number input by the user) for each page. 
Searches and collects all articles page by page; filters all the articles by the article type and puts all the articles that are
found on the page with the matched type to the directory Page_N. When the user enters some number, for example, 4, the program 
searches all pages up to that number and creates the respective folders (Folder 1, Folder 2, Folder 3, Folder 4).
3) Saves the contents of each article of the type, that is, the text from the article body without the tags, to a separate 
file named %article_title%.txt. The whitespaces in the name of the article are replaced with underscores and 
punctuation marks in the filename (string.punctuation will be useful for this) are removed. Strips all trailing whitespaces in the article 
body and title. 
For example, the article with the title "Legendary Arecibo telescope will close forever — scientists are reeling" 
would be saved to the file named Legendary_Arecibo_telescope_will_close_forever_scientists_are_reeling.txt.
4) If there's no articles on the page, script creates a folder, but in this case the folder would be empty.

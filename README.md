# Web Scrapper

- ***Author-Saurabh Puri***

**Technology-**
- Python 3.7
- BeautifulSoup Library
  - Beautiful Soup is a Python library for parsing structured data.
  - It allows you to interact with HTML in a similar way to how you would interact with a web page using developer tools.
  - Beautiful Soup exposes a couple of intuitive functions you can use to explore the HTML you received.
  
**Step-1**
- Install Requests Library
  - [pip install requests](https://pypi.org/project/requests/)
- For implementing GUI Interface
  - [pip install tk-tools](https://pypi.org/project/tk-tools/)
- Install BeautfulSoup
  - [pip install beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

**Step-2**
- Beautiful Soup supports the HTML parser included in Python’s standard library, but it also supports a number of third-party Python parsers.
- The pure-Python html5lib parser, which parses HTML the way a web browser does. Depending on your setup, you might install html5lib with one of these commands.
  - [pip install html5lib](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) 

**Step-3**
**Making Soup**
- To parse a document, pass it into the BeautifulSoup constructor. You can pass in a string or an open filehandle:
  ```
  from bs4 import BeautifulSoup

  with open("index.html") as fp:
  soup = BeautifulSoup(fp)

  soup = BeautifulSoup("<html>data</html>")
  ```
  
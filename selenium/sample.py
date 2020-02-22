from selenium import webdriver

text=input("enter")

driver = webdriver.Firefox() 
driver.implicitly_wait(1) 
driver.maximize_window()

indx = text.lower().split().index('youtube') 
query = text.split()[indx + 1:]
print('+'.join(query))    
driver.get("http://www.youtube.com/results?search_query=" + '+'.join(query))

# Web Scraper for Course Pages
Utilises [Scrapy](https://scrapy.org) to scrape data from all course pages found by using [this](https://sac.epfl.ch/English-Master-courses) page as the root of the tree.

For each course, I save  

 * Name  
 * Code  
 * Credits
 * Period

Scraped course data is saved in `scraped_course_data.json`.  
Duplicates, based on course code, are ignored.

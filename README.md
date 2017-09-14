# Web Scraper For Course Pages

Utilises [Scrapy](https://scrapy.org) to scrape data from all course pages found by using [this](https://sac.epfl.ch/English-Master-courses) page as the root of the tree.

With Scrapy installed, run by executing the following terminal command:  
`scrapy runspider course_spider.py -o scraped_course_data.json`

For each course, the following information is saved:

 * Name  
 * Code  
 * Credits
 * Period

Scraped course data is saved in `scraped_course_data.json`.

Use the script `find_courses.py` to sort and explore the scraped data.  
Run with argument `-h` or `--help` to show usage.

import time
import re

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = Options()

options.set_preference("network.http.pipelining", True)
options.set_preference("browser.cache.memory.capacity", 65536)
options.set_preference("browser.display.show_image_placeholders", False)
options.set_preference("network.http.pipelining.maxrequests", 8)
options.set_preference("permissions.default.image", 2)
options.set_preference("geo.prompt.testing", True)
options.set_preference("geo.prompt.testing.allow", False)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))



count_page = 1

while count_page <= 700:

    driver.get('http://showtimebd.com/movie/all_movie/?page='+str(count_page))

    driver.implicitly_wait(5)
    time.sleep(2)

    i = 1
    j = 1

    print(f"Finding movies on page: {count_page}")
    while i <= 60:

        views1 = driver.find_element("xpath", str('/html[1]/body[1]/section[3]/div[1]/div[1]/div[1]/div[1]/ul[1]/div['+str(i)+']/li[1]/figure[1]/figcaption[1]/p[1]')).text



        pattern = r"Views : (\d+)"
        match = re.search(pattern, views1)
        views = match.group(1)

        if int(views) >= 10000:
            name = driver.find_element("xpath",str('/html[1]/body[1]/section[3]/div[1]/div[1]/div[1]/div[1]/ul[1]/div[' + str(i) + ']/li[1]/figure[1]/figcaption[1]/a[1]')).text

            data = f"# Movie Name: {name} \n  Views: {views} \n\n"

            file_path = "MovieList.txt"
            file = open(file_path, "a")
            file.write(data)
            file.close()

            print(data)


            j += 1


        i += 1


    count_page += 1

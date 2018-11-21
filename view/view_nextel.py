from selenium import webdriver


class ViewNextel:
    def google_search(self, json_dictionary):
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        driver.maximize_window()
        locator = "//div/a/h3"
        site = "https://www.google.com"
        search_list = json_dictionary['google-me']
        output_dictonary = dict()
        output_list = list()

        for word in search_list:
            driver.get(site)
            search_field = driver.find_element_by_name("q")
            search_field.clear()
            search_field.send_keys(word)
            search_field.submit()
            searchs = driver.find_elements_by_xpath(locator)
            for search in searchs[slice(3)]:
                print(search.text)
                output_list.append(search.text)
            print("")
            output_dictonary[word] = output_list
            output_list = list()
        print(output_dictonary)
        driver.quit()
        return output_dictonary

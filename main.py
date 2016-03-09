# -*- coding: UTF-8 -*-

import sys
# import requests
# import json
# import time
# from bs4 import BeautifulSoup
from selenium import webdriver
import logging
import time

from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.common.by import By

reload(sys)
sys.setdefaultencoding('utf-8')
driver = webdriver.PhantomJS()


def get_chat_list(ctr):
    # logger = logging.getLogger('logger')
    f = open('./output/' + str(time.localtime().tm_mday) + '.' + str(time.localtime().tm_hour) + '.' + str(time.localtime().tm_min) + '.' + str(time.localtime().tm_sec) + '.txt', 'w')
    # file_handler = logging.FileHandler('./result' + str(time.localtime().tm_mday) + '.' + str(time.localtime().tm_hour) + '.' + str(time.localtime().tm_min) + '.' + str(time.localtime().tm_sec) + '.log')
    # stream_handler = logging.StreamHandler()
    # logger.addHandler(file_handler)
    # logger.addHandler(stream_handler)
    # logger.setLevel(logging.INFO)
    url = 'https://www.youtube.com/live_chat?v=qtScQubZ6Wg'



    driver.get(url)

    comments = []

    try:
        now = str(time.time())
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'comment '))
        )
        comment_list = driver.find_elements_by_class_name('comment ')
        print(str(ctr) + 'got comment list')
        for comment in comment_list:
            try:
                WebDriverWait(driver, 3).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, 'yt-user-name'))
                )
                name = comment.find_element_by_class_name('yt-user-name').text.decode('utf-8').encode('utf-8')
                WebDriverWait(driver, 3).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, 'comment-text'))
                )
                text = comment.find_element_by_class_name('comment-text').text.decode('utf-8').encode('utf-8')
                dic = {'name': name, 'text': text, 'now': now}
                comments.append(dic)

            except Exception, e:
                print(str(ctr) + 'a comment have error', e)
                # logger.info('a comment have error', e)

        print(str(ctr) + 'comments are appended to list')
    except Exception, e:
        print(str(ctr) + 'failed to get comment list', e)
        # logger.info('failed to get comment list', e)


    for chat in comments:
        f.write(chat['name'])
        f.write('\t//seperator//\t')
        f.write(chat['text'])
        f.write('\t//seperator// \t')
        f.write(chat['now'])
        f.write('\n')

    print(str(ctr) + 'wrote to file')
    f.close()
    return comments

def crawl(ctr):
    get_chat_list(ctr)


def main():
    ctr = 0
    while True:
        crawl(ctr)
        print('success ' + str(ctr))
        ctr += 1
    # driver.quit()


main()
driver.quit()

test = 'test'
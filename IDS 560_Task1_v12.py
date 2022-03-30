#!/usr/bin/env python
# coding: utf-8

# In[1]:


# !pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
from selenium.webdriver.common.by import By
import time


# In[2]:


# Use WebDriver to open a Chrome tab and navigate to Instagram login page
chromedriver_path = "C:/Users/mtkta/Desktop/chromedriver_win32/chromedriver.exe"
webdriver = webdriver.Chrome(executable_path = chromedriver_path)
webdriver.get("https://www.instagram.com/accounts/login")
sleep(1)


# In[3]:


# Enter username/password to log in
un, pw = "jewelrymdjewelry","kaviglobal123_"

# Specify which hashtags you want to explore
hashtag_list = ["gold","accessories","earrings","necklace","silver","handmadejewelry",
                "giftideas","bracelet","ring","etsyshop","diamond","diamonds","bracelets","couture","jewelrydesigner",
               "jewelryaddict","fashionjewelry","jewelrydesign","jewelryaddict","fashionjewelry","instajewelry",
               "jewelrygram","gems","gemstone","pendant","gemstones","jewels","jewelry","smallbusiness"]

#Specify comments
comments_list=["Glowing through <3","Simply Iconic, I'm in love!",
               "This is amazing! I can't wait to wear it with @jewelrymdjewelry","An absolute example of perfect beauty<3",
              "This goes so well with @jewelrymdjewelry!",
               "Same to what @jewelrymdjewelry has, this picture has all the inspiration I needed in my life!",
              "This is definitely what @jewelrymdjewelry portrays all the time - beauty in simplicity <3",
              "That is a gorgeous layered look! Many can also be found at @jewelrymdjewelry",
              "A big mood right here <3",
               "Just put in an order but I think I need to order all of these to match @jewelrymdjewelry!"]


limits = {}
limits['follow_limit_per_hour'] = randint(5,10)
limits['unfollow_limit_per_hour'] = randint(3,10)
limits['like_limit_per_hour'] = randint(50,80)
limits['comment_limit_per_hour'] = randint(10,19)
# follow_limit_per_hour = randint(5,10)
# unfollow_limit_per_hour= randint(3,10)
# like_limit_per_hour = randint(80,120)
# comment_limit_per_hour = randint(30,50)
posts_to_reach_per_hashtag = 50


# In[4]:



username = webdriver.find_element_by_name("username")
username.send_keys(un)
password = webdriver.find_element_by_name("password")
password.send_keys(pw)
sleep(1)

# Click login button
login_Xpath = '//*[@id="loginForm"]/div/div[3]/button/div'
webdriver.find_element_by_xpath(login_Xpath).click()
sleep(5)


# In[5]:


# Click "Not Now" on "Save Your Login Info?" popup
not_now = webdriver.find_element_by_css_selector("#react-root > section > main > div > div > div > div > button")
not_now.click()
sleep(randint(2,5))

# Click "Not Now" on popup "Turn on Notifications"
not_now = webdriver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm")
not_now.click()
sleep(randint(2,5))


# In[6]:


# a ='45412'
# float(a.replace(',',''))


# In[22]:


#refresh 
def refresh():
    webdriver.get("https://www.instagram.com/jewelrymdjewelry/")
    sleep(randint(2,5))
    picture=webdriver.find_element_by_css_selector("#react-root > section > main > div > div._2z6nI > article > div > div > div > div.v1Nh3.kIKUG._bz0w > a > div > div._9AhH0")
    picture.click()
    sleep(randint(2,5))
    comment = webdriver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.sH9wk._JgwE > div > form > textarea")
    comment.click()
    sleep(randint(2,5))
    comment_hashtags= '#gold,#accessories,#earrings,#necklace'
    comment = webdriver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.sH9wk._JgwE > div > form > textarea")
    comment.send_keys(comment_hashtags)
    sleep(randint(2,5))
    comment_click = webdriver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.sH9wk._JgwE > div > form > button > div")
    comment_click.click()
    
    
    
#Number of followers function

def num_followers(username):
    url = "https://www.instagram.com/"+username+'/'
    sleep(2)
    webdriver.execute_script("window.open('');")
    webdriver.switch_to.window(webdriver.window_handles[1])
    webdriver.get(url)
    sleep(3)
    num_of_followers = webdriver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(2) > a > div > span').text
    if num_of_followers[-1] == 'k':
        num = float(num_of_followers[:-1].replace(',',''))*1000
    elif num_of_followers[-1] == 'm':
        num = float(num_of_followers[:-1].replace(',',''))*1000000
    else:
        num = float(num_of_followers.replace(',',''))
    sleep(2)
    webdriver.close()
    webdriver.switch_to.window(webdriver.window_handles[0])
    return num


#Follow method and moving to next image
import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')
def unfollow():
    if (time.time()-my_dict_time ['unfollow_timer']) < 3600 and my_dict['unfollowed']<limits['unfollow_limit_per_hour']:
        webdriver.execute_script("window.open('');")
        webdriver.switch_to.window(webdriver.window_handles[1])
        for i in range(5):
            webdriver.get("https://www.instagram.com/jewelrymdjewelry/")
            following_=webdriver.find_element_by_partial_link_text("following")
            following_.click()
            sleep(randint(30,60))
            webdriver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/ul/div/li[1]/div/div[3]/button").click()
            sleep(randint(30,60))
            webdriver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[1]").click()
            sleep(randint(30,60))
            webdriver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[1]/div/div[3]/div/button").click()
            sleep(randint(30,60))
            i+=1
            my_dict['unfollowed']+=1
            my_dict['total_actions']+=1
            my_dict_cum['unfollowed']+=1
            my_dict_cum['total_actions']+=1
            logging.debug('unfollow : {}:total_unfollowed {}: total_actions {}'.format(username, my_dict_cum['unfollowed'],my_dict_cum['total_actions']))
        webdriver.close()
        webdriver.switch_to.window(webdriver.window_handles[0])  
    elif (time.time()-my_dict_time ['unfollow_timer']) > 2*3600:
        webdriver.execute_script("window.open('');")
        webdriver.switch_to.window(webdriver.window_handles[1])
        for i in range(5):
            my_dict_time ['unfollow_timer'] =time.time()
            my_dict['unfollowed'] = 0
            limits['unfollow_limit_per_hour']= randint(3,10)
            webdriver.get("https://www.instagram.com/jewelrymdjewelry/")
            following_=webdriver.find_element_by_partial_link_text("following")
            following_.click()
            sleep(randint(30,60))
            webdriver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/ul/div/li[1]/div/div[3]/button").click()
            sleep(randint(30,60))
            webdriver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[1]").click()
            sleep(randint(30,60))
            webdriver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[1]/div/div[3]/div/button").click()
            sleep(randint(30,60))
            # Increment "unfollowed" counter, add username to new_unfollowed list
            new_unfollowed.append(username)
            i+=1
            my_dict['unfollowed'] += 1
            my_dict['total_actions'] +=1
            my_dict_cum['unfollowed']+=1
            my_dict_cum['total_actions']+=1
            logging.debug('unfollow : {}:total_unfollowed {}: total_actions {}'.format(username, my_dict_cum['unfollowed'],my_dict_cum['total_actions']))
        webdriver.close()
        webdriver.switch_to.window(webdriver.window_handles[0])  
    elif (time.time()-my_dict_time ['unfollow_timer']) > 3600 and my_dict['unfollowed']<limits['unfollow_limit_per_hour']:
        webdriver.execute_script("window.open('');")
        webdriver.switch_to.window(webdriver.window_handles[1])
        for i in range(5):
            my_dict_time ['unfollow_timer'] =time.time()
            my_dict['unfollowed'] = 0
            limits['unfollow_limit_per_hour']= randint(3,10)
            webdriver.get("https://www.instagram.com/jewelrymdjewelry/")
            following_=webdriver.find_element_by_partial_link_text("following")
            following_.click()
            sleep(randint(30,60))
            webdriver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/ul/div/li[1]/div/div[3]/button").click()
            sleep(randint(30,60))
            webdriver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[1]").click()
            sleep(randint(30,60))
            webdriver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[1]/div/div[3]/div/button").click()
            sleep(randint(30,60))
            # Increment "unfollowed" counter, add username to new_unfollowed list
            new_unfollowed.append(username)
            i+=1
            my_dict['unfollowed'] += 1
            my_dict['total_actions'] +=1
            my_dict_cum['unfollowed']+=1
            my_dict_cum['total_actions']+=1
            logging.debug('unfollow : {}:total_unfollowed {}: total_actions {}'.format(username, my_dict_cum['unfollowed'],my_dict_cum['total_actions']))
        webdriver.close()
        webdriver.switch_to.window(webdriver.window_handles[0]) 

def follow():
    follow_ = webdriver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.UE9AK > div > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.bY2yH > button > div")
    username = webdriver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.UE9AK > div > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.e1e1d > div > span > a").text

    if (time.time()-my_dict_time ['follow_timer']) < 3600 and my_dict['followed']<limits['follow_limit_per_hour']:
        # Click follow
        follow_.click()
        sleep(randint(30,60))
        # Increment "followed" counter, add username to new_followed list
        new_followed.append(username)
        my_dict['followed'] += 1
        my_dict['total_actions'] +=1
        my_dict_cum['followed'] += 1
        my_dict_cum['total_actions'] +=1
        logging.debug('follow : {}:total_followed {}: total_actions {}'.format(username, my_dict_cum['followed'],my_dict_cum['total_actions']))
        
    elif (time.time()-my_dict_time ['follow_timer']) > 2*3600:
        my_dict_time ['follow_timer'] =time.time()
        my_dict['followed'] = 0
        limits['follow_limit_per_hour'] = randint(5,10)
        # Click follow
        follow_.click()
        sleep(randint(30,60))
        # Increment "followed" counter, add username to new_followed list
        new_followed.append(username)
        my_dict['followed'] += 1
        my_dict['total_actions'] +=1
        my_dict_cum['followed'] += 1
        my_dict_cum['total_actions'] +=1
        logging.debug('follow : {}:total_followed {}: total_actions {}'.format(username, my_dict_cum['followed'],my_dict_cum['total_actions']))
        
    elif (time.time()-my_dict_time ['follow_timer']) > 3600 and my_dict['followed']<limits['follow_limit_per_hour']:
        my_dict_time ['follow_timer'] =time.time()
        my_dict['followed'] = 0
        limits['follow_limit_per_hour'] = randint(5,10)
        # Click follow
        follow_.click()
        sleep(randint(30,60))
        # Increment "followed" counter, add username to new_followed list
        new_followed.append(username)
        my_dict['followed'] += 1
        my_dict['total_actions'] +=1
        my_dict_cum['followed'] += 1
        my_dict_cum['total_actions'] +=1
        logging.debug('follow : {}:total_followed {}: total_actions {}'.format(username, my_dict_cum['followed'],my_dict_cum['total_actions']))


#like function
def like ():
    if (time.time()-my_dict_time ['like_timer']) < 3600 and my_dict['likes'] <limits['like_limit_per_hour']:
        like = webdriver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button")
        like.click()
        sleep(randint(30,60))
        # Increment "likes" counter
        my_dict['likes'] += 1
        my_dict['total_actions'] +=1
        my_dict_cum['likes'] += 1
        my_dict_cum['total_actions'] +=1
        logging.debug('like: total_likes {}: total_actions {}'.format( my_dict_cum['likes'],my_dict_cum['total_actions']))

    elif (time.time()-my_dict_time ['like_timer']) > 2*3600:
        my_dict_time ['like_timer'] = time.time()
        my_dict['likes'] = 0
        limits['like_limit_per_hour'] = randint(80,120)
        like = webdriver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button")
        like.click()
        sleep(randint(30,60))
        # Increment "likes" counter
        my_dict['likes'] += 1
        my_dict['total_actions'] +=1
        my_dict_cum['likes'] += 1
        my_dict_cum['total_actions'] +=1
        logging.debug('like: total_likes {}: total_actions {}'.format( my_dict_cum['likes'],my_dict_cum['total_actions']))
        
    elif (time.time()-my_dict_time ['like_timer']) > 3600 and my_dict['likes'] <limits['like_limit_per_hour']:
        my_dict_time ['like_timer'] = time.time()
        my_dict['likes'] = 0
        limits['like_limit_per_hour'] = randint(80,120)
        like = webdriver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button")
        like.click()
        sleep(randint(30,60))
        # Increment "likes" counter
        my_dict['likes'] += 1
        my_dict['total_actions'] +=1
        my_dict_cum['likes'] += 1
        my_dict_cum['total_actions'] +=1
        logging.debug('like: total_likes {}: total_actions {}'.format( my_dict_cum['likes'],my_dict_cum['total_actions']))

   
#Comment function
def comment(num_of_followers):
    
    if (time.time()-my_dict_time ['comment_timer']) < 3600 and my_dict['comments'] <limits ['comment_limit_per_hour']:
        comment = webdriver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.sH9wk._JgwE > div > form > textarea")
        comment.click()
        sleep(randint(1,5))
        # Use "randint" to post different comments
        rand_comment = randint(1,len(comments_list))
        if num_of_followers>20000:
            pick_comment = 'If you are interested being a brand ambassador please leave us a message on our page'
        else:
            pick_comment=comments_list[rand_comment]
        comment = webdriver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.sH9wk._JgwE > div > form > textarea")
        comment.send_keys(pick_comment)
        sleep(randint(1,5))
        comment_click = webdriver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.sH9wk._JgwE > div > form > button > div")
        comment_click.click()
        sleep(randint(30,60))
        # Increment "comments" counter
        my_dict['comments'] += 1
        my_dict['total_actions'] +=1
        my_dict_cum['comments'] += 1
        my_dict_cum['total_actions'] +=1        
        logging.debug('comment:total_comments {}: total_actions {}'.format( my_dict_cum['comments'],my_dict_cum['total_actions']))

    elif (time.time()-my_dict_time ['comment_timer']) > 2*3600:
        my_dict['comments'] = 0
        my_dict_time ['comment_timer'] =time.time()
        limits ['comment_limit_per_hour'] = randint(30,50)
        comment = webdriver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.sH9wk._JgwE > div > form > textarea")
        comment.click()
        sleep(randint(1,5))
        # Use "randint" to post different comments
        rand_comment = randint(1,len(comments_list))
        #rand_comment=random.randrange(0,5)
        if num_of_followers>20000:
            pick_comment = 'If you are interested being a brand ambassador please leave us a message on our page'
        else:
            pick_comment=comments_list[rand_comment]
        comment = webdriver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.sH9wk._JgwE > div > form > textarea")
        comment.send_keys(pick_comment)
        sleep(randint(2,4))
        comment_click = webdriver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.sH9wk._JgwE > div > form > button > div")
        comment_click.click()
        sleep(randint(30,60))
        # Increment "comments" counter
        my_dict['comments'] += 1
        my_dict['total_actions'] +=1
        my_dict_cum['comments'] += 1
        my_dict_cum['total_actions'] +=1        
        logging.debug('comment:total_comments {}: total_actions {}'.format( my_dict_cum['comments'],my_dict_cum['total_actions']))
        
    elif (time.time()-my_dict_time ['comment_timer']) > 3600 and my_dict['comments'] < limits ['comment_limit_per_hour']:
        my_dict['comments'] = 0
        my_dict_time ['comment_timer'] =time.time()
        limits ['comment_limit_per_hour'] = randint(30,50)
        comment = webdriver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.sH9wk._JgwE > div > form > textarea")
        comment.click()
        sleep(randint(1,5))
        # Use "randint" to post different comments
        rand_comment = randint(1,len(comments_list))
        #rand_comment=random.randrange(0,5)
        if num_of_followers>20000:
            pick_comment = 'If you are interested being a brand ambassador please leave us a message on our page'
        else:
            pick_comment=comments_list[rand_comment]
        comment = webdriver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.sH9wk._JgwE > div > form > textarea")
        comment.send_keys(pick_comment)
        sleep(randint(1,5))
        comment_click = webdriver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.sH9wk._JgwE > div > form > button > div")
        comment_click.click()
        sleep(randint(30,60))
        # Increment "comments" counter
        my_dict['comments'] += 1
        my_dict['total_actions'] +=1
        my_dict_cum['comments'] += 1
        my_dict_cum['total_actions'] +=1        
        logging.debug('comment:total_comments {}: total_actions {}'.format( my_dict_cum['comments'],my_dict_cum['total_actions']))


# In[ ]:


# Iterate through the hashtags stored in "hashtag_list"

new_followed = []
new_unfollowed=[]
my_dict = {}
my_dict_cum = {}

my_dict['followed'] = 0
my_dict['unfollowed']=0
my_dict['likes'] = 0
my_dict['comments'] = 0
my_dict['total_actions'] = 0
my_dict_time = {}
my_dict_time ['like_timer'] =time.time()
my_dict_time ['follow_timer'] =time.time()
my_dict_time ['unfollow_timer']=time.time()
my_dict_time ['comment_timer'] =time.time()
my_dict_cum['followed'] = 0
my_dict_cum['unfollowed']=0
my_dict_cum['likes'] = 0
my_dict_cum['comments'] = 0
my_dict_cum['total_actions'] = 0

refresh()
   
for hashtag in hashtag_list:
    unfollow() 
   
    
    # Navigate to Instagram "explore/tags" page for current hashtag
    webdriver.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
    sleep(randint(1,2))
    
    # Click on the second thumbnail in the current hashtag's explore page
    first_thumbnail = webdriver.find_element_by_css_selector("#react-root > section > main > article > div.EZdmt > div > div > div:nth-child(1) > div:nth-child(2) > a > div > div._9AhH0")
    first_thumbnail.click()
    sleep(randint(1,2))
    
    try:
        # Iterate through the current hashtag  
        for _ in range(posts_to_reach_per_hashtag):
            try:
                follow_ = webdriver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.UE9AK > div > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.bY2yH > button > div")
                username = webdriver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.UE9AK > div > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.e1e1d > div > span > a").text
                number_of_followers  = num_followers(username)
                sleep(randint(1,3))  
                
                if my_dict['total_actions']>=349 and my_dict['total_actions']<350:
                    unfollow()
                elif my_dict['total_actions']>=350:
                    print('Actions during this session')
                    my_dict.items()
                    print('Total actions')
                    my_dict_cum.items()
                    sleep(86400)
                    my_dict['followed'] = 0
                    my_dict['unfollowed']=0
                    my_dict['likes'] = 0
                    my_dict['comments'] = 0
                    my_dict['total_actions'] = 0
                    my_dict_time ['like_timer'] =time.time()
                    my_dict_time ['follow_timer'] =time.time()
                    my_dict_time ['unfollow_timer']=time.time()
                    my_dict_time ['comment_timer'] =time.time()
                elif follow_.text == "Follow" and username != "jewelrymdjewelry" and number_of_followers >= 100: 

                    follow()
                    sleep(randint(1,3))
                    like()
                    sleep(randint(1,3))                    
                    comment(number_of_followers)
                    sleep(randint(1,3))
#                Click "next" to go to next picture within the same hashtag
                next = webdriver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.Z2Inc._7c9RR > div > div.l8mY4.feth3 > button")
                next.click()
                sleep(randint(2,5))
            except Exception as ex:      
                # Write out what type of Exception
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                print(message)
                driver_len = len(webdriver.window_handles) #fetching the Number of Opened tabs
                if driver_len > 1: # Will execute if more than 1 tabs found.
                    for i in range(driver_len - 1, 0, -1):
                        webdriver.switch_to.window(webdriver.window_handles[i]) #will close the last tab first.
                        webdriver.close() 
                    webdriver.switch_to.window(webdriver.window_handles[0]) # Switching the driver focus to First tab.
#               Click "next" to go to next picture within the same hashtag
                next = webdriver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.Z2Inc._7c9RR > div > div.l8mY4.feth3 > button")
                next.click()
                sleep(randint(2,5))                

                
                
    except Exception as ex:
      
        # Write out what type of Exception
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        driver_len = len(webdriver.window_handles) #fetching the Number of Opened tabs
        if driver_len > 1: # Will execute if more than 1 tabs found.
            for i in range(driver_len - 1, 0, -1):
                webdriver.switch_to.window(webdriver.window_handles[i]) #will close the last tab first.
                webdriver.close() 
            webdriver.switch_to.window(webdriver.window_handles[0]) # Switching the driver focus to First tab.        
        print(message)


# In[8]:


my_dict_cum.items()


# In[ ]:





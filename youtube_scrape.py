from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome()
url = 'https://www.youtube.com/channel/UC8yCpKSfYaMlIP4md3NZ73A/videos'

driver.get(url)

videos = driver.find_elements_by_class_name('style-scope ytd-grid-video-renderer')
video_list = []

for video in videos:
  title = video.find_element_by_xpath('.//*[@id="video-title"]').text
  views = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text
  when = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text

  vid_item = {
    'Title': title,
    'Views': views,
    'Dosted Date': when
  }
  video_list.append(vid_item)

  df = pd.DataFrame(video_list)
  df.to_csv('text.csv', index=False, encoding="utf-8")
# print (df)

driver.quit()

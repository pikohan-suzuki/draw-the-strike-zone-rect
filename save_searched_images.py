import json
import re
from googleapiclient.discovery import build
import pprint
import glob
import urllib.request

def get_image_uri(keyword,num_images):
    service = build("customsearch","v1",developerKey="AIzaSyDBZGKQSQmesq3MlSMuI-spfjOJaHmCHNM")
    start_index = 1
    uri_list = []
    try:
        for i in range(int(num_images//10)):
            res = service.cse().list(
                q=keyword,
                cx="a7f092859a5b4aaf5",
                num=10,
                searchType="image",
                start=start_index
                ).execute()
            start_index += 10

            for image in res['items']:
                uri_list += [image['link']]
    except Exception as e:
        print(e)
        exit(-1)
    return uri_list

def get_next_file_name_cnt():
    files = glob.glob("./saved_images/*")
    if len(files) == 0:
        return 1
    return max([int(re.split("[/|\\\]",path)[-1].split(".")[0]) for path in files]) +1

def save_images(uri_list):
    file_name_cnt = get_next_file_name_cnt()
    for uri in uri_list:
        path = f"./saved_images/{file_name_cnt}.png"
        try:
            img = urllib.request.urlopen(uri).read()
            with open(path,"wb") as f:
                f.write(img)
            file_name_cnt += 1
        except Exception as e:
            print(e)

def main():
    keyword = "高校野球 中継"
    num_images = 20
    
    image_uri_list = get_image_uri(keyword,num_images)
    save_images(image_uri_list)

if __name__ == '__main__':
    main()
import requests
from pprint import pprint
import json
import logging
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

class VKsaveYA:
    def __init__(self, token_vk, user_id, token_ya):
        self.token_vk = token_vk
        self.user_id = user_id
        self.token_ya = token_ya
        logging.info("Class VKsaveYA has been created")

    def get_photo(self, count=5):
        API_BASE_URL = 'https://api.vk.com/method/'
        params = {
            'access_token': self.token_vk,
            'user_id': self.user_id,
            'album_id': 'profile',
            'extended': count,
            'count': count,
            'v': '5.131'
        }
        url = API_BASE_URL + 'photos.get'
        response = requests.get(url, params=params)
        logging.info("The method get_photo has been called")
        return response.json()


    def create_folder_in_ya(self, path="VK_photos"):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {"path": path}
        headers = {"Authorization": f"OAuth {self.token_ya}"}
        response = requests.put(url, params=params, headers=headers)
        if response.status_code == 201:
            logging.info("The folder has been created")
        else:
            logging.info("The folder has not been created")
        return response

    def download_photo_in_ya(self, photo_url, photo_name):
        url_base = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {"Authorization": f"OAuth {self.token_ya}"}
        params = {"url": photo_url, "path": f"VK_photos/{photo_name}.jpg", "overwrite": "true"}
        response = requests.post(url_base, params=params, headers=headers)
        if response.status_code == 202:
            logging.info(f"The photo {photo_name}.jpg has been downloaded")
        else:
            logging.warning(f"The photo {photo_name}.jpg has not been downloaded")
        return response


    def from_vk_to_ya(self, count=5):
        self.create_folder_in_ya()
        photos_dict = self.get_photo(count)
        photos_names = []
        log_info = []
        for i in range(len(photos_dict['response']['items'])):
            photo = photos_dict['response']['items'][i]
            height_max = 0
            for item in photo['sizes']:
                if item['height'] > height_max:
                    height_max = item['height']
                    type_size = item['type']
                    photo_url = item['url']
            if photo['likes']['count'] not in photos_names:
                photos_names.append(photo['likes']['count'])
                photo_name = photo['likes']['count']
            else:
                photo_name = str(photo['date'])
            self.download_photo_in_ya(photo_url, photo_name)
            info = {"file_name": f"{photo_name}.jpg", "size": type_size}
            log_info.append(info)
        self.json_log_file(log_info)
        logging.info("Complete task")
        return log_info

    def json_log_file(self, log_info):
        with open('log.json', 'w', encoding='utf-8') as file:
            json.dump(log_info, file, ensure_ascii=False, indent=4)
        logging.info("The log file has been created")


TOKEN_VK = ""
TOKEN_YA = ''
user_id = 596164780

if __name__ == '__main__':
    vk = VKsaveYA(TOKEN_VK, user_id, TOKEN_YA)
    pprint(vk.from_vk_to_ya())

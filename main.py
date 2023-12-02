import requests
from pprint import pprint

class VKsaveYA:
    API_BASE_URL = 'https://api.vk.com/method/'

    def __init__(self, token_vk, user_id, token_ya):
        self.token_vk = token_vk
        self.user_id = user_id
        self.token_ya = token_ya

    def get_photo(self):
        params = {
            'access_token': self.token_vk,
            'user_id': self.user_id,
            'album_id': 'profile',
            'extended': 5,
            'v': '5.131'
        }
        url = self.API_BASE_URL + 'photos.get'
        response = requests.get(url, params=params)
        return response.json()

    def create_folder_in_ya(self):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {"path": "VK_photos"}
        headers = {"Authorization": f"OAuth {self.token_ya}"}
        response = requests.put(url, params=params, headers=headers)
        return response

    def download_photo_in_ya(self, photo_url, photo_name):
        url_base = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {"Authorization": f"OAuth {self.token_ya}"}
        params = {"url": photo_url, "path": f"VK_photos/{photo_name}.jpg", "overwrite": "true"}
        response = requests.post(url_base, params=params, headers=headers)
        return response


    def from_vk_to_ya(self):
        self.create_folder_in_ya()
        photos_dict = self.get_photo()
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
        return log_info


TOKEN_VK = ""
TOKEN_YA = ''

if __name__ == '__main__':
    vk = VKsaveYA(TOKEN_VK, 596164780, TOKEN_YA)
    pprint(vk.from_vk_to_ya())

import requests
from pprint import pprint
# from urllib.parse import urlencode
#
# APP_id_vk = "51805677"
# OAUTH_BASE_URL = "https://oauth.vk.com/authorize"
# params = {
#     "client_id": APP_id_vk,
#     "redirect_uri": "https://oauth.vk.com/blank.html",
#     "display": "page",
#     "scope": "photos",
#     "response_type": "token",
# }
#
# oaith_url = f"{OAUTH_BASE_URL}?{urlencode(params)}"
# print(oaith_url)


# https://api.vk.com/method/status.get?<PARAMS>
#
class VKsaveYA:
    API_BASE_URL = 'https://api.vk.com/method/'

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def get_photo(self):
        params = {
            'access_token': self.token,
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
        headers = {"Authorization": f"OAuth {TOKEN_YA}"}
        response = requests.put(url, params=params, headers=headers)
        return response

    def upload_photo_in_ya(self, photo_url, photo_name):
        url_base = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {"Authorization": f"OAuth {TOKEN_YA}"}
        params = {"url": photo_url, "path": f"VK_photos/{photo_name}.jpg", "overwrite": "true"}
        response = requests.post(url_base, params=params, headers=headers)
        return response


if __name__ == '__main__':
    vk = VKsaveYA(TOKEN_VK, 596164780)
    pprint(vk.get_photo())
    pprint(vk.create_folder_in_ya())
    pprint(vk.upload_photo_in_ya("https://sun9-80.userapi.com/impg/jWrKpsLGLEMpbqsbEXHhJwfLHPsug8I9aQB1zg/cxOBk0sgvxs.jpg?size=1024x1536&quality=95&sign=2297893f72c4a9637f4bf58a5c8143bd&c_uniq_tag=rVlJgCS2yhEXyisRfxn6WFbgoVinDL5WwqYuRg4hZt4&type=album", '0'))


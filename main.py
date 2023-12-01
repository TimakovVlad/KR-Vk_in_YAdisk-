import requests
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
            'photo_sizes': 1,
            'extended': 1,
            'count': 5,
            'v': '5.131'
        }
        url = self.API_BASE_URL + 'photos.get'
        response = requests.get(url, params=params)
        return response.json()


if __name__ == '__main__':
    vk = VKsaveYA(TOKEN, 596164780)
    print(vk.get_photo())


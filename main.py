APP_id_vk = "51805499"
import requests

class VK:

   def __init__(self, access_token, user_id, version='5.131'):
       self.token = access_token
       self.id = user_id
       self.version = version
       self.params = {'access_token': self.token, 'v': self.version}

   def users_info(self):
       url = 'https://api.vk.com/method/users.get'
       params = {'user_ids': self.id}
       response = requests.get(url, params={**self.params, **params})
       return response.json()


access_token = 'vk1.a.CzjNbXQvmfzUWHCsC08po8b7MDCSy7DJnta5VqHhjGD7Cr48BqDL47dSIf37VPqssEzT6aYfqT7yMxn8DloK5hq3Agfl0e4NWZUBEPNfRyw2YqPCzRYMOHLbVhBTOmADWdsiwQYLc05NeUlcjLGNim-K-JvK4boTEwmUEHlpVqMdfZBXtHT6tmHq4v0ZbW96QV6sDqzLZK4uV2-uMIQVAQ'
user_id = '171121029'
vk = VK(access_token, user_id)
print(vk.users_info())


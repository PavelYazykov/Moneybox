import requests


class HttpMethods:

    @staticmethod
    def get(url, access_token):
        headers = {"Content-Type": "application/json",
                   "Authorization": f"Bearer {access_token}"}
        result = requests.get(url, headers=headers)
        return result

    @staticmethod
    def post(url, body, access_token):
        headers = {"Content-Type": "application/json",
                   "Authorization": f"Bearer {access_token}"}
        result = requests.post(url, json=body, headers=headers)
        return result

    @staticmethod
    def patch(url, body, access_token):
        headers = {"Content-Type": "application/json",
                   "Authorization": f"Bearer {access_token}"}
        result = requests.patch(url, json=body, headers=headers)
        return result

    @staticmethod
    def delete(url, access_token):
        headers = {"Content-Type": "application/json",
                   "Authorization": f"Bearer {access_token}"}
        result = requests.delete(url, headers=headers)
        return result

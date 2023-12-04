import requests

def download_file(url, destination):
    """
    # TODO Add documentation

    :param url:
    :param destination:
    :return:
    """
    response = requests.get(url)
    if response.status_code == 200:
        with open(destination, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded file to {destination}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
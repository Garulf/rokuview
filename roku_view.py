import requests
from requests.auth import HTTPDigestAuth
import argparse

def grab_screenshot(host, username, password):
    url = 'http://{}/plugin_inspect'.format(host)
    print('Requesting Screenshot...')
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Authorization': 'Digest username="rokudev", realm="rokudev", uri="/plugin_inspect", qop=auth',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryV8kb0s3dXDW5bAkl',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'http://{}/plugin_inspect'.format(host),
        'Content-Length': '389',
        'Host': host,
        'Origin': 'http://{}'.format(host),
        'Accept-Encoding': 'gzip, deflate'
    }

    data = b'------WebKitFormBoundaryV8kb0s3dXDW5bAkl\r\nContent-Disposition: form-data; name="archive"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundaryV8kb0s3dXDW5bAkl\r\nContent-Disposition: form-data; name="passwd"\r\n\r\n\r\n------WebKitFormBoundaryV8kb0s3dXDW5bAkl\r\nContent-Disposition: form-data; name="mysubmit"\r\n\r\nScreenshot\r\n------WebKitFormBoundaryV8kb0s3dXDW5bAkl--\r\n'

    response = requests.post(url, headers=headers, auth=HTTPDigestAuth(username, password), data=data, verify=False)
    if 'Screenshot ok' in response.text:
        print('...Successful!')
        return True
    else:
        print('...Failed!')
        print(response.text)
    return False


def download_image(host, username, password, path, filename):
    print('Requesting file...')
    url = 'http://{}/pkgs/dev.jpg'.format(host)
    file_path = '{}/{}'.format(
        path, filename
    )
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Authorization': 'Digest username="rokudev", realm="rokudev", uri="/pkgs/dev.jpg", qop=auth',
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    response = requests.get(url, headers=headers, auth=HTTPDigestAuth(username, password), verify=False, stream=True)
    if response.status_code == 200:
        print('File loaded...')
        with open(file_path, 'wb') as f:
            for chunk in response:
                f.write(chunk)
        print('...File downloaded!')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("username")
    parser.add_argument("password")
    parser.add_argument("host")
    parser.add_argument("-p","--file-path", default='./')
    parser.add_argument("--file-name", default='roku_dev.jpg')
    args = parser.parse_args()
    if grab_screenshot(args.host, args.username, args.password):
        download_image(args.host, args.username, args.password, args.file_path, args.file_name)

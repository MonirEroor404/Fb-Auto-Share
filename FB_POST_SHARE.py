#!/usr/bin/python3
#!/coded/by/Monir
# PROJECT - FB POST AUTO SHARE
# https://www.facebook.com/mdmonirhossen62


import os,sys,json,time,requests,random,re

line=(
    45*'-'
    )
def LMNx9_Login():
    os.system(
        "clear"
        );print(
            line
            )
    print(
        "<\\> FB POST AUTO SHARE | CODED BY - Monir"
       );print(
           line
           )
    cookie = input(
        f"(+) ENTER COOKIES : "
        );print(
            line
            )
    try:
        data = requests.post(
            "https://business.facebook.com/business_locations",
            headers = {
                "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
                "referer": "https://www.facebook.com/",
                "host": "business.facebook.com",
                "origin": "https://business.facebook.com",
                "upgrade-insecure-requests": "1",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control": "max-age=0",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "content-type": "text/html; charset=utf-8"
                },
            cookies = {
                "cookie":cookie
                }
            )
        find_token = re.search(
            "(EAAG\w+)",
            data.text
            )
        open(
            "/sdcard/.token.txt", "w"
            ).write(
                find_token.group(1)
                )
        open(
            "/sdcard/.cookie.txt", "w"
            ).write(
                cookie
                )
        print(
            f'(>) LOGIN SUCCESSFUL'
            )
        print(
            line
            );time.sleep(
                2
                );LMNx9_Share()
    except requests.exceptions.ConnectionError:
        print(
            f"(!!) Internet Connection Error !"
            )
        print(
            line
            );sys.exit()
    except:
        try:
            os.system(
                "rm /sdcard/.token.txt"
                )
            os.system(
                "rm /sdcard/.cookie.txt"
                )
        except:
            pass
        print(
            '(!!) INVALID COOKIES - Try Again... '
            )
        print(
            line
            );time.sleep(
                2
                );LMNx9_Login()
    
def LMNx9_Share():
    try:
        token = open(
            "/sdcard/.token.txt","r"
            ).read()
        cok = open(
            "/sdcard/.cookie.txt","r"
            ).read()
        cookie = {
            "cookie":cok
            }
        ip = requests.get(
            "https://api.ipify.org"
            ).text
        nama = requests.post(
            f"https://graph.facebook.com/me?fields=name&access_token={token}",
            cookies=cookie
            ).json(
                )["name"]
        id = requests.get(
            "https://graph.facebook.com/me/?access_token=%s"%(
                token
                ),
            cookies={
                "cookie":cok
                }
            ).json(
                )["id"]
    except requests.exceptions.ConnectionError:
        print(
            f"(!!) Internet Connection Error !"
            )
        print(
            line
            );sys.exit()
    except:
        try:
            os.system(
                "rm /sdcard/.token.txt"
                )
            os.system(
                "rm /sdcard/.cookie.txt"
                )
        except:
            pass
        print(
            "(!!) COOKIES EXPIRED - Login Again..."
            )
        print(
            line
            );time.sleep(
                2
                );LMNx9_Login()
    LMNx9()

def LMNx9():
    os.system(
        'clear'
        );print(
            line
            )
    print(
        "(/) YOUR NAME : {nama}\n(/) YOUR UID  : {id}\n(/) YOUR IP   : {ip}"
        );print(
            line
            )
    link = input(
        f"(+) ENTER POST LINK : "
        );print(
            line
            )
    limit = int(
        input(
            f"(?) ENTER SHARE LIMIT : "
            )
        );print(
            line
            )
    try:
        header = {
            "authority":"graph.facebook.com",
            "cache-control":"max-age=0",
            "sec-ch-ua-mobile":"?0",
            "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1"
            }
        for x in range(limit):
            post = requests.post(
                f"https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={token}",
                headers=header,
                cookies=cookie
                ).text
            data = json.loads(
                post
                )
            if "id" in post:
                print(
                    f"(>) Successfully Shared - [{id}]"
                    );print(
                        line
                        )
            else:
                print(
                    f"(>) Failed To Share !"
                    );print(
                        line
                        )
        print(
            '\n(/) LMNx9 Post Share Completed !'
            )
        sys.exit()
    except requests.exceptions.ConnectionError:
        print(
            f"(!!) Internet Connection Error !"
            )
        print(
            line
            );sys.exit()

if __name__ in '__main__':
    try:
        os.system(
            "rm /sdcard/.token.txt"
            )
        os.system(
            "rm /sdcard/.cookie.txt"
            )
    except:
        pass
    LMNx9_Login()
    
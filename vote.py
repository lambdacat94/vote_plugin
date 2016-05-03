import urllib.request
import urllib.parse
import http.cookiejar
import json

app_version = "1.1.2"
appid = "7"
appkey = "EJBtjEmlMKrLvgg6luXdQoDbIcycHjKc"
device_token = "0ae7bfcdfecf320a32915487c8ce3f05"

username_base = "auto_w83"
email_prefix_base = 'to_young_w83'
email_postfix_base = '@f8at.com'


password = "iamsosorry"
_type = "m2o"
version = "1.1.2"

register_url = 'http://mobile.jlntv.cn/jlntv/m_register.php'
vote_url = 'http://mobile.jlntv.cn/jlntv/vote.php'


def vote(register_username, register_password, register_email, man_id):
    cookie = http.cookiejar.CookieJar()
    processor = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(processor)

    register_post_dict = {
        'appid' : appid,
        'appkey' : appkey,
        'device_token' : device_token,
        '_member_id' : '',
        'version' : version,
        'app_version' : app_version,
        'member_name' : register_username,
        'email' : register_email,
        'password' : register_password
    }

    register_post_data = urllib.parse.urlencode(register_post_dict).encode()

    register_op = opener.open(register_url, register_post_data)

    register_json = register_op.read().decode()
#    print(register_json)
    register_json_dict = json.loads(register_json)

#    print(register_json_dict)
    _access_token = register_json_dict[0]['access_token']
#    print(_access_token)
    
    _member_id = str(register_json_dict[0]['member_id'])
    

    vote_post_dict = {
        'appid' : appid,
        'appkey' : appkey,
        'access_token' : _access_token,
        'device_token' : device_token,
        '_member_id' : _member_id,
        'version' : version,
        'app_version' : app_version,
        'id' : '12',
        'option_id' : man_id,
        'access_token' : _access_token
    }
    
    vote_post_data = urllib.parse.urlencode(vote_post_dict).encode()
    vote_op = opener.open(vote_url, vote_post_data)
    vote_json = vote_op.read().decode()
    vote_json_dict = json.loads(vote_json)

#    print(vote_json)



for i in range(1, 200):
    print('The %dth vote' % i)

    main_username = username_base + str(i)
    main_email = email_prefix_base + str(i) + email_postfix_base
    print(main_username)
    print(main_email)
    try:
        vote(main_username, "asdasd", main_email, '83')
    except:
        print('=============================================')
        print('Occured an error')
        continue

print('=================================================')
print('========================OK=======================')
print('=================================================')

















    

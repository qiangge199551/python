data = '''Accept:application/json, text/javascript, */*; q=0.01
Accept-Encoding:gzip, deflate
Accept-Language:zh-CN,zh;q=0.9
Connection:keep-alive
Content-Length:344
Content-Type:application/x-www-form-urlencoded; charset=UTF-8
Cookie:JSESSIONID=0000Oc5IOs8obMezHrfdMWuT2No:-1; Hm_lvt_1ab04bcaf4dd6e15edf78188f2d6a32c=1521518240,1521597766,1521598305,1521598324; Hm_lpvt_1ab04bcaf4dd6e15edf78188f2d6a32c=1521598324
DNT:1
Host:cx.cnca.cn
Origin:http://cx.cnca.cn
Referer:http://cx.cnca.cn/rjwcx/web/cert/publicCert.do?progId=10&title=%E8%AE%A4%E8%AF%81%E7%BB%93%E6%9E%9C%0A%09%20%20%20%20%20%20%20%20
User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36
X-Requested-With:XMLHttpRequest'''
for item in data.split('\n'):
	print('\'' + item.split(':')[0] + '\'' + ': ' + '\''+ ''.join(item.split(':')[1: ]) + '\'' + ',')



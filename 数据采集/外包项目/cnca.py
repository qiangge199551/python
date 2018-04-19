import requests
import json


def get_org_list(session, headers):
	#搞定验证码
	code = session.get('http://cx.cnca.cn/rjwcx/checkCode/rand.do?d=1521511949862.jpg').content
	with open('code.jpg', 'wb') as f:
		f.write(code)
	orgName = input('Please input the orgName!!\n')
	checkCode = input('Please input the check code!!\n')
	#获得组织列表
	data = {
		'certNumber': '',
		'orgName': orgName,
		'queryType': 'public',
		'checkCode': checkCode,
	}
	params ={
		'progId': '10'
	}
	url = 'http://cx.cnca.cn/rjwcx/web/cert/queryOrg.do?progId=10'
	response = session.post(url, headers=headers, data=data)
	# # print(response.url)
	# print(response.text, '\n----------------------------------------------\n')
	# print(json.loads(response.text)['data'], '\n00000000000000000000000000000000000000000\n')
	for org_detial in json.loads(response.text)['data']:
		# print(org_detial, '\n\n++++++++++++++++++++++++++++++++++++++++++\n')
		yield org_detial


def get_cert_list(session, headers, org_detial):
	params = {
	'progId': '10',
	}
	data ={
		'orgName':org_detial['orgName'] ,
		'orgCode': org_detial['orgCode'],
		'method': 'queryCertByOrg',
		'needCheck': 'false',
		'checkC': org_detial['checkC'],
		'randomCheckCode': org_detial['randomCheckCode'],
		'queryType': 'public',
		'page': '1',
		'rows': '10',
		'checkCode': '',
	}
	url = 'http://cx.cnca.cn/rjwcx/web/cert/list.do?progId=10'
	response = session.post(url, headers=headers, data=data, params=params)
	# print(response.text, '\n\n\n\n===========================================')
	for rows in json.loads(response.text)['rows']:
		# print(rows, '\n\n||||||||||||||||||||||||||||||||||||||||||||||\n\n')
		yield dict(rows)


def get_cert_detial(session, rows):
	# http://cx.cnca.cn/rjwcx/web/cert/index.do?url=web/cert/show.do%3FrzjgId=CNCA-R-2002-001%26certNo=00114Q26950R7L%2F3502%26checkC=-1535837572
	# http://cx.cnca.cn/rjwcx/web/cert/show.do?rzjgId=CNCA-R-2002-001&certNo=00114Q26950R7L/3502&checkC=-1535837572
	url = 'http://cx.cnca.cn/rjwcx/web/cert/show.do?rzjgId={0}&certNo={1}&checkC={2}'.format(rows['rzjgId'], rows['certNumber'], rows['checkC'])
	print(url)
	response = session.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'},)
	# print(response.text, '\n\n////////////////////////////\n\n')
	


def main():
	url = 'http://cx.cnca.cn/rjwcx/web/cert/index.do?progId=1212'
	headers = {
		'Connection': 'keep-alive',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'DNT': '1',
		'Host': 'cx.cnca.cn',
		'Origin': 'http//cx.cnca.cn',
		'Referer': 'http//cx.cnca.cn/rjwcx/web/cert/publicCert.do?progId=10&title=%E8%AE%A4%E8%AF%81%E7%BB%93%E6%9E%9C%0A%09%20%20%20%20%20%20%20%20',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
		'X-Requested-With': 'XMLHttpRequest',
	}
	session = requests.Session()
	for org_detial in get_org_list(session, headers):
		for rows in get_cert_list(session, headers, org_detial):
			get_cert_detial(session, rows)


if __name__ == '__main__':
	main()
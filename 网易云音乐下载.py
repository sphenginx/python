# 网易云音乐批量图片下载
# Python3.6.5

import requests
import urllib 

# 浏览器打开有100条数据， requests获取只有1条数据！！！, 设置headers就可以了
musicHeader = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive',
	'Cookie': '_ntes_nnid=4d0ec1292639877c381dc60a5dd872d3,1524456154156; _ntes_nuid=4d0ec1292639877c381dc60a5dd872d3; usertrack=ezq0pVrkFEOn1grnIxxOAg==; _ga=GA1.2.1165107714.1524896839; vjuids=365440b3f.16347b1f899.0.18f11cb7a1993; s_n_f_l_n3=67160b6c2889824f1525916236011; City=010; Province=010; mp_MA-A924-182E1997E62F_hubble=%7B%22sessionReferrer%22%3A%20%22http%3A%2F%2Fxf.house.163.com%2Fbj%2FBcJO.html%22%2C%22updatedTime%22%3A%201525916277633%2C%22sessionStartTime%22%3A%201525916277630%2C%22deviceUdid%22%3A%20%22e8521614-466d-4f0d-96ba-faa86cd0dbe5%22%2C%22persistedTime%22%3A%201525916239021%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22da_screen%22%2C%22time%22%3A%201525916277633%7D%2C%22sessionUuid%22%3A%20%2236709863-a6a9-4551-bd07-fba969f75fe2%22%7D; HOUSE_USER_MEMBER_SESSION_ID=HOUSE_USER_MEMBER_SESSION_ID-2be2732670ff4dfb167ff6671307bd829b43f6dd-0968-4cac-8368-dae952c2595b; _antanalysis_s_id=1525916277908; __e_=1526261527709; _iuqxldmzr_=32; __utmc=94650624; __utmz=94650624.1526876866.1.1.utmcsr=yangbingdong.com|utmccn=(referral)|utmcmd=referral|utmcct=/2017/build-blog-hexo-base/; vjlast=1525916236.1529549525.11; WM_TID=EQwe3gTZCrQUj%2FQJCgVFNICSwCzBR5Ga; __utma=94650624.1165107714.1524896839.1531206003.1531211878.4; starttime=; mail_login_way=normal; NTES_SESS=HkwdB75NSRpPJTKRi7VP5RH6MuKL0rWVaFouiDuECBm0PdtC9PJt3aKarba5EG7T2jwEwDrl4iOGeaBaJkTLhTOR5J7D6kdLSwhzDpRfpVqLIoGJajVK_JzbD4c9OP7eiytuhXd16TH5cIVWJPPKKJH_6Py4CDjS4kbMlKDl.CG.nLepKJgysi2M6; S_INFO=1531469648|0|3&40##|sphenginx; P_INFO=sphenginx@163.com|1531469648|0|mail163|11&17|null&null&null#shd&370200#10#0#0|&0||sphenginx@163.com; nts_mail_user=sphenginx@163.com:-1:1; df=mail163_letter; mail_psc_fingerprint=43173a30ac53ac7370f6313d6a6751c0; JSESSIONID-WYYY=WgbQZ3lEN%5CHB8c4VdVzz7TzW1T%2FRnYXKFPchc3JvbwyzpS5morX1JkTw79ga3O35gfGAFgmEsXtv%2Bo35D9Wbc%5Czcsow0BAypJkxQFUq52%2FZ6uYpsSC3WJzeTwGzHogSCbgXQPcc%2FM57k3erRfSfR5SGpTa3mvbvHxogzXUcCa%2FX4ZpIk%3A1531471453068; playliststatus=visible; MUSIC_EMAIL_U=eb2a90746c06cc8d06a1e3dc20ff2ab1f0acecfc4e35abd85eef61d2148effcfcf865e4ad974f1736dea581fc4fc7e54b20814e7e0c61d0e8bafcdfe5ad2b092; ne_analysis_trace_id=1531470695440; NTES_CMT_USER_INFO=259792401%7C%E6%9C%89%E6%80%81%E5%BA%A6%E7%BD%91%E5%8F%8B0fv1Uh%7C%7Cfalse%7Cc3BoZW5naW54QDE2My5jb20%3D; vinfo_n_f_l_n3=67160b6c2889824f.1.0.1525916236010.0.1531471263085; __f_=1532425119283',
	'Host': 'music.163.com',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}

#榜单歌曲批量下载
#r = requests.get('http://music.163.com/api/playlist/detail?id=2884035') #网易原创歌曲榜 
#r = requests.get('http://music.163.com/api/playlist/detail?id=19723756') #云音乐飙升榜
#r = requests.get('http://music.163.com/api/playlist/detail?id=3778678')#云音乐热歌榜
#r = requests.get('http://music.163.com/api/playlist/detail?id=3779629') #云音乐新歌榜

#歌单歌曲批量下载
r = requests.get('http://music.163.com/api/playlist/detail?id=123415635', headers = musicHeader) #云音乐歌单——【华语】中国风的韵律，中国人的印记+
#r = requests.get('http://music.163.com/api/playlist/detail?id=122732380') #云音乐歌单——那不是爱，只是寂寞说的谎
arr = r.json()['result']['tracks'] #+共有100首歌+
#print(r.json())

#把结果写入数据库
fl = open('163music.txt', 'w')
fl.write(str(r.json()))
fl.close()

for i in range(10):
	#输入要下载音乐的数量，1到100。+
	name = str(i+1) + '_' +arr[i]['name'] + '.jpg'
	link = arr[i]['album']['picUrl']
	#需要提前要创建文件夹
	urllib.request.urlretrieve(link, '网易云音乐\\' + name) 
	print(name + ' 下载完成')
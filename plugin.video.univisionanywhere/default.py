import urllib
import httplib
import re
import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin


#Settings
uaUser = "tester" #<----- univision anywhere username
uaPass = "123456" #<----- univision anywhere password


def csrfTokenAndCookie():
	params = urllib.urlencode({})
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	conn = httplib.HTTPConnection("tv.univision.mn")
	conn.request("GET", "/wsc.php/login?returnurl=@tv_home", params, headers)
	response = conn.getresponse()
	data = response.read()
	conn.close()
	
	return re.search(r"(#?[0-9A-Fa-f]{32})", data).group(0),response.msg['Set-Cookie'].split(';')[0]

csrfToken,Cookie = csrfTokenAndCookie()
print csrfToken
print Cookie


def tryToLoginUnivision():
	params = urllib.urlencode({	'signin[_csrf_token]' : csrfToken,
								'signin[username]' : uaUser,
								'signin[password]' : uaPass,
								'submit':''})
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain","Referer":"http://tv.univision.mn/wsc.php/login?returnurl=@tv_home","Cookie":Cookie}
	conn = httplib.HTTPConnection("tv.univision.mn")
	conn.request("POST", "/wsc.php/login?returnurl=@tv_home", params, headers)
	response = conn.getresponse()
	print response.status, response.reason
	data = response.read()
	print response.msg['Set-Cookie']
	conn.close()
	return response.msg['Set-Cookie'].split(';')[0];
Cookie = tryToLoginUnivision()

def tryToParseTvToken():
	params = urllib.urlencode({})
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain","Referer":"http://tv.univision.mn/","Cookie":Cookie}
	conn = httplib.HTTPConnection("tv.univision.mn")
	conn.request("GET", "/24/watch", params, headers)
	response = conn.getresponse()
	data = response.read()
	conn.close()
	return re.search(r".m3u8\?(#?[0-9A-Fa-f]{32})", data).group(0)

tvToken = tryToParseTvToken()



xbmcplugin.setContent(int(sys.argv[1]),'movies')
#MN
linkMN = 'http://202.70.32.50/hls/_definst_/tv_mid/smil:mnb.smil/playlist'+tvToken
liMN = xbmcgui.ListItem(label='MN', path=linkMN)
liMN.setInfo(type='Video', infoLabels={ "Title": 'MN' })
liMN.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=linkMN, listitem=liMN, isFolder=False)

#MN2
linkMN2 = 'http://202.70.32.50/hls/_definst_/tv_mid/smil:mnb_2.smil/playlist'+tvToken
liMN2 = xbmcgui.ListItem(label='MN 2', path=linkMN2)
liMN2.setInfo(type='Video', infoLabels={ "Title": 'MN 2' })
liMN2.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=linkMN2, listitem=liMN2, isFolder=False)

#EDU
linkEDU = 'http://202.70.32.50/hls/_definst_/tv_mid/smil:edu.smil/playlist'+tvToken
liEDU = xbmcgui.ListItem(label='EDU', path=linkEDU)
liEDU.setInfo(type='Video', infoLabels={ "Title": 'EDU' })
liEDU.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=linkEDU, listitem=liEDU, isFolder=False)

#UBS
linkUBS = 'http://202.70.32.50/hls/_definst_/tv_mid/smil:ubs.smil/playlist'+tvToken
liUBS = xbmcgui.ListItem(label='UBS', path=linkUBS)
liUBS.setInfo(type='Video', infoLabels={ "Title": 'UBS' })
liUBS.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=linkUBS, listitem=liUBS, isFolder=False)

#MN25
linkMN25 = 'http://202.70.32.50/hls/_definst_/tv_mid/smil:mn25.smil/playlist'+tvToken
liMN25 = xbmcgui.ListItem(label='MN25', path=linkMN25)
liMN25.setInfo(type='Video', infoLabels={ "Title": 'MN25' })
liMN25.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=linkMN25, listitem=liMN25, isFolder=False)

#NTV
linkNTV = 'http://202.70.32.50/hls/_definst_/tv_mid/smil:ntv.smil/playlist'+tvToken
liNTV = xbmcgui.ListItem(label='NTV', path=linkNTV)
liNTV.setInfo(type='Video', infoLabels={ "Title": 'NTV' })
liNTV.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=linkNTV, listitem=liNTV, isFolder=False)

#TV5
linkTV5 = 'http://202.70.32.50/hls/_definst_/tv_mid/smil:tv5.smil/playlist'+tvToken
liTV5 = xbmcgui.ListItem(label='TV5', path=linkTV5)
liTV5.setInfo(type='Video', infoLabels={ "Title": 'TV5' })
liTV5.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=linkTV5, listitem=liTV5, isFolder=False)


#Eagle
linkEAGLE = 'http://202.70.32.50/hls/_definst_/tv_mid/smil:eagle.smil/playlist'+tvToken
liEAGLE = xbmcgui.ListItem(label='Eagle', path=linkEAGLE)
liEAGLE.setInfo(type='Video', infoLabels={ "Title": 'Eagle' })
liEAGLE.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=linkEAGLE, listitem=liEAGLE, isFolder=False)

#SBN
linkSBN = 'http://202.70.32.50/hls/_definst_/tv_mid/smil:sbn.smil/playlist'+tvToken
liSBN = xbmcgui.ListItem(label='SBN', path=linkSBN)
liSBN.setInfo(type='Video', infoLabels={ "Title": 'SBN' })
liSBN.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=linkSBN, listitem=liSBN, isFolder=False)

#TV9
linkTV9 = 'http://202.70.32.50/hls/_definst_/tv_mid/smil:tv5.smil/playlist'+tvToken
liTV9 = xbmcgui.ListItem(label='TV9', path=linkTV9)
liTV9.setInfo(type='Video', infoLabels={ "Title": 'TV9' })
liTV9.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=linkTV9, listitem=liTV9, isFolder=False)

#SPORTBOX
linkSPORTBOX = 'http://202.70.32.50/hls/_definst_/tv_mid/smil:sportbox.smil/playlist'+tvToken
liSPORTBOX = xbmcgui.ListItem(label='SportBox', path=linkSPORTBOX)
liSPORTBOX.setInfo(type='Video', infoLabels={ "Title": 'SportBox' })
liSPORTBOX.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=linkSPORTBOX, listitem=liSPORTBOX, isFolder=False)

#MONGOLHD
linkMONGOLHD = 'http://202.70.32.50/hls/_definst_/tv_mid/smil:mongolhd.smil/playlist'+tvToken
liMONGOLHD = xbmcgui.ListItem(label='MongolHD', path=linkMONGOLHD)
liMONGOLHD.setInfo(type='Video', infoLabels={ "Title": 'MongolHD' })
liMONGOLHD.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=linkMONGOLHD, listitem=liMONGOLHD, isFolder=False)

#ROYAL
linkROYAL = 'http://202.70.32.50/hls/_definst_/tv_mid/smil:tv5.smil/playlist'+tvToken
liROYAL = xbmcgui.ListItem(label='Royal', path=linkROYAL)
liROYAL.setInfo(type='Video', infoLabels={ "Title": 'Royal' })
liROYAL.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=linkROYAL, listitem=liROYAL, isFolder=False)

#MNC
linkMNC = 'http://202.70.32.50/hls/_definst_/tv_mid/smil:mnc.smil/playlist'+tvToken
liMNC = xbmcgui.ListItem(label='MNC', path=linkMNC)
liMNC.setInfo(type='Video', infoLabels={ "Title": 'MNC' })
liMNC.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=linkMNC, listitem=liMNC, isFolder=False)

#EHORON
linkEHORON = 'http://202.70.32.50/hls/_definst_/tv_mid/smil:ehoron.smil/playlist'+tvToken
liEHORON = xbmcgui.ListItem(label='Eh oron', path=linkEHORON)
liEHORON.setInfo(type='Video', infoLabels={ "Title": 'Eh oron' })
liEHORON.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=linkEHORON, listitem=liEHORON, isFolder=False)

#BLOOMBERG
linkBLOOMBERG = 'http://202.70.32.50/hls/_definst_/tv_mid/smil:bloomberg.smil/playlist'+tvToken
liBLOOMBERG = xbmcgui.ListItem(label='Bloomberg', path=linkBLOOMBERG)
liBLOOMBERG.setInfo(type='Video', infoLabels={ "Title": 'Bloomberg' })
liBLOOMBERG.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=linkBLOOMBERG, listitem=liBLOOMBERG, isFolder=False)

#PARLIAMENT
linkPARLIAMENT = 'http://202.70.32.50/hls/_definst_/tv_mid/smil:parliament.smil/playlist'+tvToken
liPARLIAMENT = xbmcgui.ListItem(label='Parliament', path=linkPARLIAMENT)
liPARLIAMENT.setInfo(type='Video', infoLabels={ "Title": 'Parliament' })
liPARLIAMENT.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=linkPARLIAMENT, listitem=liPARLIAMENT, isFolder=False)

xbmcplugin.endOfDirectory(int(sys.argv[1]))


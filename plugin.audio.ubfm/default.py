import urllib
import httplib
import re
import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin



xbmcplugin.setContent(int(sys.argv[1]),'music')
#100.9
link1009 = 'http://5278fa1a8b76e.streamlock.net/live/1009.stream/playlist.m3u8'
li1009 = xbmcgui.ListItem(label='P3 Radio FM 100.9', path=link1009)
li1009.setInfo(type='Video', infoLabels={ "Title": 'P3 Radio FM 100.9' })
li1009.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=link1009, listitem=li1009, isFolder=False)

#Ikh Mongol Radio 99.7
link997 = 'http://5278fa1a8b76e.streamlock.net/live/997.stream/playlist.m3u8'
li997 = xbmcgui.ListItem(label='Ikh Mongol Radio 99.7', path=link997)
li997.setInfo(type='Video', infoLabels={ "Title": 'Ikh Mongol Radio 99.7' })
li997.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=link997, listitem=li997, isFolder=False)

#Ulaanbaatar Radio 102.5
link1025 = 'http://5278fa1a8b76e.streamlock.net/live/1025.stream/playlist.m3u8'
li1025 = xbmcgui.ListItem(label='Ulaanbaatar Radio 102.5', path=link1025)
li1025.setInfo(type='Video', infoLabels={ "Title": 'Ulaanbaatar Radio 102.5' })
li1025.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=link1025, listitem=li1025, isFolder=False)

#Ger Bvliin Radio 104.5
link1045 = 'http://5278fa1a8b76e.streamlock.net/live/1045.stream/playlist.m3u8'
li1045 = xbmcgui.ListItem(label='Ger Bvliin Radio 104.5', path=link1045)
li1045.setInfo(type='Video', infoLabels={ "Title": 'Ger Bvliin Radio 104.5' })
li1045.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=link1045, listitem=li1045, isFolder=False)

#Lavain Egshig Radio 97.5
link975 = 'http://5278fa1a8b76e.streamlock.net/live/975.stream/playlist.m3u8'
li975 = xbmcgui.ListItem(label='Lavain Egshig Radio 97.5', path=link975)
li975.setInfo(type='Video', infoLabels={ "Title": 'Lavain Egshig Radio 97.5' })
li975.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=link975, listitem=li975, isFolder=False)

#Khamag Mongol Radio 95.1
link951 = 'http://5278fa1a8b76e.streamlock.net/live/951.stream/playlist.m3u8'
li951 = xbmcgui.ListItem(label='Khamag Mongol Radio 95.1', path=link951)
li951.setInfo(type='Video', infoLabels={ "Title": 'Khamag Mongol Radio 95.1' })
li951.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=link951, listitem=li951, isFolder=False)

#Auto Radio 105.5
link1055 = 'http://5278fa1a8b76e.streamlock.net/live/1055.stream/playlist.m3u8'
li1055 = xbmcgui.ListItem(label='Auto Radio 105.5', path=link1055)
li1055.setInfo(type='Video', infoLabels={ "Title": 'Auto Radio 105.5' })
li1055.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=link1055, listitem=li1055, isFolder=False)

#MGL Radio 102.1
link1021 = 'http://209.105.250.73:8080/;stream.nsv'
li1021 = xbmcgui.ListItem(label='MGL Radio 102.1', path=link1021)
li1021.setInfo(type='Video', infoLabels={ "Title": 'MGL Radio 102.1' })
li1021.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=link1021, listitem=li1021, isFolder=False)

xbmcplugin.endOfDirectory(int(sys.argv[1]))



#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys,os,re,urllib,xbmcplugin,xbmcaddon,xbmcgui

addonID = "script.categories"
addon_work_folder=xbmc.translatePath("special://profile/addon_data/"+addonID)
playlist=xbmc.translatePath("special://profile/addon_data/"+addonID+"/categories")
addon = xbmcaddon.Addon(id=addonID)
translation = addon.getLocalizedString

playlistsTemp=[]
for i in range(0,9,1):
  playlistsTemp.append(addon.getSetting("cat"+str(i)))
playlists=[]
for pl in playlistsTemp:
  if pl!="":
    playlists.append(pl)
playlists.append("- "+translation(30005))

if not os.path.isdir(addon_work_folder):
  os.mkdir(addon_work_folder)

param=urllib.unquote_plus(sys.argv[1])

if len(playlists)==0:
  addon.openSettings()
  playlistsTemp=[]
  for i in range(0,9,1):
    playlistsTemp.append(addon.getSetting("cat"+str(i)))
  playlists=[]
  for pl in playlistsTemp:
    if pl!="":
      playlists.append(pl)
  playlists.append("- "+translation(30005))
dialog = xbmcgui.Dialog()
pl = playlists[dialog.select(translation(30004), playlists)]
while ("- "+str(translation(30005)) in pl):
  addon.openSettings()
  playlistsTemp=[]
  for i in range(0,9,1):
    playlistsTemp.append(addon.getSetting("cat"+str(i)))
  playlists=[]
  for pl in playlistsTemp:
    if pl!="":
      playlists.append(pl)
  playlists.append("- "+translation(30005))
  dialog = xbmcgui.Dialog()
  pl = playlists[dialog.select(translation(30004), playlists)]
playlistEntry=param+"#"+pl
if os.path.exists(playlist):
  fh = open(playlist, 'r')
  content=fh.read()
  fh.close()
  if content.find(playlistEntry)==-1:
    fh=open(playlist, 'a')
    fh.write(playlistEntry+"\n")
    fh.close()
else:
  fh=open(playlist, 'a')
  fh.write(playlistEntry+"\n")
  fh.close()

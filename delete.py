#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys,os,re,urllib,xbmcplugin,xbmcaddon,xbmcgui

addonID = "script.categories"
addon_work_folder=xbmc.translatePath("special://profile/addon_data/"+addonID)
playlist=xbmc.translatePath("special://profile/addon_data/"+addonID+"/categories")

if not os.path.isdir(addon_work_folder):
  os.mkdir(addon_work_folder)

param=urllib.unquote_plus(sys.argv[1])

fh = open(playlist, 'r')
content=fh.read()
fh.close()
fh=open(playlist, 'w')
fh.write(content.replace(param,""))
fh.close()
xbmc.executebuiltin("Container.Refresh")

# -*- coding: utf-8 -*-

import xbmc,xbmcgui
import subprocess,os
import xbmcaddon
import json
import time
import requests
import datetime, time
from requests.auth import HTTPBasicAuth

#Initialize AddOn
settings = xbmcaddon.Addon(id='insteon.addon')

#NIGHT MODE

hour = 0

night_mode = settings.getSetting( "night_mode" )
on_time = int(settings.getSetting( "night_on_time" ))
off_time = int(settings.getSetting( "night_off_time" ))
night_switch = 3

#Degub

degug_mode = settings.getSetting( "degub_mode_state" )


#Initialize AddOn information

__addonname__     = settings.getAddonInfo('name')
__icon__          = settings.getAddonInfo('icon')
plugin_test = "Working"
plugin_start = "INSTEON plugin started"
plugin_ip = "Please insert your INSTEON Hub IP address in the addon settings"
plugin_port = "Please insert your INSTEON Hub Port number in the addon settings"
plugin_user = "Please insert your INSTEON Hub Username in the addon settings"
plugin_pword = "Please insert your INSTEON Hub Password in the addon settings"
plugin_gid = "Please assign an INSTEON Group (Scene) ID in the addon settings"
time1        = 7000
time2        = 3000


#Initialize INSTEON Hub information
hip      =  settings.getSetting( "hub_ip" )
hport    =  settings.getSetting( "hub_port" )
huser    =  settings.getSetting( "hub_user" )
hpword   =  settings.getSetting( "hub_pword" )



#Initialize INSTEON Hub Groups (Scenes)
g_video_started = settings.getSetting( "video_start_gid" )
g_video_paused = settings.getSetting( "video_pause_gid" )
g_video_resumed = settings.getSetting( "video_resume_gid" )
g_video_stopped = settings.getSetting( "video_stop_gid" )
g_video_ended = settings.getSetting( "video_end_gid" )

g_audio_started = settings.getSetting( "audio_start_gid" )
g_audio_paused = settings.getSetting( "audio_pause_gid" )
g_audio_resumed = settings.getSetting( "audio_resume_gid" )
g_audio_stopped = settings.getSetting( "audio_stop_gid" )
g_audio_ended = settings.getSetting( "audio_end_gid" )
	

#Check if INSTEON Hub information has been entered
if (degug_mode == "Yes"):
    if (hip == "0.0.0.0"):
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,plugin_ip, time1, __icon__))
        print("INSTEON Addon - Hub IP Address Not Set")
    else:
        if (hport == ""):
            xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,plugin_port, time1, __icon__))
            print("INSTEON Addon - Hub Port Not Set")
        else:
            if (huser == ""):
                xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,plugin_user, time1, __icon__))
                print("INSTEON Addon - Hub User Name Not Set")
            else:
                if (hpword == ""):
                    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,plugin_pword, time1, __icon__))
                    print("INSTEON Addon - Hub Password Not Set")
                else:
                    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,plugin_start, time2, __icon__))
                    print("INSTEON Addon - Hub Information Set")


#Initialize Shortcut INSTEON Hub Groups (Scenes)

shortActive = 0
shortActive1 = 0
shortActive2 = 0
shortActive3 = 0
shortActive4 = 0
shortActive5 = 0


if (str(settings.getSetting("short_active")) == "Yes"):
    shortActive = 1
    if (str(settings.getSetting("short_1_active")) == "Yes"):
        if (str(settings.getSetting("short_1_name")) == ""):
            shortName1 = "Shorcut 1 Name Not Set"
        else:
            if (str(settings.getSetting("short_1_gid")) == ""):
                shortName1 = "Shorcut 1 Scene ID Not Set"
            else:
                shortActive1 = 1
                shortName1 = settings.getSetting( "short_1_name" )
                shortGid1 = settings.getSetting( "short_1_gid" )
    else:
        shortActive1 = 0
        shortName1 = "Shortcut 1 Not Active"

    if (str(settings.getSetting("short_2_active")) == "Yes"):
        if (str(settings.getSetting("short_2_name")) == ""):
            shortName2 = "Shorcut 2 Name Not Set"
        else:
            if (str(settings.getSetting("short_2_gid")) == ""):
                shortName2 = "Shorcut 2 Scene ID Not Set"
            else:
                shortActive2 = 1
                shortName2 = settings.getSetting( "short_2_name" )
                shortGid2 = settings.getSetting( "short_2_gid" )
    else:
        shortActive2 = 0
        shortName2 = "Shortcut 2 Not Active"

    if (str(settings.getSetting("short_3_active")) == "Yes"):
        if (str(settings.getSetting("short_3_name")) == ""):
            shortName3 = "Shorcut 3 Name Not Set"
        else:
            if (str(settings.getSetting("short_3_gid")) == ""):
                shortName3 = "Shorcut 3 Scene ID Not Set"
            else:
                shortActive3 = 1
                shortName3 = settings.getSetting( "short_3_name" )
                shortGid3 = settings.getSetting( "short_3_gid" )
    else:
        shortActive3 = 0
        shortName3 = "Shortcut 3 Not Active"

    if (str(settings.getSetting("short_4_active")) == "Yes"):
        if (str(settings.getSetting("short_4_name")) == ""):
            shortName4 = "Shorcut 4 Name Not Set"
        else:
            if (str(settings.getSetting("short_4_gid")) == ""):
                shortName4 = "Shorcut 4 Scene ID Not Set"
            else:
                shortActive4 = 1
                shortName4 = settings.getSetting( "short_4_name" )
                shortGid4 = settings.getSetting( "short_4_gid" )
    else:
        shortActive4 = 0
        shortName4 = "Shortcut 4 Not Active"

    if (str(settings.getSetting("short_5_active")) == "Yes"):
        if (str(settings.getSetting("short_5_name")) == ""):
            shortName5 = "Shorcut 5 Name Not Set"
        else:
            if (str(settings.getSetting("short_5_gid")) == ""):
                shortName5 = "Shorcut 5 Scene ID Not Set"
            else:
                shortActive5 = 1
                shortName5 = settings.getSetting( "short_5_name" )
                shortGid5 = settings.getSetting( "short_5_gid" )
    else:
        shortActive5 = 0
        shortName5 = "Shortcut 5 Not Active"

else:
    shortActive = 0


#Shortcut Dialog Window

#get actioncodes from https://github.com/xbmc/xbmc/blob/master/xbmc/guilib/Key.h
ACTION_PREVIOUS_MENU = 10

class MyClass(xbmcgui.WindowDialog):
    def __init__(self):
        background = xbmcgui.ControlImage(43, 43, 279, 166, 'ContentPanel.png')
        self.addControl(background)
        self.strActionInfo = xbmcgui.ControlLabel(43, 43, 279, 20, '', 'font13', '0xFFFF00FF')
        self.addControl(self.strActionInfo)
        self.strActionInfo.setLabel('')
        self.button0 = xbmcgui.ControlButton(51, 51, 263, 30, shortName1)
        self.addControl(self.button0)
        self.button1 = xbmcgui.ControlButton(51, 81, 263, 30, shortName2)
        self.addControl(self.button1)
        self.button2 = xbmcgui.ControlButton(51, 111, 263, 30, shortName3)
        self.addControl(self.button2)
        self.button3 = xbmcgui.ControlButton(51, 141, 263, 30, shortName4)
        self.addControl(self.button3)
        self.button4 = xbmcgui.ControlButton(51, 171, 263, 30, shortName5)
        self.addControl(self.button4)
        self.setFocus(self.button0)
        self.button0.controlDown(self.button1)
        self.button0.controlUp(self.button4)
        self.button1.controlUp(self.button0)
        self.button1.controlDown(self.button2)
        self.button2.controlUp(self.button1)
        self.button2.controlDown(self.button3)
        self.button3.controlUp(self.button2)
        self.button3.controlDown(self.button4)
        self.button4.controlUp(self.button3)
        self.button4.controlDown(self.button0)

    def onAction(self, action):
        if action == ACTION_PREVIOUS_MENU:
            self.close()

# Add Debugging

    def onControl(self, control):
        if control == self.button0:
            if (shortActive1 == 1):
                auth=HTTPBasicAuth( huser , hpword )
                url = 'http://%s:%s/0?11%s=I=0' % ( hip, hport, shortGid1 )
                r = requests.post(url=url, auth=auth)
                if (str(settings.getSetting("short_1_win")) == "None"):
                    if (degug_mode == "Yes"):
                        xbmc.executebuiltin('Notification(%s, Shortcut 1 Active - XBMC Window Not Set, %d, %s)'%(__addonname__,time1, __icon__))
                        print("INSTEON Addon - Shortcut 1 Active - XBMC Window Not Set")
                else:
                    if (str(settings.getSetting("short_1_win")) == "Movies - Recently Added"):
                        xbmc.executebuiltin("ActivateWindow(VideoLibrary,RecentlyAddedMovies,return)")
                    if (str(settings.getSetting("short_1_win")) == "Movies - Titles"):
                        xbmc.executebuiltin("ActivateWindow(VideoLibrary,MovieTitles,return)")
                    if (str(settings.getSetting("short_1_win")) == "TV Shows - Titles"):
                        xbmc.executebuiltin("ActivateWindow(VideoLibrary,TvShowTitles,return)")
                    if (str(settings.getSetting("short_1_win")) == "Music - Videos"):
                        xbmc.executebuiltin("ActivateWindow(VideoLibrary,MusicVideos,return)")
                    if (str(settings.getSetting("short_1_win")) == "Music - Playlists"):
                        xbmc.executebuiltin("ActivateWindow(MusicLibrary,Playlists,return)")
                    if (str(settings.getSetting("short_1_win")) == "Music - Albums"):
                        xbmc.executebuiltin("ActivateWindow(MusicLibrary,Albums,return)")
                    if (str(settings.getSetting("short_1_win")) == "Music - Artists"):
                        xbmc.executebuiltin("ActivateWindow(MusicLibrary,Artists,return)")
                self.close()
        if control == self.button1:
            if (shortActive2 == 1): 
                auth=HTTPBasicAuth( huser , hpword )
                url = 'http://%s:%s/0?11%s=I=0' % ( hip, hport, shortGid2 )
                r = requests.post(url=url, auth=auth)
                if (str(settings.getSetting("short_1_win")) == "None"):
                    xbmc.executebuiltin('Notification(%s, Debug not completed, %d, %s)'%(__addonname__,time1, __icon__))
                else:
                    if (str(settings.getSetting("short_2_win")) == "Movies - Recently Added"):
                        xbmc.executebuiltin("ActivateWindow(VideoLibrary,RecentlyAddedMovies,return)")
                    if (str(settings.getSetting("short_2_win")) == "Movies - Titles"):
                        xbmc.executebuiltin("ActivateWindow(VideoLibrary,MovieTitles,return)")
                    if (str(settings.getSetting("short_2_win")) == "TV Shows - Titles"):
                        xbmc.executebuiltin("ActivateWindow(VideoLibrary,TvShowTitles,return)")
                    if (str(settings.getSetting("short_2_win")) == "Music - Videos"):
                        xbmc.executebuiltin("ActivateWindow(VideoLibrary,MusicVideos,return)")
                    if (str(settings.getSetting("short_2_win")) == "Music - Playlists"):
                        xbmc.executebuiltin("ActivateWindow(MusicLibrary,Playlists,return)")
                    if (str(settings.getSetting("short_2_win")) == "Music - Albums"):
                        xbmc.executebuiltin("ActivateWindow(MusicLibrary,Albums,return)")
                    if (str(settings.getSetting("short_2_win")) == "Music - Artists"):
                        xbmc.executebuiltin("ActivateWindow(MusicLibrary,Artists,return)")
                self.close()
        if control == self.button2:
            if (shortActive3 == 1): 
                auth=HTTPBasicAuth( huser , hpword )
                url = 'http://%s:%s/0?11%s=I=0' % ( hip, hport, shortGid3 )
                r = requests.post(url=url, auth=auth)
                if (str(settings.getSetting("short_1_win")) == "None"):
                    xbmc.executebuiltin('Notification(%s, Debug not completed, %d, %s)'%(__addonname__,time1, __icon__))
                else:
                    if (str(settings.getSetting("short_3_win")) == "Movies - Recently Added"):
                        xbmc.executebuiltin("ActivateWindow(VideoLibrary,RecentlyAddedMovies,return)")
                    if (str(settings.getSetting("short_3_win")) == "Movies - Titles"):
                        xbmc.executebuiltin("ActivateWindow(VideoLibrary,MovieTitles,return)")
                    if (str(settings.getSetting("short_3_win")) == "TV Shows - Titles"):
                        xbmc.executebuiltin("ActivateWindow(VideoLibrary,TvShowTitles,return)")
                    if (str(settings.getSetting("short_3_win")) == "Music - Videos"):
                        xbmc.executebuiltin("ActivateWindow(VideoLibrary,MusicVideos,return)")
                    if (str(settings.getSetting("short_3_win")) == "Music - Playlists"):
                        xbmc.executebuiltin("ActivateWindow(MusicLibrary,Playlists,return)")
                    if (str(settings.getSetting("short_3_win")) == "Music - Albums"):
                        xbmc.executebuiltin("ActivateWindow(MusicLibrary,Albums,return)")
                    if (str(settings.getSetting("short_3_win")) == "Music - Artists"):
                        xbmc.executebuiltin("ActivateWindow(MusicLibrary,Artists,return)")
                self.close()
        if control == self.button3:
            if (shortActive4 == 1): 
                auth=HTTPBasicAuth( huser , hpword )
                url = 'http://%s:%s/0?11%s=I=0' % ( hip, hport, shortGid4 )
                r = requests.post(url=url, auth=auth)
                if (str(settings.getSetting("short_1_win")) == "None"):
                    xbmc.executebuiltin('Notification(%s, Debug not completed, %d, %s)'%(__addonname__,time1, __icon__))
                else:
                    if (str(settings.getSetting("short_4_win")) == "Movies - Recently Added"):
                        xbmc.executebuiltin("ActivateWindow(VideoLibrary,RecentlyAddedMovies,return)")
                    if (str(settings.getSetting("short_4_win")) == "Movies - Titles"):
                        xbmc.executebuiltin("ActivateWindow(VideoLibrary,MovieTitles,return)")
                    if (str(settings.getSetting("short_4_win")) == "TV Shows - Titles"):
                        xbmc.executebuiltin("ActivateWindow(VideoLibrary,TvShowTitles,return)")
                    if (str(settings.getSetting("short_4_win")) == "Music - Videos"):
                        xbmc.executebuiltin("ActivateWindow(VideoLibrary,MusicVideos,return)")
                    if (str(settings.getSetting("short_4_win")) == "Music - Playlists"):
                        xbmc.executebuiltin("ActivateWindow(MusicLibrary,Playlists,return)")
                    if (str(settings.getSetting("short_4_win")) == "Music - Albums"):
                        xbmc.executebuiltin("ActivateWindow(MusicLibrary,Albums,return)")
                    if (str(settings.getSetting("short_4_win")) == "Music - Artists"):
                        xbmc.executebuiltin("ActivateWindow(MusicLibrary,Artists,return)")
                self.close()
        if control == self.button4:
            if (shortActive5 == 1): 
                auth=HTTPBasicAuth( huser , hpword )
                url = 'http://%s:%s/0?11%s=I=0' % ( hip, hport, shortGid5 )
                r = requests.post(url=url, auth=auth)
                if (str(settings.getSetting("short_1_win")) == "None"):
                    xbmc.executebuiltin('Notification(%s, Debug not completed, %d, %s)'%(__addonname__,time1, __icon__))
                else:
                    if (str(settings.getSetting("short_5_win")) == "Movies - Recently Added"):
                        xbmc.executebuiltin("ActivateWindow(VideoLibrary,RecentlyAddedMovies,return)")
                    if (str(settings.getSetting("short_5_win")) == "Movies - Titles"):
                        xbmc.executebuiltin("ActivateWindow(VideoLibrary,MovieTitles,return)")
                    if (str(settings.getSetting("short_5_win")) == "TV Shows - Titles"):
                        xbmc.executebuiltin("ActivateWindow(VideoLibrary,TvShowTitles,return)")
                    if (str(settings.getSetting("short_5_win")) == "Music - Videos"):
                        xbmc.executebuiltin("ActivateWindow(VideoLibrary,MusicVideos,return)")
                    if (str(settings.getSetting("short_5_win")) == "Music - Playlists"):
                        xbmc.executebuiltin("ActivateWindow(MusicLibrary,Playlists,return)")
                    if (str(settings.getSetting("short_5_win")) == "Music - Albums"):
                        xbmc.executebuiltin("ActivateWindow(MusicLibrary,Albums,return)")
                    if (str(settings.getSetting("short_5_win")) == "Music - Artists"):
                        xbmc.executebuiltin("ActivateWindow(MusicLibrary,Artists,return)")
                self.close()
 
#Do the magic

class MyPlayer(xbmc.Player):

    def onPlayBackStarted(self):
        xbmc.sleep(200) # it may take some time for xbmc to read tag info after playback started
        if xbmc.Player().isPlayingVideo():
            if (str(settings.getSetting("video_started")) == "Yes"):
                if (str(settings.getSetting("video_start_gid")) == ""):
                    if (degug_mode == "Yes"):
                        xbmc.executebuiltin('Notification(%s, Video Started - Scene Active - ID Not Set, %d, %s)'%(__addonname__,time1, __icon__))
                        print("INSTEON Addon - Video Started - Scene Active - ID Not Set")
                    else:
                        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,plugin_gid, time1, __icon__))
                else:
                    if (night_mode == "Yes"):
                        if (night_switch == 1):
                            auth=HTTPBasicAuth( huser , hpword )
                            url = 'http://%s:%s/0?11%s=I=0' % ( hip, hport, g_video_started )
                            r = requests.post(url=url, auth=auth)
                            if (degug_mode == "Yes"):
                                xbmc.executebuiltin('Notification(%s, Video Started - Scene Active - Night Mode On - Is Night, %d, %s)'%(__addonname__,time1, __icon__))
                                print("INSTEON Addon - Video Started - Scene Active - Night Mode On - Is Night")
                                print("INSTEON Addon - Group (Scene) ID: " + g_video_started)
                                print("INSTEON Addon - HTTP URL: " + url)
                        else:
                            if (degug_mode == "Yes"):
                                xbmc.executebuiltin('Notification(%s, Video Started - Scene Active - Night Mode On - Not Night, %d, %s)'%(__addonname__,time1, __icon__))
                                print("INSTEON Addon - Video Started - Scene Active - Night Mode On - Not Night")
                    else:
                        auth=HTTPBasicAuth( huser , hpword )
                        url = 'http://%s:%s/0?11%s=I=0' % ( hip, hport, g_video_started )
                        r = requests.post(url=url, auth=auth)
                        if (degug_mode == "Yes"):
                            xbmc.executebuiltin('Notification(%s, Video Started - Scene Active - Night Mode Off, %d, %s)'%(__addonname__,time1, __icon__))
                            print("INSTEON Addon - Video Started - Scene Active - Night Mode Off")
                            print("INSTEON Addon - Group (Scene) ID: " + g_video_started)
                            print("INSTEON Addon - HTTP URL: " + url)
            else:
                if (degug_mode == "Yes"):
                    xbmc.executebuiltin('Notification(%s, Video Started - Scene Inactive, %d, %s)'%(__addonname__,time1, __icon__))
                    print("INSTEON Addon - Video Started - Scene Inactive")

        if xbmc.Player().isPlayingAudio() == True:
            if (str(settings.getSetting("audio_started")) == "Yes"):
                if (str(settings.getSetting("audio_start_gid")) == ""):
                    if (degug_mode == "Yes"):
                        xbmc.executebuiltin('Notification(%s, Audio Started - Scene Active - ID Not Set, %d, %s)'%(__addonname__,time1, __icon__))
                        print("INSTEON Addon - Audio Started - Scene Active - ID Not Set")
                    else:
                        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,plugin_gid, time1, __icon__))
                else:
                    if (night_mode == "Yes"):
                        if (night_switch == 1):
                            auth=HTTPBasicAuth( huser , hpword )
                            url = 'http://%s:%s/0?11%s=I=0' % ( hip, hport, g_audio_started )
                            r = requests.post(url=url, auth=auth)
                            if (degug_mode == "Yes"):
                                xbmc.executebuiltin('Notification(%s, Audio Started - Scene Active - Night Mode On - Is Night, %d, %s)'%(__addonname__,time1, __icon__))
                                print("INSTEON Addon - Audio Started - Scene Active - Night Mode On - Is Night")
                                print("INSTEON Addon - Group (Scene) ID: " + g_audio_started)
                                print("INSTEON Addon - HTTP URL: " + url)
                        else:
                            if (degug_mode == "Yes"):
                                xbmc.executebuiltin('Notification(%s, Audio Started - Scene Active - Night Mode On - Not Night, %d, %s)'%(__addonname__,time1, __icon__))
                                print("INSTEON Addon - Audio Started - Scene Active - Night Mode On - Not Night")
                    else:
                        auth=HTTPBasicAuth( huser , hpword )
                        url = 'http://%s:%s/0?11%s=I=0' % ( hip, hport, g_audio_started )
                        r = requests.post(url=url, auth=auth)
                        if (degug_mode == "Yes"):
                            xbmc.executebuiltin('Notification(%s, Audio Started - Scene Active - Night Mode Off, %d, %s)'%(__addonname__,time1, __icon__))
                            print("INSTEON Addon - Audio Started - Scene Active - Night Mode Off")
                            print("INSTEON Addon - Group (Scene) ID: " + g_audio_started)
                            print("INSTEON Addon - HTTP URL: " + url)
            else:
                if (degug_mode == "Yes"):
                    xbmc.executebuiltin('Notification(%s, Audio Started - Scene Inactive, %d, %s)'%(__addonname__,time1, __icon__))
                    print("INSTEON Addon - Audio Started - Scene Inactive")

    def onPlayBackStopped(self):
        if (VIDEO == 1):
            if (str(settings.getSetting("video_stopped")) == "Yes"):
                if (str(settings.getSetting("video_stop_gid")) == ""):
                    if (degug_mode == "Yes"):
                        xbmc.executebuiltin('Notification(%s, Video Stopped - Scene Active - ID Not Set, %d, %s)'%(__addonname__,time1, __icon__))
                        print("INSTEON Addon - Video Stopped - Scene Active - ID Not Set")
                    else:
                        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,plugin_gid, time1, __icon__))
            	else:
            	    if (night_mode == "Yes"):
                        if (night_switch == 1):
                            auth=HTTPBasicAuth( huser , hpword )
                            url = 'http://%s:%s/0?11%s=I=0' % ( hip, hport, g_video_stopped )
                            r = requests.post(url=url, auth=auth)
                            if (degug_mode == "Yes"):
                                xbmc.executebuiltin('Notification(%s, Video Stopped - Scene Active - Night Mode On - Is Night, %d, %s)'%(__addonname__,time1, __icon__))
                                print("INSTEON Addon - Video Stopped - Scene Active - Night Mode On - Is Night")
                                print("INSTEON Addon - Group (Scene) ID: " + g_video_stopped)
                                print("INSTEON Addon - HTTP URL: " + url)
                        else:
                            if (degug_mode == "Yes"):
                                xbmc.executebuiltin('Notification(%s, Video Stopped - Scene Active - Night Mode On - Not Night, %d, %s)'%(__addonname__,time1, __icon__))
                                print("INSTEON Addon - Video Stopped - Scene Active - Night Mode On - Not Night")
                    else:
                        auth=HTTPBasicAuth( huser , hpword )
                        url = 'http://%s:%s/0?11%s=I=0' % ( hip, hport, g_video_stopped )
                        r = requests.post(url=url, auth=auth)
                        if (degug_mode == "Yes"):
                            xbmc.executebuiltin('Notification(%s, Video Stopped - Scene Active - Night Mode Off, %d, %s)'%(__addonname__,time1, __icon__))
                            print("INSTEON Addon - Video Stopped - Scene Active - Night Mode Off")
                            print("INSTEON Addon - Group (Scene) ID: " + g_video_stopped)
                            print("INSTEON Addon - HTTP URL: " + url)
            else:
                if (degug_mode == "Yes"):
                    xbmc.executebuiltin('Notification(%s, Video Stopped - Scene Inactive, %d, %s)'%(__addonname__,time1, __icon__))
                    print("INSTEON Addon - Video Stopped - Scene Inactive")

        if (AUDIO == 1):
            if (str(settings.getSetting("audio_stopped")) == "Yes"):
                if (str(settings.getSetting("audio_stop_gid")) == ""):
                    if (degug_mode == "Yes"):
                        xbmc.executebuiltin('Notification(%s, Audio Stopped - Scene Active - ID Not Set, %d, %s)'%(__addonname__,time1, __icon__))
                        print("INSTEON Addon - Audio Stopped - Scene Active - ID Not Set")
                    else:
                        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,plugin_gid, time1, __icon__))
            	else:
            	    if (night_mode == "Yes"):
                        if (night_switch == 1):
                            auth=HTTPBasicAuth( huser , hpword )
                            url = 'http://%s:%s/0?11%s=I=0' % ( hip, hport, g_audio_stopped )
                            r = requests.post(url=url, auth=auth)
                            if (degug_mode == "Yes"):
                                xbmc.executebuiltin('Notification(%s, Audio Stopped - Scene Active - Night Mode On - Is Night, %d, %s)'%(__addonname__,time1, __icon__))
                                print("INSTEON Addon - Audio Stopped - Scene Active - Night Mode On - Is Night")
                                print("INSTEON Addon - Group (Scene) ID: " + g_audio_stopped)
                                print("INSTEON Addon - HTTP URL: " + url)
                        else:
                            if (degug_mode == "Yes"):
                                xbmc.executebuiltin('Notification(%s, Audio Stopped - Scene Active - Night Mode On - Not Night, %d, %s)'%(__addonname__,time1, __icon__))
                                print("INSTEON Addon - Audio Stopped - Scene Active - Night Mode On - Not Night")
                    else:
                        auth=HTTPBasicAuth( huser , hpword )
                        url = 'http://%s:%s/0?11%s=I=0' % ( hip, hport, g_audio_stopped )
                        r = requests.post(url=url, auth=auth)
                        if (degug_mode == "Yes"):
                            xbmc.executebuiltin('Notification(%s, Audio Stopped - Scene Active - Night Mode Off, %d, %s)'%(__addonname__,time1, __icon__))
                            print("INSTEON Addon - Audio Stopped - Scene Active - Night Mode Off")
                            print("INSTEON Addon - Group (Scene) ID: " + g_audio_stopped)
                            print("INSTEON Addon - HTTP URL: " + url)
            else:
                if (degug_mode == "Yes"):
                    xbmc.executebuiltin('Notification(%s, Audio Stopped - Scene Inactive, %d, %s)'%(__addonname__,time1, __icon__))
                    print("INSTEON Addon - Audio Stopped - Scene Inactive")

    def onPlayBackEnded(self):
        if (VIDEO == 1):
            if (str(settings.getSetting("video_ended")) == "Yes"):
                if (str(settings.getSetting("video_end_gid")) == ""):
                    if (degug_mode == "Yes"):
                        xbmc.executebuiltin('Notification(%s, Video Ended - Scene Active - ID Not Set, %d, %s)'%(__addonname__,time1, __icon__))
                        print("INSTEON Addon - Video Ended - Scene Active - ID Not Set")
                    else:
                        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,plugin_gid, time1, __icon__))
            	else:
            	    if (night_mode == "Yes"):
                        if (night_switch == 1):
                            auth=HTTPBasicAuth( huser , hpword )
                            url = 'http://%s:%s/0?11%s=I=0' % ( hip, hport, g_video_ended )
                            r = requests.post(url=url, auth=auth)
                            if (degug_mode == "Yes"):
                                xbmc.executebuiltin('Notification(%s, Video Ended - Scene Active - Night Mode On - Is Night, %d, %s)'%(__addonname__,time1, __icon__))
                                print("INSTEON Addon - Video Ended - Scene Active - Night Mode On - Is Night")
                                print("INSTEON Addon - Group (Scene) ID: " + g_video_ended)
                                print("INSTEON Addon - HTTP URL: " + url)
                        else:
                            if (degug_mode == "Yes"):
                                xbmc.executebuiltin('Notification(%s, Video Ended - Scene Active - Night Mode On - Not Night, %d, %s)'%(__addonname__,time1, __icon__))
                                print("INSTEON Addon - Video Ended - Scene Active - Night Mode On - Not Night")
                    else:
                        auth=HTTPBasicAuth( huser , hpword )
                        url = 'http://%s:%s/0?11%s=I=0' % ( hip, hport, g_video_ended )
                        r = requests.post(url=url, auth=auth)
                        if (degug_mode == "Yes"):
                            xbmc.executebuiltin('Notification(%s, Video Ended - Scene Active - Night Mode Off, %d, %s)'%(__addonname__,time1, __icon__))
                            print("INSTEON Addon - Video Ended - Scene Active - Night Mode Off")
                            print("INSTEON Addon - Group (Scene) ID: " + g_video_ended)
                            print("INSTEON Addon - HTTP URL: " + url)
            else:
                if (degug_mode == "Yes"):
                    xbmc.executebuiltin('Notification(%s, Video Ended - Scene Inactive, %d, %s)'%(__addonname__,time1, __icon__))
                    print("INSTEON Addon - Video Ended - Scene Inactive")

        if (AUDIO == 1):
            if (str(settings.getSetting("audio_ended")) == "Yes"):
                if (str(settings.getSetting("audio_end_gid")) == ""):
                    if (degug_mode == "Yes"):
                        xbmc.executebuiltin('Notification(%s, Audio Ended - Scene Active - ID Not Set, %d, %s)'%(__addonname__,time1, __icon__))
                        print("INSTEON Addon - Audio Ended - Scene Active - ID Not Set")
                    else:
                        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,plugin_gid, time1, __icon__))
            	else:
            	    if (night_mode == "Yes"):
                        if (night_switch == 1):
                            auth=HTTPBasicAuth( huser , hpword )
                            url = 'http://%s:%s/0?11%s=I=0' % ( hip, hport, g_audio_ended )
                            r = requests.post(url=url, auth=auth)
                            if (degug_mode == "Yes"):
                                xbmc.executebuiltin('Notification(%s, Audio Ended - Scene Active - Night Mode On - Is Night, %d, %s)'%(__addonname__,time1, __icon__))
                                print("INSTEON Addon - Audio Ended - Scene Active - Night Mode On - Is Night")
                                print("INSTEON Addon - Group (Scene) ID: " + g_audio_ended)
                                print("INSTEON Addon - HTTP URL: " + url)
                        else:
                            if (degug_mode == "Yes"):
                                xbmc.executebuiltin('Notification(%s, Audio Ended - Scene Active - Night Mode On - Not Night, %d, %s)'%(__addonname__,time1, __icon__))
                                print("INSTEON Addon - Audio Ended - Scene Active - Night Mode On - Not Night")
                    else:
                        auth=HTTPBasicAuth( huser , hpword )
                        url = 'http://%s:%s/0?11%s=I=0' % ( hip, hport, g_audio_ended )
                        r = requests.post(url=url, auth=auth)
                        if (degug_mode == "Yes"):
                            xbmc.executebuiltin('Notification(%s, Audio Ended - Scene Active - Night Mode Off, %d, %s)'%(__addonname__,time1, __icon__))
                            print("INSTEON Addon - Audio Ended - Scene Active - Night Mode Off")
                            print("INSTEON Addon - Group (Scene) ID: " + g_audio_ended)
                            print("INSTEON Addon - HTTP URL: " + url)
            else:
                if (degug_mode == "Yes"):
                    xbmc.executebuiltin('Notification(%s, Audio Ended - Scene Inactive, %d, %s)'%(__addonname__,time1, __icon__))
                    print("INSTEON Addon - Audio Ended - Scene Inactive")


player=MyPlayer()

VIDEO = 0
AUDIO = 0
VPAUSE = 0
APAUSE = 0

#Loop video and audio playing check for states and pause

while( not xbmc.abortRequested ):
#Shortcut Popup - Need make this happen on custom keypress (ie CTRL + I) - a combination unlikely to be used by XBMC < Is there a better way?
    if xbmcgui.Window( 10000 ).getProperty( "insteonmenu" ) == "true":
        mydisplay = MyClass()
        mydisplay .doModal()
        del mydisplay
        xbmcgui.Window( 10000 ).setProperty( "insteonmenu", "false" )
    
    if xbmc.Player().isPlaying():
        if xbmc.Player().isPlayingVideo():
            VIDEO = 1
            AUDIO = 0

#Check pause state - can audio and video be combined?
#Check pause state - is there a better way?
            if xbmc.getCondVisibility('Player.Paused'):
                if (str(settings.getSetting("video_paused")) == "Yes"):
                    if (str(settings.getSetting("video_pause_gid")) == ""):
                        if (degug_mode == "Yes"):
                            xbmc.executebuiltin('Notification(%s, Video Paused - Scene Active - ID Not Set, %d, %s)'%(__addonname__,time1, __icon__))
                            print("INSTEON Addon - Video Paused - Scene Active - ID Not Set")
                        else:
                            xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,plugin_gid, time1, __icon__))
                    else:
                        if (night_mode == "Yes"):
                            if (night_switch == 1):
                                VPAUSE = 1
                                auth=HTTPBasicAuth( huser , hpword )
                                url = 'http://%s:%s/0?11%s=I=0' % ( hip, hport, g_video_paused )
                                r = requests.post(url=url, auth=auth)
                                if (degug_mode == "Yes"):
                                    xbmc.executebuiltin('Notification(%s, Video Paused - Scene Active - Night Mode On - Is Night, %d, %s)'%(__addonname__,time1, __icon__))
                                    print("INSTEON Addon - Video Paused - Scene Active - Night Mode On - Is Night")
                                    print("INSTEON Addon - Group (Scene) ID: " + g_video_paused)
                                    print("INSTEON Addon - HTTP URL: " + url)
                            else:
                                if (degug_mode == "Yes"):
                                    xbmc.executebuiltin('Notification(%s, Video Paused - Scene Active - Night Mode On - Not Night, %d, %s)'%(__addonname__,time1, __icon__))
                                    print("INSTEON Addon - Video Paused - Scene Active - Night Mode On - Not Night")
                        else:
                            VPAUSE = 1
                            auth=HTTPBasicAuth( huser , hpword )
                            url = 'http://%s:%s/0?11%s=I=0' % ( hip, hport, g_video_paused )
                            r = requests.post(url=url, auth=auth)
                            if (degug_mode == "Yes"):
                                xbmc.executebuiltin('Notification(%s, Video Paused - Scene Active - Night Mode Off, %d, %s)'%(__addonname__,time1, __icon__))
                                print("INSTEON Addon - Video Paused - Scene Active - Night Mode Off")
                                print("INSTEON Addon - Group (Scene) ID: " + g_video_paused)
                                print("INSTEON Addon - HTTP URL: " + url)
                else:
                    if (degug_mode == "Yes"):
                        xbmc.executebuiltin('Notification(%s, Video Paused - Scene Inactive, %d, %s)'%(__addonname__,time1, __icon__))
                        print("INSTEON Addon - Video Paused - Scene Inactive")


#Check unpause state - is there a better way?
            if (VPAUSE == 1):
                if not xbmc.getCondVisibility('Player.Paused'):
                    VPAUSE = 0
                    if (str(settings.getSetting("video_resumed")) == "Yes"):
                        if (str(settings.getSetting("video_resume_gid")) == ""):
                            if (degug_mode == "Yes"):
                                xbmc.executebuiltin('Notification(%s, Video Resumed - Scene Active - ID Not Set, %d, %s)'%(__addonname__,time1, __icon__))
                                print("INSTEON Addon - Video Resumed - Scene Active - ID Not Set")
                            else:
                                xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,plugin_gid, time1, __icon__))
                        else:
                            if (night_mode == "Yes"):
                                if (night_switch == 1):
                                    auth=HTTPBasicAuth( huser , hpword )
                                    url = 'http://%s:%s/0?11%s=I=0' % ( hip, hport, g_video_resumed )
                                    r = requests.post(url=url, auth=auth)
                                    if (degug_mode == "Yes"):
                                        xbmc.executebuiltin('Notification(%s, Video Resumed - Scene Active - Night Mode On - Is Night, %d, %s)'%(__addonname__,time1, __icon__))
                                        print("INSTEON Addon - Video Resumed - Scene Active - Night Mode On - Is Night")
                                        print("INSTEON Addon - Group (Scene) ID: " + g_video_resumed)
                                        print("INSTEON Addon - HTTP URL: " + url)
                                else:
                                    if (degug_mode == "Yes"):
                                        xbmc.executebuiltin('Notification(%s, Video Resumed - Scene Active - Night Mode On - Not Night, %d, %s)'%(__addonname__,time1, __icon__))
                                        print("INSTEON Addon - Video Resumed - Scene Active - Night Mode On - Not Night")
                            else:
                                auth=HTTPBasicAuth( huser , hpword )
                                url = 'http://%s:%s/0?11%s=I=0' % ( hip, hport, g_video_resumed )
                                r = requests.post(url=url, auth=auth)
                                if (degug_mode == "Yes"):
                                    xbmc.executebuiltin('Notification(%s, Video Resumed - Scene Active - Night Mode Off, %d, %s)'%(__addonname__,time1, __icon__))
                                    print("INSTEON Addon - Video Resumed - Scene Active - Night Mode Off")
                                    print("INSTEON Addon - Group (Scene) ID: " + g_video_resumed)
                                    print("INSTEON Addon - HTTP URL: " + url)
                    else:
                        if (degug_mode == "Yes"):
                            xbmc.executebuiltin('Notification(%s, Video Resumed - Scene Inactive, %d, %s)'%(__addonname__,time1, __icon__))
                            print("INSTEON Addon - Video Resumed - Scene Inactive")
            

        else:
            VIDEO = 0
            AUDIO = 1

        if xbmc.Player().isPlayingAudio() == True:
#Check unpause state - is there a better way?
            if xbmc.getCondVisibility('Player.Paused'):
                if (str(settings.getSetting("audio_paused")) == "Yes"):
                    if (str(settings.getSetting("audio_pause_gid")) == ""):
                        if (degug_mode == "Yes"):
                            xbmc.executebuiltin('Notification(%s, Audio Paused - Scene Active - ID Not Set, %d, %s)'%(__addonname__,time1, __icon__))
                            print("INSTEON Addon - Audio Paused - Scene Active - ID Not Set")
                        else:
                            xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,plugin_gid, time1, __icon__))
                    else:
                        if (night_mode == "Yes"):
                            if (night_switch == 1):
                                APAUSE = 1
                                auth=HTTPBasicAuth( huser , hpword )
                                url = 'http://%s:%s/0?11%s=I=0' % ( hip, hport, g_audio_paused )
                                r = requests.post(url=url, auth=auth)
                                if (degug_mode == "Yes"):
                                    xbmc.executebuiltin('Notification(%s, Audio Paused - Scene Active - Night Mode On - Is Night, %d, %s)'%(__addonname__,time1, __icon__))
                                    print("INSTEON Addon - Audio Paused - Scene Active - Night Mode On - Is Night")
                                    print("INSTEON Addon - Group (Scene) ID: " + g_audio_paused)
                                    print("INSTEON Addon - HTTP URL: " + url)
                            else:
                                if (degug_mode == "Yes"):
                                    xbmc.executebuiltin('Notification(%s, Audio Paused - Scene Active - Night Mode On - Not Night, %d, %s)'%(__addonname__,time1, __icon__))
                                    print("INSTEON Addon - Audio Paused - Scene Active - Night Mode On - Not Night")
                        else:
                            APAUSE = 1
                            auth=HTTPBasicAuth( huser , hpword )
                            url = 'http://%s:%s/0?11%s=I=0' % ( hip, hport, g_audio_paused )
                            r = requests.post(url=url, auth=auth)
                            if (degug_mode == "Yes"):
                                xbmc.executebuiltin('Notification(%s, Audio Paused - Scene Active - Night Mode Off, %d, %s)'%(__addonname__,time1, __icon__))
                                print("INSTEON Addon - Audio Paused - Scene Active - Night Mode Off")
                                print("INSTEON Addon - Group (Scene) ID: " + g_audio_paused)
                                print("INSTEON Addon - HTTP URL: " + url)
                else:
                    if (degug_mode == "Yes"):
                        xbmc.executebuiltin('Notification(%s, Audio Paused - Scene Inactive, %d, %s)'%(__addonname__,time1, __icon__))
                        print("INSTEON Addon - Audio Paused - Scene Inactive")
                         
#Check unpause state - is there a better way?
            if (APAUSE == 1):
                if not xbmc.getCondVisibility('Player.Paused'):
                    APAUSE = 0
                    if (str(settings.getSetting("audio_resumed")) == "Yes"):
                        if (str(settings.getSetting("audio_resume_gid")) == ""):
                            if (degug_mode == "Yes"):
                                xbmc.executebuiltin('Notification(%s, Audio Resumed - Scene Active - ID Not Set, %d, %s)'%(__addonname__,time1, __icon__))
                                print("INSTEON Addon - Audio Resumed - Scene Active - ID Not Set")
                            else:
                                xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,plugin_gid, time1, __icon__))
                        else:
                            if (night_mode == "Yes"):
                                if (night_switch == 1):
                                    auth=HTTPBasicAuth( huser , hpword )
                                    url = 'http://%s:%s/0?11%s=I=0' % ( hip, hport, g_audio_resumed )
                                    r = requests.post(url=url, auth=auth)
                                    if (degug_mode == "Yes"):
                                        xbmc.executebuiltin('Notification(%s, Audio Resumed - Scene Active - Night Mode On - Is Night, %d, %s)'%(__addonname__,time1, __icon__))
                                        print("INSTEON Addon - Audio Resumed - Scene Active - Night Mode On - Is Night")
                                        print("INSTEON Addon - Group (Scene) ID: " + g_audio_resumed)
                                        print("INSTEON Addon - HTTP URL: " + url)
                                else:
                                    if (degug_mode == "Yes"):
                                        xbmc.executebuiltin('Notification(%s, Audio Resumed - Scene Active - Night Mode On - Not Night, %d, %s)'%(__addonname__,time1, __icon__))
                                        print("INSTEON Addon - Audio Resumed - Scene Active - Night Mode On - Not Night")
                            else:
                                auth=HTTPBasicAuth( huser , hpword )
                                url = 'http://%s:%s/0?11%s=I=0' % ( hip, hport, g_audio_resumed )
                                r = requests.post(url=url, auth=auth)
                                if (degug_mode == "Yes"):
                                    xbmc.executebuiltin('Notification(%s, Audio Resumed - Scene Active - Night Mode Off, %d, %s)'%(__addonname__,time1, __icon__))
                                    print("INSTEON Addon - Audio Resumed - Scene Active - Night Mode Off")
                                    print("INSTEON Addon - Group (Scene) ID: " + g_audio_resumed)
                                    print("INSTEON Addon - HTTP URL: " + url)
                    else:
                        if (degug_mode == "Yes"):
                            xbmc.executebuiltin('Notification(%s, Audio Resumed - Scene Inactive, %d, %s)'%(__addonname__,time1, __icon__))
                            print("INSTEON Addon - Audio Resumed - Scene Inactive")

#Night Mode Timer Check

#Get current Hour
    now = datetime.datetime.today()
    hour = int(now.hour)
    if (off_time < on_time):
        if (hour < on_time and hour <= off_time):
            night_switch = 1
        else:
            if (hour >= on_time and hour <= (off_time + 24)):
                night_switch = 1
            else:
                night_switch = 0
    else:
        if (hour >= on_time and hour <= off_time):
            night_switch = 1
        else:
            night_switch = 0

    xbmc.sleep(100)



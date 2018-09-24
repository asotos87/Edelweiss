#!/usr/bin/env python

import urllib
import re
import csv
from bs4 import BeautifulSoup


class Parser():


    def teams(self):
            teams = ["BOS","BKN","NY","PHI","TOR","GS","LAC","LAL","PHO","SAC",
                     "CHI","CLE","DET","IND","MIL","DAL","HOU","MEM","NO","SA",
                     "ATL","CHA","MIA","ORL","WAS","DEN","MIN","OKC","POR","UTAH"]
            return teams


    def parsingRosterData(self,team):
    """We parse the data from http://espn.com/nba/team/roster/_/name/<team_name>"""
        nameList = []
        number = []
        sal= []
        salary = []
        college =[]
        age= []
        position =[]
        link = []
        html = urllib.urlopen("http://www.espn.com/nba/team/roster/_/name/" + str(team))
        print (html)
        htmltext = html.read()
        bs0bj = BeautifulSoup(htmltext,"lxml")
        length = len(bs0bj.findAll("table")[0].findAll("tr")[2:])
        for jj in range(0, length):
            constant = bs0bj.findAll("table")[0].findAll("tr")[2 + jj]
            number.append(str(constant.findAll("td")[0]).split(">")[1].split("<")[0])
            link_name = constant.findAll("td")[1].findAll("a")[0]
            link.append(str(link_name).split(" ")[1].split(">")[0].split("=")[1])
            nameList.append(str(link_name).split(">")[1].split("<")[0])
            position.append(str(constant.findAll("td")[2]).split(">")[1].split("<")[0])
            age.append(str(constant.findAll("td")[3]).split(">")[1].split("<")[0])
            HT = str(constant.findAll("td")[4]).split(">")[1].split("<")[0]
            WT = str(constant.findAll("td")[5]).split(">")[1].split("<")[0]
            college.append(str(constant.findAll("td")[6]).split(">")[1].split("<")[0])
            sal.append(str(constant.findAll("td")[7]).split(">")[1].split("<")[0])

        for jj in range(0, length):
            salary.append(re.sub(r'\W+', "", sal[jj])) #clean all the additional useless things like $12,345,567

        return nameList,number,salary,college,age,position,link


    def parsingPlayersData(self):
        team = "BOS" #example
        nameList,number,salary,college,age,position,link = self.parsingRosterData(team)
        gamelog = re.sub("http://www.espn.com/nba/player","http://www.espn.com/nba/player/gamelog",link[13]) #example
        html2 = urllib.urlopen(gamelog[1:-1])
        htmltext = html2.read()
        bs0bj = BeautifulSoup(htmltext,"lxml")
        length = len(bs0bj.findAll('table')[1].findAll("tr")[2:])
        season = (str(bs0bj.findAll("table")[1].findAll("tr")[0].findAll("td")).split(">")[1].split("<")[0])
        ddate = []; op=[]; tsco=[];opsco=[];mini=[]; fgm=[]; fga=[]
        fgper=[]; threepm=[]; threepa=[]; threeper=[];ftm=[];fta=[]
        ftper=[];reb=[];ast=[];blk=[];stl=[];pf=[];to=[];pts=[]
        for jj in range(0,length):
            const = bs0bj.findAll("table")[1].findAll("tr")[2+jj]
            date = str(const.findAll("td")[0]).split(">")[1].split("<")[0]
            try:
                if date[-1].isdigit():
                    ddate.append(date)
                    op.append(str(const.findAll("td")[1].findAll("a")[1]).split(">")[1].split("<")[0]) #opponent
                    linkbsco = (str(const.findAll("td")[1].findAll("a")[0]).split(">")[0].split("<")[1].split('=')[1])[1:-1] #boxscorelink
                    score = str(const.findAll("td")[2].findAll("a")[0]).split(">")[1].split("<")[0]
                    tsco.append(score.split("-")[0])
                    opsco.append(score.split("-")[1])
                    mini.append(str(const.findAll("td")[3]).split(">")[1].split("<")[0])
                    fg = str(const.findAll("td")[4]).split(">")[1].split("<")[0]
                    fgm.append(fg.split("-")[0])
                    fga.append(fg.split("-")[1])
                    fgper.append(str(const.findAll("td")[5]).split(">")[1].split("<")[0])
                    threep = str(const.findAll("td")[6]).split(">")[1].split("<")[0]
                    threepm.append(threep.split("-")[0])
                    threepa.append(threep.split("-")[1])
                    threeper.append(str(const.findAll("td")[7]).split(">")[1].split("<")[0])
                    ft = str(const.findAll("td")[8]).split(">")[1].split("<")[0]
                    ftm.append(ft.split("-")[0])
                    fta.append(ft.split("-")[1])
                    ftper.append(str(const.findAll("td")[9]).split(">")[1].split("<")[0])
                    reb.append(str(const.findAll("td")[10]).split(">")[1].split("<")[0])
                    ast.append(str(const.findAll("td")[11]).split(">")[1].split("<")[0])
                    blk.append(str(const.findAll("td")[12]).split(">")[1].split("<")[0])
                    stl.append(str(const.findAll("td")[13]).split(">")[1].split("<")[0])
                    pf.append(str(const.findAll("td")[14]).split(">")[1].split("<")[0])
                    to.append(str(const.findAll("td")[15]).split(">")[1].split("<")[0])
                    pts.append(str(const.findAll("td")[16]).split(">")[1].split("<")[0])
            except IndexError:
                continue
        return score,tsco,opsco,mini,fgm,fga

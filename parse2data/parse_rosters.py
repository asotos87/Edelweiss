#!/usr/bin/env python
import urllib
import re
import csv
from bs4 import BeautifulSoup

"""We parse the data from http://espn.com/nba/team/roster/_/name/<team_name>"""

class ParsingRosters():
    def parsingRosterData(self,team):
        nameList = []
        number = []
	sal= []
        salary = []
	college =[]
	age= []
	position =[]
        html = urllib.urlopen("http://www.espn.com/nba/team/roster/_/name/" + str(team))
        htmltext = html.read()
        bs0bj = BeautifulSoup(htmltext,"lxml")
        length = len(bs0bj.findAll("table")[0].findAll("tr")[2:])
        for jj in range(0, length):
            constant = bs0bj.findAll("table")[0].findAll("tr")[2 + jj]
            number.append(str(constant.findAll("td")[0]).split(">")[1].split("<")[0])
            link_name = constant.findAll("td")[1].findAll("a")[0]
            link = str(link_name).split(" ")[1].split(">")[0].split("=")[1]
            nameList.append(str(link_name).split(">")[1].split("<")[0])
            position.append(str(constant.findAll("td")[2]).split(">")[1].split("<")[0])
            age.append(str(constant.findAll("td")[3]).split(">")[1].split("<")[0])
            HT = str(constant.findAll("td")[4]).split(">")[1].split("<")[0]
            WT = str(constant.findAll("td")[5]).split(">")[1].split("<")[0]
            college.append(str(constant.findAll("td")[6]).split(">")[1].split("<")[0])
            sal.append(str(constant.findAll("td")[7]).split(">")[1].split("<")[0])
        
        for jj in range(0, length):
            salary.append(re.sub(r'\W+', "", sal[jj])) #clean all the additional useless things like $12,345,567

        return nameList,number,salary,college,age,position


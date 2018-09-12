#!/usr/bin/env python

import re
import datetime
from parse2data.parse_rosters import ParsingRosters
import mysql.connector

class players2data():

    def teams(self):
        teams = ["BOS","BKN","NY","PHI","TOR","GS","LAC","LAL","PHO","SAC",
                 "CHI","CLE","DET","IND","MIL","DAL","HOU","MEM","NO","SA",
                 "ATL","CHA","MIA","ORL","WAS","DEN","MIN","OKC","POR","UTAH"]
        return teams
         
    def database(self):
        a = ParsingRosters()
        cnx = mysql.connector.connect(user='user',password='password',host='localhost',database='NbaTeams')
	cursor = cnx.cursor()
	for team in self.teams():
            name,number,salary,college,age,position = a.parsingRosterData(team.lower())
            query1 = "create table " + str(team) + " (Name VARCHAR(25), Number INT(2),College VARCHAR(28), Age INT(2), Position CHAR(2),Salary INT(8))"
            cursor.execute(query1)
	    for jj in range(0, len(name)):
                query = "INSERT INTO " + str(team) + " values (%s,%s,%s,%s,%s,%s)"
		if salary[jj] == '':
                    salary[jj] = 0
                if number[jj] == "--":
	            number[jj] = 99
	    	cursor.execute(query,(str(name[jj]),number[jj],str(college[jj]),age[jj],str(position[jj]),salary[jj]))
            	cnx.commit()
        cnx.close()


if __name__ == "__main__":

    con = players2data()
    con.database()

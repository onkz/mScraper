import sys
import orjson
import requests
import unittest
import warnings
import opengraph_py3
import AdvancedHTMLParser

global message
message = " \nmScraper v1.29 by onkz - https://github.com/onkz \n-------------------- \nUsage: \n    --plain <id> = Fetch plain song data. \n    --cover <id> = Fetch song cover art. \n    --json <id> = Fetch JSON song data. \n    --mp3 <id> = Fetch song mp3 link. \n "

def mParser(x):
	try:
		parser_apiv1 = AdvancedHTMLParser.AdvancedHTMLParser()
		parser_public = AdvancedHTMLParser.AdvancedHTMLParser()
		user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
		headers = {'User-Agent': user_agent}
		matter_link_apiv1 = ("https://api.matter.online/api/v1/open-graph/tracks/" + sys.argv[2] + "/embedded")
		matter_link_public = ("https://app.matter.online/tracks/" + sys.argv[2])
		m_https_get_apiv1 = requests.get(matter_link_apiv1)
		m_https_get_public = requests.get(matter_link_public,headers=headers)
		m_data_apiv1 = (m_https_get_apiv1.text)
		m_data_public = (m_https_get_public.text)
		parser_apiv1.parseStr(m_data_apiv1)
		parser_public.parseStr(m_data_public)
		m_data_raw = parser_apiv1.getAllNodes()
		m_data_opengraph_raw = opengraph_py3.OpenGraph(html=m_data_public)
		m_data_file_mp3 = parser_apiv1.getElementsByTagName("source")
		jsonNameVar = "{\'name\': \'"
		jsonCoverVar = "\', \'cover\': \'"
		jsonSongVar = "\', \'mp3\': \'"
		if len((str(m_data_file_mp3)[47:])[:-12]) > 10:
			m_moved_json = ((str(m_data_opengraph_raw)))
			m_corrected_json = ((((str(m_moved_json)).replace("\'", "\"")).replace("None", "\"None\"")).replace("False", "\"False\"")).replace("True", "\"True\"")
			m_data_opengraph_json = orjson.loads(m_corrected_json)
			jsonVar = (jsonNameVar + m_data_opengraph_json['title'] + jsonCoverVar + m_data_opengraph_json['image'] + jsonSongVar + ((str(m_data_file_mp3)[47:])[:-12]) + "\'}")
			if x == 5:
				print(m_data_opengraph_json['title'])
				print((str(m_data_file_mp3)[47:])[:-12])
				print(m_data_opengraph_json['image'])
			elif x == 7:
				print(jsonVar)
			elif x == 9:
				print(m_data_opengraph_json['image'])
			elif x == 11:
				print((str(m_data_file_mp3)[47:])[:-12])
			else:
				print(" \nError: Argument was not passed correctly. Restart mScraper. \n " + message)
		else:
			print(" \nError: This song is either a Matter Artist Club song, or this song does not exist. \n " + message)
	except ValueError:
		print(" \nError: This song is either a Matter Artist Club song, or this song does not exist. \n " + message)
	except requests.exceptions.RequestException:
		print(" \nError: Could not connect to Matter services. \n " + message)

def run(x):
	with warnings.catch_warnings():
		warnings.simplefilter("ignore")
		mParser(x)

if len(sys.argv) > 1:
	if sys.argv[1] == "--plain" and int(sys.argv[2]) > 0:
		run(5)
	elif sys.argv[1] == "--json" and int(sys.argv[2]) > 0:
		run(7)
	elif sys.argv[1] == "--cover" and int(sys.argv[2]) > 0:
		run(9)
	elif sys.argv[1] == "--mp3" and int(sys.argv[2]) > 0:
		run(11)
	else:
		print(" \nError: Invalid arguments given. Restart mScraper. \n " + message)
else:
	print(message)

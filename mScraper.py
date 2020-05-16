import sys
import json
import requests
import unittest
import warnings
import opengraph
import AdvancedHTMLParser

def mParser(x):
	parser_apiv1 = AdvancedHTMLParser.AdvancedHTMLParser()
	parser_public = AdvancedHTMLParser.AdvancedHTMLParser()
	matter_link_apiv1 = ("https://api.matter.online/api/v1/open-graph/tracks/" + sys.argv[2] + "/embedded")
	matter_link_public = ("https://app.matter.online/tracks/" + sys.argv[2])
	m_https_get_apiv1 = requests.get(matter_link_apiv1)
	m_https_get_public = requests.get(matter_link_public)
	m_data_apiv1 = (m_https_get_apiv1.text)
	m_data_public = (m_https_get_public.text)
	parser_apiv1.parseStr(m_data_apiv1)
	parser_public.parseStr(m_data_public)
	m_data_raw = parser_apiv1.getAllNodes()
	m_data_opengraph_raw = opengraph.OpenGraph(html=m_data_public)
	# m_data_opengraph_json = m_data_opengraph_raw.to_json()
	m_data_opengraph_json = (json.loads((str(m_data_opengraph_raw)).replace("\'", "\"")))
	m_data_file_mp3 = parser_apiv1.getElementsByTagName("source")
	#
	# useful variables list:
	#
	# m_data 		- [raw aHTMLp] all page data.
	# m_data_song		- [raw aHTMLp] the artist + song name.
	# m_data_file_image	- [raw aHTMLp] the link to the song cover artwork.
	# m_data_file_mp3	- [raw aHTMLp] the link to the song mp3 file.
	# m_name_artist		- parsed artist name.
	# m_name_song		- parsed song name.
	#
	if x == 5:
		print(m_data_opengraph_json['title'])
		print((str(m_data_file_mp3)[47:])[:-12])
		print(m_data_opengraph_json['image'])
	elif x == 7:
		print(m_data_opengraph_json)
		print(m_data_file_mp3)
	elif x == 9:
		print(m_data_file_mp3)
	else:
		print("Error: Argument was not passed correctly. Restart mScraper.")

def run(x):
	with warnings.catch_warnings():
		warnings.simplefilter("ignore")
		mParser(x)

if len(sys.argv) > 1:
	if sys.argv[1] == "--plain" and int(sys.argv[2]) > 0:
		run(5)
	elif sys.argv[1] == "--json" and int(sys.argv[2]) > 0:
		run(7)
	elif sys.argv[1] == "--mp3" and int(sys.argv[2]) > 0:
		run(9)
	else:
		print(" \nmScraper v0.97 by onkz - https://github.com/onkz \n-------------------- \nusage: \n    --plain <id> = fetch plain song data \n    --json <id> = fetch JSON song data \n    --mp3 <id> = fetch song mp3 link \n ")
else:
	print(" \nmScraper v0.97 by onkz - https://github.com/onkz \n-------------------- \nusage: \n    --plain <id> = fetch plain song data \n    --json <id> = fetch JSON song data \n    --mp3 <id> = fetch song mp3 link \n ")



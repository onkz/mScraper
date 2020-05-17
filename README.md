# mScraper
### Python-based song scraper for the Matter music platform.

mScraper will output basic song data from Matter.Online.  
The purpose of this program is to provide Matter integration functionality to any program that wishes to add it.  

mScraper was developed in Python 3. No guarantee of anything working in Python 2.
```
mScraper.py --plain <id> - fetch full song data from ID.  
mScraper.py --cover <id> - fetch cover art from song ID.
mScraper.py  --json <id> - fetch data in JSON format.  
mScraper.py   --mp3 <id> - fetch MP3 from song ID.
```
As of v1.02, JSON output is now fixed and working as intended.

## Dependencies
#### mScraper requires these libraries to be installed:
* LXML
* Requests
* OpenGraph
* AdvancedHTMLParser

## Known Issues (as of v1.02)
* mScraper works on Linux/macOS - it doesn't run properly on Windows hosts.

## Upcoming Features
##### Version v1.1
* Automatic installation script for Debian/Ubuntu.
##### Version v2.0
* Full compatibility with Windows hosts.
* Automatic installation script for Windows hosts.
* Ability to store output into text files.
* Ability to output only song cover artwork with "--cover".

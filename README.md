# mScraper
### Python-based song scraper for the Matter music platform.

mScraper will output basic song data from Matter.Online.  
The purpose of this program is to provide Matter integration functionality to any program that wishes to add it.  

mScraper was developed in Python 3. It will not work in Python 2.  
Pre-compiled binaries will soon be available.
```
mScraper.py --plain <id> - fetch full song data from ID.  
mScraper.py --cover <id> - fetch cover art from song ID.
mScraper.py  --json <id> - fetch data in JSON format.  
mScraper.py   --mp3 <id> - fetch MP3 from song ID.
```
~As of v1.02, JSON output is now fixed and working as intended.~    
As of v1.29, JSON output is actually fixed and working and won't break when on different OS's!

## Dependencies
#### mScraper.py requires these libraries to be installed:
* LXML
* URLLIB3
* Requests
* OpenGraph (sometimes called opengraph_py3 on different OS's)
* BeautifulSoup
* AdvancedHTMLParser 

#### For easier use, pre-compiled binaries will be available very soon.

## Known Issues (as of v1.29)
* ~mScraper works on Linux/macOS - it doesn't run properly on Windows hosts.~
* ~Windows hosts have trouble using the OpenGraph library.~

## Upcoming Features
##### Version 2
* Full compatibility with Windows hosts.
* Automatic installation script for Windows hosts.
* Automatic installation script for Debian/Ubuntu.
* Ability to store mScraper output into text files.

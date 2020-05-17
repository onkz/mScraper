# mScraper
### Python-based song scraper for the Matter music platform.

mScraper will output basic song data from Matter.Online.  
The purpose of this program is to provide Matter integration functionality to any program that wishes to add it.  

mScraper was developed in Python 3. No guarantee of anything working in Python 2.

## Usage
#### mScraper will take these arguments:
```
mScraper.py --plain <id> - fetch full song data from ID.  
mScraper.py  --json <id> - fetch song data in JSON format.  
mScraper.py   --mp3 <id> - fetch MP3 from specified song ID.
```

## Dependencies
#### mScraper requires these libraries to be installed:
* LXML
* Requests
* OpenGraph
* AdvancedHTMLParser

## Known Issues
* mScraper works on Linux/macOS - it doesn't run properly on Windows hosts.

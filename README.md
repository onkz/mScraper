# mScraper
### Python-based song scraper for the Matter music platform.

Requires these libraries to be installed:
* LXML
* Requests
* OpenGraph
* AdvancedHTMLParser

mScraper was developed in Python 3. No guarantee of anything working in Python 2.

## Usage
#### mScraper will take these arguments:
mScraper.py --plain [id]  - fetch full song data from ID.  
mScraper.py --json [id]   - fetch song data from ID, in JSON format.  
mScraper.py --mp3 [id]    - fetch MP3 from specified song ID.  

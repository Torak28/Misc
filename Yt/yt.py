import os
import time
links = [
	'https://www.youtube.com/watch?v=xV47lwuqT3U'
]

for link in links:
	os.system('youtube-dl ' + link)
	time.sleep(5)

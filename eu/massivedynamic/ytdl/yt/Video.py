import lxml
from lxml import etree
import urllib

class Title():
	def __init__(self, url):
		self.url = url

	def title(self):
		youtube = etree.HTML(urllib.urlopen(self.url).read())
		video_title = youtube.xpath("//span[@id='eow-title']/@title")
		return ''.join(video_title)
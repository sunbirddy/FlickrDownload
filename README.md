# FlickrDownload
This simple script helps you download flickr images (one at a time or bulky download) based on various criteria (name tag, geo tag, taken time, user ID, set ID, url etc.) using Python. Unlike many other projects aiming to download images by photo url or photo ID, this script can be more personalized. You can specify different senarios to drag out the images you want. For example, if you would like just photos from San Francisco, then specify the name tag to "San Francisco", all the retieved images will be related with San Francisco to some extent. Or if you aim to get photos around one particular area, you can either locate a bouding box or set a circle around a geo-center. All the usage details are listed in the flickrDownload.py file. Any unwanted criteria, just comment that line out and you are good to go. 

Before using, please make sure you already have Python 2.7+ and Python Flickr API kit (from http://stuvel.eu/flickrapi) installed on your computer. And you have a registered Flickr API key and secret. Happy downloading!

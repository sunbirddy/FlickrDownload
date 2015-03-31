# FlickrDownload
This simple script helps you download flickr images (one at a time or bulky download) based on various criteria (name tag, geo coordinats, taken time, user ID, set ID, url etc.) using Python. Unlike many other projects aiming to download images by photo url or photo ID, this script can be more personalized. You can specify different senarios to drag out the images you want. For example, if you would like just photos from San Francisco, then specify the name tag to "San Francisco", all the retieved images will be related with San Francisco to some extent. Or if you aim to get photos around one particular area, you can either locate a bouding box or set a circle around a geo-center. All the usage details are listed in the flickrDownload.py file. Any unwanted criteria, just comment that line out and you are good to go. 

Before using, please make sure you already have Python 2.7+ and Python Flickr API kit (from http://stuvel.eu/flickrapi) installed on your computer. And you have a registered Flickr API key and secret. Happy downloading!

Steps to use: 
1. Install Python 2.7+ in your computer. Currently because the Python Flickr API kit doesn't support Python 3.3+, we recommend you to use Python 2.7. You can download the newest version at https://www.python.org/downloads/.
2. Install the Python Flickr API kit, instructions at http://stuvel.eu/flickrapi. 
   If you don't have Setup-tools installed, type:
      sudo apt-get install python-setuptools
   Then type
      easy_install flickrapi
   to install the api toolkit. You can then always update to the latest version using:
      easy_install -U flickrapi
3. Use any text editor to open script flickrDownload.py, fill in your Flickr API key and secret. Change any criteria you desire or unwanted. Remmeber to change the folder name to store your images and its associated metadata. 
4. Open a terminal, run the script
      python /DIRECTORY TO THE SCRIPT/flickrDownload.py
You will see the retrived photo ID, geo coordinates displayed in the terminal, and all the photos downloaded to your specified folder.
5. Sometimes there will be error occurs like internet error. This is because your network doesn't connect with Flickr stablely. Try to find a stable network before downloading the data or download the images by batches (e.g., use min_taken_time and max_taken_time to restrict the number of retrieved photos at a time and download multiple times.)

import flickrapi    # Beej's Python Flickr API from http://stuvel.eu/flickrapi
import urllib, urlparse
import os
# import socket

if __name__ == '__main__':

    api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'  # Obtained from https://www.flickr.com/services/api/
    api_secret = 'XXXXXXXXXXXXXXXXX'
    flickr = flickrapi.FlickrAPI(api_key, api_secret, cache=True)

    try:
        photos = flickr.walk(# Query text
                             # text = "stanford",
                             # Geo-location by locating bounding box
                             # bbox = {-180.0,-90.0,180.0,90.0},
                             # Privacy filter
                             ispublic = '1',
                             # Geo-location by specifying lat/lon and radius(default km)
                             lat = '37.428620',
                             lon = '-122.170723',
                             radius = '2',
                             # Taken time constraint
                             min_taken_date = '2014-12-20',
                             max_taken_date = '2014-12-31',
                             # Accuracy level
                             accuracy = '16',
                             # Content type, '1' means photos only. You can also use '7' to include screenshots and all other image type
                             content_type = '1',
                             # Has geotag or not
                             has_geo = '1',
                             # Media type: photos. You can also use 'all' here to include both photos and videos
                             media = 'photos',
                             # Extra tag: description, url, geo coordinates, tags, license type, image taken time, image dimensions, views
                             extras = 'description, url_n, geo, tags, license, date_taken, o_dims, views'
                             )
    except Exception:
        print 'No photos found!'

    # Open a new txt file to store meta information associated with each photo
    # f = open('/home/yzhu25/Downloads/Campus/all.txt','a+')
    f = open('/Users/yizhu/Downloads/Campus/all.txt','a+')
    
    exceptionNum = 0
    try:
        count = 0
        for photo in photos:
            myurl = photo.get('url_n')
            myid = photo.get('id')
            lat = photo.get('latitude')
            if not lat:
                lat = None
            lon = photo.get('longitude')
            if not lon:
                lon = None
            username = photo.get('owner')
            if not username:
                username = None
            title = photo.get('title')
            if not title:
                title = None
            geo = photo.get('geo')
            if not geo:
                geo = None
            date = photo.get('datetaken')
            if not date:
                date = None
            # descript = photo[0].get('value')
            for description in photo:
                descript = description.text
            if not descript:
                descript = None
            # tags = photo.get('tags')
            # if not tags:
            #     tags = None
            license = photo.get('license')
            context = photo.get('context')
            views = photo.get('views')
            height = photo.get('height_n')
            width = photo.get('width_n')

            if myurl is not None and myid is not None:
                # print myurl
                image = urllib.URLopener()
                image.retrieve(myurl, os.path.join("/Users/yizhu/Downloads/Campus/FlickrCampus", (myid + '.jpg')))
                # image.retrieve(myurl, os.path.join("/home/yzhu/Downloads/Flickr_images", os.path.basename(urlparse.urlparse(myurl).path))) 
                print 'downloading:', myid, lat, lon
                f.write('%s: ' % myid)
                f.write('%s: ' % lat)
                f.write('%s: ' % lon)
                f.write('%s: ' % username)
                f.write('%s: ' % date)
                f.write('%s: ' % context)
                f.write('%s: ' % height)
                f.write('%s: ' % width)
                f.write('%s: ' % title)
                f.write('%s: ' % descript)
                # f.write('%s ' % tags)
                f.write('%s: ' % views)
                f.write('%s:  \r\n' % license)
            
                count = count + 1
                print count
                
    except Exception: 
        exceptionNum = exceptionNum + 1
        # print exceptionNum
        pass

    f.close()

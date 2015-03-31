import flickrapi  # Beej's Python Flickr API from http://stuvel.eu/flickrapi
import urllib, urlparse
import os
# import socket

if __name__ == '__main__':

    api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'  # Obtained from https://www.flickr.com/services/api/
    api_secret = 'XXXXXXXXXXXXXXXXX'
    flickr = flickrapi.FlickrAPI(api_key, api_secret, cache=True)

    try:
        photos = flickr.walk(# Name
                             # text = "stanford",
                             # geo-location by locating bounding box
                             # bbox = {-122.181885, 37.422008, -122.160299, 37.436765},
                             # geo-location by specifying lat/lon and radius
                             lat = '37.428620',
                             lon = '-122.170723',
                             radius = '2',
                             # Taken time
                             min_taken_date = '2014-12-23',
                             max_taken_date = '2014-12-30',
                             # Accuracy level
                             accuracy = '16',
                             # Content type
                             content_type = '1',
                             # Has geotag or not?
                             has_geo = '1',
                             # Media type: photo
                             media = 'photos',
                             # Extra tag: url, geo coordinates
                             extras = 'url_z,geo'
                             )
    except Exception:
        print 'No photos found!'

    # Open a new txt file to store meta information associated with each photo
    f = open('/home/yzhu/Downloads/imageInfo_2.txt','a+')
    exceptionNum = 0
    try:
        count = 0
        for photo in photos:
            # myurl = photo.getURL(size='Medium', urlType='source')
            myurl = photo.get('url_z')
            myid = photo.get('id')
            # mygeo = photo.geo_getLocation(api_key,myid)
            lon = photo.get('longitude')
            lat = photo.get('latitude')
            # author = photo.get('owner_name')
            # date = photo.get('date_taken')
            if myurl is not None and myid is not None and lon is not None and lat is not None:
                # print myurl
                image = urllib.URLopener()
                image.retrieve(myurl, os.path.join("/home/yzhu/Downloads/flickr1", (myid + '.jpg')))
                # image.retrieve(myurl, os.path.join("/home/yzhu/Downloads/Flickr_images", os.path.basename(urlparse.urlparse(myurl).path))) 
                print 'downloading:', myid, lon, lat
                f.write('%s  ' % myid)
                f.write('%s  ' % lon)
                f.write('%s  \r' % lat)
                count = count + 1
                print count
                            # f.write('%s  ' % author)
                # f.write('%s  \r'% date)
    except Exception,ex: # XXX what error?
        # print 'error'
        print ex
        exceptionNum = exceptionNum + 1
        print exceptionNum
        pass

    f.close()

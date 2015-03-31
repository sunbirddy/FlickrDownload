import flickrapi
import urllib, urlparse
import os
# import socket

if __name__ == '__main__':

    api_key = 'd80e22556ee7270de4648a8d74e902c3'
    api_secret = 'b46e39656fee2b2e'
    flickr = flickrapi.FlickrAPI(api_key, api_secret, cache=True)

    try:
        photos = flickr.walk(# text = "stanford",
                             # bbox = {-122.181885, 37.422008, -122.160299, 37.436765},
                             # bbox = {-180.0,-90.0,180.0,90.0},
                             lat = '37.428620',
                             lon = '-122.170723',
                             radius = '2',
                             min_taken_date = '2014-12-23',
                             max_taken_date = '2014-12-30',
                             accuracy = '16',
                             content_type = '1',
                             has_geo = '1',
                             media = 'photos',
                             extras = 'url_z,geo'
                             )
    except Exception:
        print 'No photos found!'

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

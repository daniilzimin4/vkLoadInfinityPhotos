# VK downloader

How to load many photos (>500k) to the different albums

## Alghoritm

Code automatically load photos to the album, until the VK API block (maximum 2000 photos per 2 hours, and 10k for the 24 hours). After album reached maximum count of photos (it is 10k), code auto make new album.\
Album id store in the simple data base.
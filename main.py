import vk_api
from time import sleep
from vk_config import *
import logging
from db_work import *

db = Database()

logging.basicConfig(filename="log.log", level=logging.INFO)
log = logging.getLogger("script")
log.info("start")

vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()

upload = vk_api.VkUpload(vk_session)

cnt = db.getCnt()
ALBUM = db.getAlbum()

while True:
    if cnt == 10000:
        new_album = vk.photos.createAlbum(title="sorry")
        ALBUM = new_album['id']
        vk.photos.editAlbum(album_id=ALBUM, privacy_view='only_me')
        db.updAlbum(ALBUM)
        cnt = 0
    try:
        upload.photo(photos="photo.jpg", album_id=ALBUM)
        cnt += 1
    except vk_api.exceptions.ApiError:
        db.updCnt(cnt)
        sleep(18000)
    except Exception as error:
        logging.exception(error)

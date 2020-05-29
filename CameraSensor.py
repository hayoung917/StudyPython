# import time
# import picamera

# camera = picamera.PiCamera()

# try:
#     camera.start_preview()
#     time.sleep(10)
#     camera.stop_preview()
# finally:
#     camera.close()

# import picamera # 영상녹화

# with picamera.PiCamera() as camera:
#     camera.resolution = (640,480)
#     camera.start_preview()
#     camera.start_recording('foo.h264')
#     camera.wait_recording(60)
#     camera.stop_recording()
#     camera.stop_preview()

import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1200,720)
    camera.start_preview()
    camera.exposure_compensation = 2
    camera.exposure_mode = 'auto'
    camera.meter_mode = 'matrix'
    camera.image_effect = 'none'
    time.sleep(2)
    camera.exif_tags['IFD0.Artist'] = 'Kim'
    camera.exif_tags['IFD0.Copyright'] = 'Copyleft Kim'
    camera.capture('foo.jpg')
    camera.stop_preview()
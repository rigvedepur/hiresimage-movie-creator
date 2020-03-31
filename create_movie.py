import cv2
import argparse
from skimage.io import imread
from progress.bar import IncrementalBar


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="input filenname")
ap.add_argument("-r", "--resolution", required=True, help="output resolution", default='4K')
ap.add_argument("-s", "--step", required=False, help="step size", default=5)
ap.add_argument("-f", "--fps", required=True, help="fps", default=30)
ap.add_argument("-c", "--codec", required=False, help="codec", default='MP4V')
args = vars(ap.parse_args())

# Read input filename and shape
filename = args['input']
image = imread(filename)
(image_height, image_width) = image.shape[:2]

# Assign output screen resolution
resolution = args['resolution']
if resolution == '4K':
    size = (3840, 2160)
elif resolution == '1080p':
    size = (1920, 1080)
elif resolution == '720p':
    size = (1280, 720)
elif resolution == '480p':
    size = (854, 480)
elif resolution == '360p':
    size = (640, 360)
elif resolution == '240p':
    size = (426, 240)
else:
    size = (1920, 1080)

(screen_width, screen_height) = size


# Read output FPS
fps = int(args['fps'])

# Read step-size for panning in x-direction
step = int(args['step'])

# Read format of output file-extension (.avi or .mp4)
codec = args['codec']
if codec == 'DIVX':
    file_ext = '.avi'
elif codec == 'MP4V':
    file_ext = '.mp4'


# Define output filename
output_filename = 'output_'+str(fps)+'-fps_'+resolution+'-resolution_'+str(step)+'-step'+file_ext


# Inspect ROI array by row (in Y) and by frame (in X)
out = cv2.VideoWriter(output_filename, cv2.VideoWriter_fourcc(*codec), fps, size)

total_frames = int((image_height//screen_height) * (image_width//step))

bar = IncrementalBar('Progress: ', max=total_frames)

for j in [k*screen_height for k in range(image_height//screen_height)]:

    for i in [f*step for f in range(image_width//step)]:

        crop = image[j:j+screen_height, i:i+screen_width, :]
        crop = cv2.cvtColor(crop, cv2.COLOR_RGB2BGR)
        out.write(crop)
        bar.next()


out.release()
bar.finish()

print('Movie saved successfully')



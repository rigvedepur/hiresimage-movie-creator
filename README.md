# Creating a movie from Ultra Hires Images

### Setup instructions

1. Clone or download this repository
	* git clone this [repo](https://github.com/rigvedepur/hiresimage-movie-creator.git)
	* `cd hiresimage-movie-creator`

2. Download the image from source [example curiosity image](https://mars.nasa.gov/resources/24801/curiositys-18-billion-pixel-panorama/?site=msl). For the example video embedded below, I used the M34 version photo which is about 717 MB.

3. Create a virtual environment of python3 and install dependencies
	`pip install -r requirements.txt`

##### Available flags
```
-i --input : input filename that links to the downloaded Images

-r --resolution : output resolution
				Available options: 4K, 1080p, 720p, 480p, 360p, 240p;
				default=4K

-s --step  : defines how many pixels to shift while including them in the movie; default=5

-f --fps   : output frames per second; default=30fps

-c --codec   : output movie file format
				Available options: DIVX (for avi), MP4V (for mp4); default=MP4V
```

##### How to execute the script (Example)
```python
python create_movie.py data/PIA23623_M34.tif -r 4K -s 5 -f 30 -c MP4V`
```
#### Sample video generated from above arguments

[![](http://img.youtube.com/vi/Ri2_X28t9lE/0.jpg)](http://www.youtube.com/watch?v=Ri2_X28t9lE "Mastcam from Curiosity Rover: M34")

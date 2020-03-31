# Creating a movie from Ultra Hires Images

### Setup instructions

1. Download the image from source [example curiosity image](https://www.youtube.com/redirect?redir_token=dfA4GMEeU4k3BJnXCxl-UJDD0bV8MTU4NTcyOTA4MUAxNTg1NjQyNjgx&q=https%3A%2F%2Fmars.nasa.gov%2Fresources%2F24801%2Fcuriositys-18-billion-pixel-panorama%2F%3Fsite%3Dmsl&v=Ri2_X28t9lE&event=video_description)
2. clone or download this repository

		`git clone https://github.com/rigvedepur/hiresimage-movie-creator.git`
		`cd hiresimage-movie-creator`


3. Create a virtual environment of python3 and install dependencies
	`pip install -r requirements.txt`

##### Available flags

`-i --input : input filename that links to the downloaded Images`
`-r --resolution : output resolution
				Available options: 4K, 1080p, 720p, 480p, 360p, 240p`
`-s --step  : defines how many pixels to shift while including them in the movie`
`-f --fps   : output frames per second`
`-c --codec   : output movie file format
				Available options: DIVX (for avi), MP4V (for mp4)`

##### How to execute the script

`python create_movie.py data/PIA23623_M34.tif -r 4K -s 5 -f 30 -c MP4V`

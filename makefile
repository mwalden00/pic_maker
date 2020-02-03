all:
	python3 pic_maker.py
	magick convert pic.ppm pic.png
	rm pic.ppm

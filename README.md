# HaarCascade-Trained-to-detect-my-Watch-
 # I have trained  to detect my watch using opencv and installation notes of opencv has been listed


# In the program facecase.py is the main program
	git clone https://github.com/arunodhayan/HaarCascade-Trained-to-detect-my-Watch-.git 
# The code illustrates that
    	1.The first few lines of code helps to download the images from imagenet.org
    	2.Resize the image based on required pixel i choose(100X100).
   	3.Then there will be unwanted images to remove that create a folder called uglies and unwanted images will be deleted
    	4.Now create a file bg.txt to list negative files for training 

# To train the model
    mkdir data 
    mkdir info
    1.opencv_createsamples -img typeimagename.jpg -bg bg.txt -info info/info.txt -pngoutput info -maxxangle 0.5 -maxyangle 0.5      -maxzangle 0.5 -num 1900 
	    The numimages should be less than the negative image count(Eg if negative image is 1950 use 1900)
    2.opencv_createsamples -info info/info.txt -num 1900 -vec positives.vec 
	    To create positive vector files
    3.opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numstages 12
	    Here the positive must higher and negatives must be half

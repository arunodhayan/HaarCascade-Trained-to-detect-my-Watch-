# Step 1:
    $ sudo apt-get update
    $ sudo apt-get upgrade
    $ sudo apt-get install build-essential cmake pkg-config
    $ sudo apt-get install libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev(16.04)
    $  sudo apt-get install libjpeg-dev libpng-dev libtiff-dev(18.04)
    $ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev(16.04)
    $ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev(18.04)
    $ sudo apt-get install libxvidcore-dev libx264-dev
    $ sudo apt-get install libgtk-3-dev
    $ sudo apt-get install libatlas-base-dev gfortran
    $ sudo apt-get install python2.7-dev python3.5-dev

# Step 2:
# Opencv 
    $ cd ~
    $ wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.1.0.zip
    $ unzip opencv.zip

# opencv_contribute
    $ wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.1.0.zip
    $ unzip opencv_contrib.zip
# for latest version 
    git clone https://github.com/opencv/opencv.git
    $ mkdir build
    $ cd build
    cmake ../
# Install Numpy,Nose,Matplotlib
    $python2 -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose

# Install opencv in python2
    $ cd ~/opencv-3.1.0/
    $ mkdir build
    $ cd build
    $ cmake -D CMAKE_BUILD_TYPE=RELEASE \
        -D CMAKE_INSTALL_PREFIX=/usr/local \
        -D INSTALL_PYTHON_EXAMPLES=ON \
        -D INSTALL_C_EXAMPLES=OFF \
        -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.1.0/modules \
        -D BUILD_EXAMPLES=ON ..
        
        if error occured in the above process
        remove build folder and type mkdir build and cd build
        then cmake ..


# Step 3:
    $make -j4

# If couldn't able to install or if make is broken
    $make clean
    $make

# If make is done 100%
    $sudo make install
    $sudo ldconfig

# Finish your Opencv Install
# python2.7
    $ ls -l /usr/local/lib/python2.7/dist-packages/
    total 2082
    listed

# Step 4:
    # Test your opencv is install
    $ cd ~
    $ python2
    Python 2.7.14 (default, June 6 2017, 12:43:10) 
    [GCC 5.4.0 20160609] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import cv2
    >>> cv2.__version__
    '3.1.0'
    >>>

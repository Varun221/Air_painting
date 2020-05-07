# WebCam_paint
An OpenCV Project

This application allows you to track an object's movement, using which the user can draw on the screen by moving the object around. It also contains a hold feature, in which by showing another object you stop the camera from painting. It is useful in painting disconnected drawings. 
You can select colours and brush sizes according to your choice, by bringing the object's pointer on the palette.

Features - 
1. The application contains a total of 12 colors and 5 brush sizes.
2. The painting can be started and stopped by the buttons in the palette.
3. The Save option lets you save your painting in a "save.png".
4. You can stop and start the painting instantly by creating a hold object.

Here's a Save image - 

![alt text](https://github.com/Varun221/WebCam_paint/blob/master/save.png)


Libraries Used -   
Opencv-Python (v4.0)  
Numpy (v1.18)


Customizing The application- 
The code is open sourced and commented wherever necessary. Feel free to reach out for any suggestions.
Some options for customizing - 
1. To create a marker and holder - use the files hsv.py and hsv_check.py.
   They are made for creating and testing of object detection codes.
2. The pallete has been created keeping the resolution of 900x650 in mind. Changing it will mess up the coordinates.   





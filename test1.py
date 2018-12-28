#!/usr/bin/python3

# print hello
print("Hello world")



import cv2
# using imread() function in cv2
tree_original=cv2.imread('tree.jpg',1)
tree_grey=cv2.imread('tree.jpg',0)
print("colored image")
print(tree_original)
print("grey image")
print(tree_grey)



# using imwrite() func in cv2
cv2.imwrite('tree_gray.jpg',tree_grey)
cv2.imwrite('tree_color.jpg',tree_original)

#using imshow() func in cv2
#      window_name, numpy_image
cv2.imshow('1',tree_grey)
cv2.waitKey(0)





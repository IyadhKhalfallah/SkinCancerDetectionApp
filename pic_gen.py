import imutils
import cv2

TITLE = 'm'
img = cv2.imread(TITLE+'.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
threshold = cv2.threshold(gray,80,255,cv2.THRESH_BINARY_INV)[1]

cont = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cont = imutils.grab_contours(cont)
img_sym = img.copy()

i = 0
biggest_center=(0,0)
biggest_radius = 0

for cnt in cont:
  i+=1
  (x,y),radius = cv2.minEnclosingCircle(cnt)
  center = (int(x),int(y))
  radius = int(radius)
  if (radius>biggest_radius):
    biggest_radius=radius
    biggest_center=center

# get coords based on boundary
lineX,lineY = center
# textY = int((img.shape[0] + textsize[1]) / 2)

# add text centered on image
cv2.line(img_sym,(lineX,0),(lineX,img.shape[0]),(0,0,255),5)

cv2.imwrite(str(TITLE)+'_a.jpg', img_sym) 

cont = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cont = imutils.grab_contours(cont)
img_cont = img.copy()

i = 0

for ct in cont:
  cv2.drawContours(img_cont, [ct], -1, (0,255,0), 3)
  i+=1
cv2.imwrite(str(TITLE)+'_b.jpg', img_cont)

colored = cv2.applyColorMap(gray, cv2.COLORMAP_JET)
cv2.imwrite(str(TITLE)+'_c.jpg', colored) 

cont = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cont = imutils.grab_contours(cont)
img_cont = img.copy()

i = 0
biggest_center=(0,0)
biggest_radius = 0

for cnt in cont:
  i+=1
  (x,y),radius = cv2.minEnclosingCircle(cnt)
  center = (int(x),int(y))
  radius = int(radius)
  if (radius>biggest_radius):
    biggest_radius=radius
    biggest_center=center

# setup text
font = cv2.FONT_HERSHEY_SIMPLEX
text = "Diameter = "+str(format(biggest_radius*0.02, '.2f'))+" mm"

# get boundary of this text
textsize = cv2.getTextSize(text, font, 1, 2)[0]

# get coords based on boundary
textX = int((img.shape[1] - textsize[0]) / 2)
textY = int((img.shape[0] + textsize[1]) / 2)

# add text centered on image
cv2.putText(img_cont, text, (textX, textY ), font, 1, (0, 255, 0), 2)
img_cont = cv2.circle(img_cont,biggest_center,biggest_radius,(0,255,0),2)

cv2.imwrite(str(TITLE)+'_d.jpg', img_cont) 
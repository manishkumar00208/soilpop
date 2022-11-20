from PIL import Image
from statistics import mean
im = Image.open('humus.jpg','r')
pix_val = list(im.getdata())
pix_val_flat = [x for sets in pix_val for x in sets]
val=mean(pix_val_flat)
pixels= [17.3,45,61.6,86.6,126.6]
l=[0,0,0,0,0]
aom= [5,3.5,2.5,2,1.5]
for x in range(5):
    l[x]=abs(pixels[x]-val)
print(min(l))
print("Average Oraganic Matter Content is : ", aom[l.index(min(l))])














#print("----------------------")
#imm = Image.open('five.JPG','r')
#pix_vals = list(imm.getdata())
#pix_val_flats = [x for sets in pix_vals for x in sets]
#print(mean(pix_val_flats))
#dict= {
   # "level" : [1,2,3,4,5],
  #  "pixels" : [17.3,45,61.6,86.6,126.6],
 #   "aom" : [5,3.5,2.5,2,1.5]
#}



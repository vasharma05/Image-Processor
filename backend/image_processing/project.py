import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
from .filter import applyFilter,medianFilter
from backend.settings import BASE_DIR
# http://localhost:8000/media/images/my-node_OMXKIqV.png
# http://localhost:8000/accounts/api/centroid/
#  Add id = 9 in body
# [{"key":"Authorization","value":"Token 50fe836fdd78b2456a902c50d81fb494cc9d7315","description":"","type":"text","enabled":true}]
# https://stackoverflow.com/questions/53688225/typeerror-required-argument-mat-pos-2-not-found
def getCentroidImage(imgId=None,imgUrl=None):
    try:
        img = cv2.imread(imgUrl, 0)
        ret,binary = cv2.threshold(img,10,255,cv2.THRESH_BINARY)
        def findBB(im):
            h, w = im.shape[0], im.shape[1] 
            left, top = w, h
            right, bottom = 0, 0
            
            for x in range(h):
                for y in range(w):
                    if (im[x,y] == 0):
                        right = x if x > right else right
                        left = x if x < left else left
                        bottom = y if y > bottom else bottom
                        top = y if y < top else top
                        
            return (left, right, top, bottom)
        def findCentroid(im):
            h, w = im.shape[0], im.shape[1]
            cx, cy, n = 0, 0, 0
            for x in range(h):
                for y in range(w):
                    if (im[x,y] == 0):
                        cx += x
                        cy += y
                        n += 1
            cx //= n
            cy //= n
            return (cx, cy)
        def divideImgIntoFour(im, cent):
            h, w = im.shape[0], im.shape[1]
            cx, cy = cent
            img1 = im[0:cx, 0:cy]
            img2 = im[0:cx, cy:w]
            img3 = im[cx:h, 0:cy]
            img4 = im[cx:h, cy:w]
            return [img1, img2, img3, img4]
        def calculateTransitions(im):
            h, w = im.shape[0], im.shape[1]
            prev = im[0,0]
            n = 0
            for x in range(1, h):
                for y in range(1, w):
                    curr = im[x,y]
                    # check if the is black to white transition
                    n = n+1 if curr == 255 and prev == 0 else n
                    prev = curr
            return n
        boundingBox = findBB(binary)
        cropImg = binary[boundingBox[0]:boundingBox[1], boundingBox[2]:boundingBox[3]]
        centroid = findCentroid(cropImg)
        segments = divideImgIntoFour(cropImg, centroid)
        transitions = [calculateTransitions(seg) for seg in segments]

        topLeft="centroid_TopLeft_"+imgId+".png"
        topRight="centroid_TopRight_"+imgId+".png"
        bottomLeft="centroid_BottomLeft_"+imgId+".png"
        bottomRight="centroid_BottomRight_"+imgId+".png"
    
        topLeft= saveImage(topLeft,segments[0],"centroid")
        topRight= saveImage(topRight,segments[1],"centroid")
        bottomLeft= saveImage(bottomLeft,segments[2],"centroid")
        bottomRight= saveImage(bottomRight,segments[3],"centroid")

        return [topLeft,topRight,bottomLeft,bottomRight]
    
    except Exception as e:
        print(e)
        print("IMAGE KA LINK DE@!!")

def getGradientImage(imgId=None,imgUrl=None):
    try:
        #Read Image in GrayScale
        img_gray = cv2.imread(imgUrl,0)
        h,w = img_gray.shape[:2]

        grad_img = np.asarray(img_gray)

        for i in range(0,h):
            for j in range(0,w-1):

                #applying gradient
                a = min(img_gray[i][j+1],img_gray[i][j])
                if a == img_gray[i][j+1] :
                    temp_arr = img_gray[i][j] - img_gray[i][j+1]
                else :
                    temp_arr = img_gray[i][j+1] - img_gray[i][j]
                grad_img[i,j] = temp_arr

                          
        imgName="gradient_"+imgId+".png"        
        imgName=saveImage(imgName,grad_img,"gradient")

        return [imgName]
        
    except Exception as e:
        print(e)

def getNegativeImage(imgId=None,imgUrl=None):
    try:
        S = 255

        img = cv2.imread(imgUrl)
        k = len(img.shape)
        # if in rgb
        if(k==3):
            # open in rgb  
            B,G,R = cv2.split(img)
            B[:] = [S-x for x in B]     #inverting blue
            G[:] = [S-x for x in G]     #inverting green    
            R[:] = [S-x for x in R]     #inverting red

            #saving image
            my_img = cv2.merge((B, G, R)) 
            img_name='inverted_'+ imgId+ '.png'
            img_name=saveImage(img_name,my_img,"negative")   
            return[img_name]
        #if in grayscale or binary
        else:    
            # open in grayscale 
            my_img = np.array([S-x for x in img])
            img_name='inverted_'+ imgId+ '.png'
            img_name=saveImage(img_name,my_img,"negative")
             
            return[img_name]

    except Exception as e:
            print("Url not given")

def getGrayscaleImage(imgId=None,imgUrl=None):
    try:
        img_gray = cv2.imread(imgUrl,0)
        img_name='gray_'+ imgId+ '.png'
    
        img_name=saveImage(img_name,img_gray,"grayscale")

        return[img_name]
    except Exception as e:
        print(e)
        print("Url not given") 

def getSegemtationImage(imgId=None,imgUrl=None):
    try:
        img = cv2.imread(imgUrl)

        # Applying Gaussian blur with kernel size 7 to remove unwanted noise
        blurred_image = cv2.GaussianBlur(img,(7,7),0)

        # Applying Otsu's thresholding to binarize the image
        retval ,binarized_image = cv2.threshold(blurred_image,40,255,cv2.THRESH_BINARY)

        # Applying Closing to fill in the holes
        filter = np.ones((3,3),np.uint8)
        closed_image = cv2.morphologyEx(binarized_image, cv2.MORPH_CLOSE, filter)
        closed_image=cv2.cvtColor(closed_image,cv2.COLOR_BGR2GRAY)
        # Using connected components to label the image
        retval, markers = cv2.connectedComponents(closed_image)

        # Mapping the component labels to hue val
        label_hue = np.uint8(120*markers/np.max(markers))
        blank_ch = 255*np.ones_like(label_hue)
        labeled_image = cv2.merge([label_hue, blank_ch, blank_ch])

        # changing from HSV to RGB again to show
        labeled_image = cv2.cvtColor(labeled_image, cv2.COLOR_HSV2BGR)

        # background label set to black
        labeled_image[label_hue==0] = 0

        imgName='segment_'+imgId+'.png'
       
        imgName=saveImage(imgName,labeled_image,"segmentation")

        return [imgName]        
    except Exception as e:
        print(e)
        print("SENd link")
   
def getHistogramEqualization(imgId=None,imgUrl=None):
    try:
        img = cv2.imread(imgUrl,0)

        #Initialize intensity values with 256 zeroes
        intensity_count = [0] * 256         

        height,width = img.shape[:2]        
        N = height * width                  

        #Array for new_image
        high_contrast = np.zeros(img.shape) 

        for i in range(0,height):
            for j in range(0,width):
                intensity_count[img[i][j]] += 1     #Find pixels count for each intensity

        L = 256

        intensity_count,total_values_used = np.histogram(img.flatten(),L,[0,L])      
        pdf_list = np.ceil(intensity_count*(L-1)/img.size)                    #Calculate PDF
        cdf_list = pdf_list.cumsum()                                                #Calculate CDF


        for y in range(0, height):
            for x in range(0, width): 
            #Apply the new intensities in our new image
                high_contrast[y,x] = cdf_list[img[y,x]]                         

        
        

        #PLOT THE HISTOGRAMS
        imgName="histogram_"+imgId+'.png'
        imgName=saveImage(imgName,high_contrast,"histogram")                         

       
        plt.hist(img.ravel(),256,[0,256])
        plt.xlabel('Intensity Values')
        plt.ylabel('Pixel Count')
        name_plt1='histogram_plt1_'+imgId+".png"
        
        name_plt1=os.path.join(os.getcwd(),"media","histogram",name_plt1)
        plt.savefig(name_plt1)  
        print("SAVED "+name_plt1)
        

        plt.hist(high_contrast.ravel(),256,[0,256]) 
        plt.xlabel('Intensity Values')
        plt.ylabel('Pixel Count')
        name_plt2='histogram_plt2_'+imgId+".png"
        
        name_plt2=os.path.join(os.getcwd(),"media","histogram",name_plt2)
        plt.savefig(name_plt2)
        print("SAVED "+name_plt2)

        os.chdir(globalPath)

        return[name_plt1,name_plt2,imgName]
    except Exception as e:
        print("SENd link")

def getAverageFilter(imgId=None,imgUrl=None,size=None):
    # try:
        #reading image from file
    im = cv2.imread(imgUrl,0).astype(np.float)
    #applying filter on image
    img = applyFilter(im, filterSize=size)
    #writing image to image file
    imgName= "average_"+imgId+".png"
    imgName= saveImage(imgName,img,"average")

    return [imgName]
    # except Exception as e:
    #     print(e)
    #     print("Send link")

def getGaussionFilter(imgId=None,imgUrl=None):
    # try:
    #reading image from file
    im = cv2.imread(imgUrl,0).astype(np.float)
    gaussianFilter = np.array([[1,1,2,2,2,1,1],
                       [1,2,2,4,2,2,1],
                       [2,2,4,8,4,2,2],
                       [2,4,8,16,8,4,2],
                       [2,2,4,8,4,2,2],
                       [1,2,2,4,2,2,1],
                       [1,1,2,2,2,1,1]], np.float)
    gaussianFilter /= np.sum(gaussianFilter*1.0)
    
    #applying filter on image
    img = applyFilter(im, imFilter=gaussianFilter)
    #writing image to image file
    imgName= "gaussian_"+imgId+".png"
    imgName= saveImage(imgName,img,"gaussian")
    return [imgName]
    # except Exception as e:
    #     print(e)
    #     print("Send link")

def getMedianFilter(imgId=None,imgUrl=None,size=None):
    try:
        #reading image from file
        im = cv2.imread(imgUrl,0).astype(np.float)
        
        #applying filter on image
        img = medianFilter(im, filterSize=size)

        #writing image to image file
        imgName= "median_"+imgId+".png"
        
        imgName= saveImage(imgName,img,"median")

        return [imgName]
    except Exception as e:
        print(e)
        print("Send link")

def getSobel(imgId=None,imgUrl=None):
    try:
        img=cv2.imread(imgUrl)
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        container = np.copy(img)
        size = container.shape
        for i in range(1, size[0] - 1):
            for j in range(1, size[1] - 1):
                gx = (img[i - 1][j - 1] + 2*img[i][j - 1] + img[i + 1][j - 1]) - (img[i - 1][j + 1] + 2*img[i][j + 1] + img[i + 1][j + 1])
                gy = (img[i - 1][j - 1] + 2*img[i - 1][j] + img[i - 1][j + 1]) - (img[i + 1][j - 1] + 2*img[i + 1][j] + img[i + 1][j + 1])
                container[i][j] = min(255, np.sqrt(gx**2 + gy**2))
        
        img = cv2.cvtColor(container, cv2.COLOR_GRAY2RGB)

        imgName="sobel_"+imgId+".png"
        imgName= saveImage(imgName,img,"sobel")

        return [imgName]
    except Exception as e:
        print(e)
        print("Link dedo")


def saveImage(filename=None,img=None,typeFilter=None):
    try:

        # directory=os.path.join(BASE_DIR,"media",typeFilter,filename)
        d = 'media/{}/{}'.format(typeFilter, filename)
        print(d)
        if(cv2.imwrite(d, img)):
            print("SAVED "+ d)
        else:
            print("SAVE NI HUI "+d)
        return 'http://localhost:8000/{}'.format(d)
    except Exception as e:
        print(e)

# getCentroidImage("ll","/home/shivamsoods/Pictures/iig.png") 4
# getGradientImage("ii","/home/shivamsoods/Pictures/iig.png") 1
# getNegativeImage("ll","/home/shivamsoods/Pictures/iig.png") 1
# getGrayscaleImage("ll","/home/shivamsoods/Pictures/iig.png") 1
# getSegemtationImage("ll","/home/shivamsoods/Pictures/iig.png") 1
# getHistogramEqualization("ll","/home/shivamsoods/Pictures/iig.png") 3
# getAverageFilter("ll","/home/shivamsoods/Pictures/iig.png",3) 1
# getGaussionFilter("ll","/home/shivamsoods/Pictures/iig.png") 1
# getMedianFilter("ll","/home/shivamsoods/Pictures/iig.png",3) 1
# getSobel("ll","/home/shivamsoods/Pictures/iig.png") 1
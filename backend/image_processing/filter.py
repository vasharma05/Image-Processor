import numpy as np
import copy

#function to apply filter on image
#call it with just filter size (averaging filter)
#call it with given filter in imFilter
def applyFilter(img, filterSize=None, imFilter=None):
    if(filterSize is not None):
        filterSize=int(filterSize)
    filteredImg = copy.deepcopy(img)
    #if filter is provided
    if (imFilter is not None):
        imgFilter = imFilter
        filterSize = len(imFilter)
    #if filter is not provided, create an averging filter
    else:
        imgFilter = (1.0/(filterSize*filterSize))*np.ones((filterSize,filterSize)) #creating filter
    
    paddingSize = filterSize//2
    #padding the image with zeros
    filteredImg = np.pad(filteredImg, (paddingSize, paddingSize), 'constant', constant_values=(0))
    
    for row in range(paddingSize, filteredImg.shape[0]-paddingSize):
        for col in range(paddingSize, filteredImg.shape[1]-paddingSize):
            pixel = 0.0
            #convolving the filter
            for x_filter in range(filterSize):
                for y_filter in range(filterSize):
                    pixel += filteredImg[row+x_filter-paddingSize][col+y_filter-paddingSize]*imgFilter[x_filter][y_filter]
            filteredImg[row,col] = pixel
    #removing padded pixels
    filteredImg = filteredImg[paddingSize:filteredImg.shape[0]-paddingSize, paddingSize:filteredImg.shape[1]-paddingSize]
    return filteredImg

def medianFilter(img, filterSize):
    #making deep copy of image
    filteredImg = copy.deepcopy(img)
    #calculating padding size
    filterSize=int(filterSize)
    paddingSize = filterSize//2
    #padding the image
    filteredImg = np.pad(filteredImg, (paddingSize, paddingSize), 'constant', constant_values=(0))
    #loop through image pixels
    for row in range(paddingSize, filteredImg.shape[0]-paddingSize):
        for col in range(paddingSize, filteredImg.shape[1]-paddingSize):
            kernal = []
            for x_filter in range(filterSize):
                for y_filter in range(filterSize):
                    kernal.append(filteredImg[row+x_filter-paddingSize][col+y_filter-paddingSize])
            #calculating median of list
            filteredImg[row,col] = np.median(kernal)
    #removing zero padding 

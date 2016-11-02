#Custom Functions to help handle remote sensing data

#Requirements
import rasterio
from GeoPandas import GeoDataFrame
import numpy as np
import matplotllib.pyplot as plt

#Functions
def ExploreRasterImage(input_file, band_number=1):
    with rasterio.open(input_file) as src:
        meta_data = src.meta
        band = src.read(band_number)

        for i in [x for x in meta_data]:
            print i.upper() + ': ', meta_data[i]

        image_height_to_width_ratio = float(meta_data['height']) / float(meta_data['width'])
        image_height_to_width_ratio

    plt.figure(figsize=(25.0*image_height_to_width_ratio,25.0))
    plt.imshow(band) #, cmap='gray')
    plt.show()
    
    plt.hist(np.ravel(band), bins=260)
    plt.show()


def CreateMaskArray(input_file, threshold_float):
    try:
        print '-------------------------------------'
        print 'Generating mask array from input file...'
        print
        with rasterio.open(input_file) as src:
            meta_data = src.meta
            band = src.read(1)
            
            print 'META DATA'
            for i in [x for x in meta_data]:
                print i.upper() + ': ', meta_data[i]
            print 

            #Transform into mask_array
            mask_array = np.where(band > threshold_float, 1.0, 0.0)
    except Exception:
        print Exception
    
    print 'Returning mask array... '
    return mask_array


def ExploreMultiBandImage(input_file):
    with rasterio.open(input_file) as src:
        number_of_bands = src.count

    for num in range(1,number_of_bands+1):
        print 'BAND NUMBER ' + str(num)
        ExploreRasterImage(input_file, band_number=num)


def StoreBandinGPD(input_file, band_number):
    try:
        print '-------------------------------------'
        print 'Storing band array in GeoPandas DataFrame...'
        print
        
        with rasterio.open(input_file) as src:
            meta_data = src.meta

            band = src.read(band_number)
            band_as_gpd = GeoDataFrame(band)

    except:
        print Exception
    
    print 'Returning dataframe... '
    return band_as_gpd
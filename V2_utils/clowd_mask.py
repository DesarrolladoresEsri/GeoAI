# coding: utf-8
import os
import arcpy
try:
    import rasterio
    from rasterio.plot import show
except:
    arcpy.AddMessage("System don't has rasterio installed")

original_image = arcpy.Describe(arcpy.GetParameterAsText(0))
udm2_image =  arcpy.Describe(arcpy.GetParameterAsText(1))
out_location = arcpy.GetParameterAsText(2)
out_file = os.path.join(out_location, 
                        r'{}_Cloud_masked.tiff'.format(original_image.name[:-4]))

with rasterio.open(udm2_image.CatalogPath) as src:
    shadow_mask = src.read(3).astype(bool)
    cloud_mask = src.read(6).astype(bool)
mask = cloud_mask + shadow_mask
with rasterio.open(original_image.CatalogPath) as src:
    profile = src.profile
    img_data = src.read([1, 2, 3, 4], masked=True)/1000.0
    kwds = profile
    print(kwds)
    kwds['driver'] = 'GTiff'
    kwds['dtype'] = profile['dtype']
    img_data.mask = mask
    img_data = img_data.filled(fill_value=0)
    
    show(img_data, title="masked image")


with rasterio.open(out_file, 'w', **kwds) as f:
    print(out_location)
    f.write(img_data*10000)
    f.close()
        
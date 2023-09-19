import arcpy

raster_path = r"D:\Sem-3\Programming for GIS-3\Assignment2\ProProject_Practical_Two\RASTER_DATA\ASTGTMV003_N18E073_dem.tif"
desc_obj = arcpy.Describe(raster_path)

# Band count
print(desc_obj.bandCount)
# Format
print(desc_obj.format)
# Image Height and Width
print(desc_obj.height)
print(desc_obj.width)
# Base Name
print(desc_obj.basename)

print("Process Completed")



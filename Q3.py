import arcpy
import os

# Path to file gdb
file_GDB_path = r"D:\Sem-3\Programming for GIS-3\Assignment2\ProProject_Practical_Two\World_data.gdb"
fc_name = ["lakes"]

for fc in fc_name:
    fc_path = os.path.join(file_GDB_path, fc)
    desc_obj = arcpy.Describe(fc_path)

    sr_obj = desc_obj.spatialReference
    print(sr_obj.name)
    print(sr_obj.type)

    shape_type = desc_obj.shapeType
    print("The geometry type of feature class: {} is {}".format(fc, shape_type))

    field_list = desc_obj.fields
    for field in field_list:
        print("The field name is {} and the type is {}".format(field.name, field.type))

print("Process Completed")


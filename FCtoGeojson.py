import arcpy

gdb = arcpy.GetParameterAsText(0)
outFolder = arcpy.GetParameterAsText(1)
arcpy.env.workspace = gdb
featureclasses = arcpy.ListFeatureClasses()
for fc in featureclasses:
    #print(fc)
    #arcpy.AddMessage(fc)
    outjson = (outFolder + "\\" + fc[16:24] + "-dbct-stockpiles.geojson")
    #print(outjson)
    arcpy.AddMessage(outjson)
    arcpy.conversion.FeaturesToJSON(fc, outjson, geoJSON='GEOJSON')

print("Script Complete")
arcpy.AddMessage("Script Complete")
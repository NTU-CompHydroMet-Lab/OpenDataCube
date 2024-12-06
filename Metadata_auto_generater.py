from datetime import datetime
from pathlib import Path
from eodatasets3 import DatasetAssembler

import xarray as xr 
import rioxarray as rio

import os
import pandas as pd

PATH = './Split_improve'
timestamps = []
outputfiles = []
inputfiles = os.listdir(PATH)
for file in inputfiles:
    date = []
    timelt = []
    file_date = file[-22:-12]
    file_time = file[-11: -3]
    for i, t in zip(file_date.split('-'), file_time.split(':')):
        if i[0] == '0':
            i = i[-1]
            date.append(int(i))
        else :
            date.append(int(i))
        if t[0] == '0':
            t = t[-1]
            timelt.append(int(t))
        else :
            timelt.append(int(t))
    timestamps.append(datetime(date[0], date[1], date[2], timelt[0], timelt[1], timelt[2]))
    outputfiles.append(str(date[0]) + str(date[1]) + str(date[2]) + '_' + file[-11:-3]+ '.tiff')
print('list ok')

tiffoutfile_path = './TiffsImprove'

def conversion(input_filename, epsg, tiffoutfile_path, out_filename, para):
    nc_file = xr.open_dataset(input_filename,decode_times=False)
    vls = [i for i in nc_file.variables]
    #print(f'Here is the variable list in the nc file :{vls}')
    #print('Please choose the variable you would like to output :')
    #para = str(input())
    if para in [i for i in nc_file.variables]:
        data = nc_file[para]
    else: print(f'{para} is not in the variable list! Pleas change the variable!')
    #print('Pleas input the longtitude and latitude name based on the variable list :')
    #crs = str(input())
    #lonlat = tuple(crs.split(","))
    data = data.rio.set_spatial_dims(x_dim = vls[0], y_dim = vls[1])
    epsgFinal = 'epsg:' + epsg
    data.rio.write_crs(epsgFinal, inplace=True)
    data.rio.to_raster(tiffoutfile_path + '/' + out_filename)

for timestamp, inputfile, outputfile in zip(timestamps, inputfiles, outputfiles):
    with DatasetAssembler(
    Path("/odctest" + "/Clean/"), naming_conventions="default"
    ) as p:
        p.product_family = 'improve'
        p.datetime = timestamp
        p.processed_now()
        print(f'{PATH}/{inputfile}')
        conversion(PATH + '/' + inputfile, '4326', tiffoutfile_path, outputfile, 'value')
        p.write_measurement('variable', tiffoutfile_path + '/' + outputfile)
        p.done()

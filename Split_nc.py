import netCDF4 as nc
import numpy as np
import datetime as dt
from netCDF4 import date2num,num2date
import xarray as xr 
import rioxarray as rio
import matplotlib.pyplot as plt

def Split_nc(input_file, path, para):
    file = nc.Dataset(str(input_file))
    xrnc = xr.open_dataset(str(input_file), decode_times=True)
    
    for timestamp in range(file.variables['time'].shape[0]):
        var = file[para][timestamp, :]
        var.data[var.data == var.data.min()] = np.nan
        
        timeList = str(xrnc['time'][timestamp])

        dates = [dt.datetime.fromisoformat(timeList[36:55])]
        #46
        output_file = str(path) + '/' + str(timestamp) + '_' + timeList[36:55] + '.nc'
        ds = nc.Dataset(output_file, 'w', format='NETCDF4')
        
        
        lon_dim = ds.createDimension('lon', var.data.shape[1])
        lat_dim = ds.createDimension('lat', var.data.shape[0])
        time_dim = ds.createDimension('time', None)
        
        
        lons = ds.createVariable('lon', 'f4', ('lon',))
        lats = ds.createVariable('lat', 'f4', ('lat',))
        times = ds.createVariable('time', 'f4', ('time',))
        value = ds.createVariable('value', 'f4', ('time', 'lat', 'lon',))
        
        value.units = 'Unknown'
        times.units = 'hours since 1800-01-01'
        time = date2num(dates, times.units)
        lats.units = 'degrees north'
        lons.units = 'degrees east'
        
        
        lons[:] = np.arange([i for i in file['longitude']][0].tolist(), [i for i in file['longitude']][-1].tolist()+0.1, 0.1)
        lats[:] = np.arange([i for i in file['latitude']][0].tolist(),[i for i in file['latitude']][-1].tolist(), -0.1)
        times[:] = time
        value[0, :, :] = var.data

        print(f'Time : {timeList[36:55]}')

        ds.close()
from herbie import Herbie
# Use a confirmed historical date so the server has the file
H = Herbie(
    "2026-06-15 06:00", 
    model="gfs", 
    fxx=0, 
    product="pgrb2.0p25",
    download_kwargs={"verify": False}
)

# Print the inventory to screen
ds = H.xarray(r":VVEL:100 mb:", remove_grib=False)
point = ds.sel(latitude=33.0, longitude=330, method="nearest")
print(float(point["w"]))

print(ds)
print(ds["w"].values) 

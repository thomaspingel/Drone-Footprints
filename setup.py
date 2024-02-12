from setuptools import setup
import re

with open('src/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)

setup(
    name='src',
    version=version,
    description='Drone_image footprint calculator',
    long_description="""
    The purpose of this module is to calculate imagery footprints of individual drone images. There is no stitching of
    images, so the process is actually quite fast. The output is geo-rectified GeoTiff image file and a GeoJSON file 
    with:

    * Drone Flightpath (LineString)
    * Drone Location at location of photo (Point)
    * Individual Image Footprints (Polygons)
    """,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Drone Image Processors',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Programming Language :: Python :: 3.9'
    ],
    packages=['src'],
    keywords=['src', 'DJI', 'exif', 'footprints'],
    url='https://github.com/spifftek70/Drone-Footprints',
    author='Dean Hand',
    author_email='dean.e.hand@me.com',
    install_requires=[
        'geojson',
        'argparse',
        'geopandas',
        'fiona',
        'pyproj',
        'numpy',
        'utm',
        'geojson_rewind',
        'GDAL',
        'progress',
        'shapely',
        'numpy',
        'progressbar',
        'pyexiftool',
        'GDAL',
        'gps-time',
        'datetime',
        'vector3d'],
    zip_safe=False
)

# Leaflet Tools
These scripts can be used to make [Leaflet](https://leafletjs.com) tiles from a large large image.

## Usage
```sh
$ python tilize.py -o tiles large-image.png
```

```JavaScript
const map = new L.Map(this.$refs.map, { crs: L.CRS.Simple })
const layer = L.tileLayer(`./tiles/{z}/{y}/{x}.png`)

map.addLayer(layer)
```
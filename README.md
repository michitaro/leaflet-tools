# Leaflet Tools
These scripts can be used to make [Leaflet](https://leafletjs.com) tiles from a large large image.

## Usage
```sh
$ python tilize.py -o tiles large-image.png
```

```JavaScript
const map = new L.Map('#map', { crs: L.CRS.Simple })
const layer = L.tileLayer(`./tiles/{z}/{y}/{x}.png`)

map.addLayer(layer)
map.setView([0, 0], 0)
```

```html
<html>

<body>
  <div id="map"></div>
</body>

</html>
```

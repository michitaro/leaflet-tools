<html>

<head>
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css"
    integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A=="
    crossorigin="" />
  <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"
    integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA=="
    crossorigin=""></script>
  <script>
    window.addEventListener('load', () => {
      const map = new L.Map('#map', { crs: L.CRS.Simple })
      const layer = L.tileLayer(`./tiles/{z}/{y}/{x}.png`)
      map.addLayer(layer)
      map.setView([0, 0], 0)
    })
  </script>
</head>

<body>
  <div id="map"></div>
</body>

</html>

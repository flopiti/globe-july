# 🌍 Spinning Globe with Land Data

Create beautiful, interactive spinning globes using your Natural Earth land data (`ne_110m_land.json`).

## 🚀 Quick Start

### Option 1: Python Server (Recommended)
```bash
# Make the server executable
chmod +x serve.py

# Start the server
python3 serve.py
```

This will:
- Start a local server on port 8000
- Automatically open your browser
- Show both D3.js and Three.js versions

### Option 2: Node.js Server
```bash
# Install a simple server
npm install -g http-server

# Start server in this directory
http-server -p 8000 --cors

# Open in browser
open http://localhost:8000/three-globe.html
```

### Option 3: Other Servers
```bash
# PHP
php -S localhost:8000

# Ruby
ruby -run -e httpd . -p 8000
```

## 📁 Files Created

| File | Description | Features |
|------|-------------|----------|
| `three-globe.html` | **Advanced 3D Globe** | ✨ WebGL, atmosphere effects, stars |
| `spinning-globe.html` | **Simple 2D Globe** | 📊 D3.js, lightweight, classic |
| `serve.py` | **Python Server** | 🐍 CORS-enabled local server |

## 🎨 Globe Features

### Three.js Version (Recommended)
- ✨ **3D WebGL rendering** with realistic lighting
- 🌊 **Ocean sphere** with water-like material
- 🌍 **Filled land masses** from your GeoJSON data
- 🌌 **Atmosphere glow** and starfield background
- 🖱️ **Interactive controls**: drag, zoom, touch support
- ⚡ **Performance optimized** for smooth rotation
- 📱 **Mobile friendly** with touch controls

### D3.js Version
- 📊 **SVG-based** 2D projection
- 🗺️ **Orthographic projection** for globe effect
- 🌐 **Graticule lines** (lat/lon grid)
- 🖱️ **Drag and zoom** interactions
- 💨 **Lightweight** and fast loading

## 🎛️ Controls

### Both Versions
- **🖱️ Drag**: Rotate the globe manually
- **🖲️ Scroll**: Zoom in/out
- **⏯️ Toggle**: Start/stop auto-rotation
- **🔄 Reset**: Return to initial view

### Three.js Additional
- **🌐 Wireframe**: Toggle land wireframe mode
- **⚡ Speed**: Change rotation speed
- **📱 Touch**: Mobile-optimized controls

## 🔧 Customization Options

### Land Appearance
```javascript
// In three-globe.html, modify land material:
const landMaterial = new THREE.MeshLambertMaterial({
    color: 0x2d5016,        // Forest green
    // Try: 0x8B4513 (brown), 0x228B22 (green), 0x654321 (dark brown)
});
```

### Ocean Color
```javascript
// Modify ocean material:
const oceanMaterial = new THREE.MeshPhongMaterial({
    color: 0x006994,        // Ocean blue
    // Try: 0x000080 (navy), 0x4682B4 (steel blue), 0x008B8B (dark cyan)
});
```

### Rotation Speed
```javascript
// Adjust rotation speed:
let rotationSpeed = 0.005;  // Slow and smooth
// Try: 0.01 (faster), 0.002 (slower), 0.02 (much faster)
```

### Globe Size
```javascript
// Change globe radius:
const sphereGeometry = new THREE.SphereGeometry(2, 64, 32);
//                                              ^ radius
// Try: 1.5 (smaller), 3 (larger), 2.5 (bigger)
```

## 🌟 Alternative Approaches

### 1. **Mapbox GL JS** (Professional)
- Best for production applications
- Built-in globe view (requires API key)
- Advanced styling options

### 2. **Cesium.js** (Scientific/GIS)
- Full-featured 3D globe
- Terrain, imagery, and time-based data
- Great for scientific applications

### 3. **Google Earth Engine** (Data-Heavy)
- Satellite imagery integration
- Real-time data processing
- Requires Google account

### 4. **Observable Notebooks** (Rapid Prototyping)
- Online development environment
- Built-in D3.js examples
- Easy sharing and collaboration

## 📊 Data Information

Your `ne_110m_land.json` contains:
- **Format**: GeoJSON FeatureCollection
- **Source**: Natural Earth 1:110m scale
- **Features**: Land polygons with country boundaries
- **Coordinates**: Longitude, Latitude pairs in decimal degrees
- **Size**: ~133 lines (~4KB) - perfect for web use

## 🎯 Performance Tips

1. **File Size**: Your 1:110m data is optimized for web use
2. **Browsers**: Modern browsers (Chrome, Firefox, Safari, Edge)
3. **Mobile**: Both versions work on mobile devices
4. **Loading**: Three.js version may take 2-3 seconds to load initially

## 🐛 Troubleshooting

### "Failed to fetch" Error
- **Cause**: CORS restrictions when opening HTML directly
- **Solution**: Use the Python server or any local server

### Land Not Appearing
- **Check**: Ensure `ne_110m_land.json` is in the same directory
- **Check**: Browser console for error messages
- **Check**: File permissions are readable

### Slow Performance
- **Try**: Reduce sphere geometry segments (64→32)
- **Try**: Disable atmosphere effects
- **Try**: Use D3.js version instead

## 🚀 Next Steps

1. **Customize Colors**: Match your brand or preferences
2. **Add Features**: Country names, population data, etc.
3. **Export Views**: Screenshot functionality
4. **Data Updates**: Use different Natural Earth scales
5. **Integration**: Embed in your website or application

## 📚 Resources

- [Natural Earth Data](https://www.naturalearthdata.com/) - More geographic data
- [D3.js Documentation](https://d3js.org/) - Data visualization library
- [Three.js Documentation](https://threejs.org/) - 3D graphics library
- [GeoJSON Specification](https://geojson.org/) - Understanding your data format

---

**🎉 Enjoy your spinning globe!** 

Feel free to experiment with the code and create your own unique Earth visualization.
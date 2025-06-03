# Live Satellite Tracker

A real-time 3D satellite visualization system that combines web-based rendering with orbital mechanics simulation. Built with **CesiumJS** and **Satellite.js**, this project visualizes live satellite trajectories using Two-Line Element (TLE) data, supports user interaction for metadata inspection, and incorporates backend modeling in Python to simulate orbital motion and verify accuracy.

## 🔧 Key Features

- **Real-Time Visualization**: Renders satellite positions over an interactive 3D Earth using CesiumJS.
- **TLE-Based Propagation**: Integrates Satellite.js to parse and propagate orbital paths from live TLE feeds.
- **Metadata & UI Controls**: Custom UI to toggle satellite labels, view real-time properties, and filter objects.
- **Orbit Simulation**: Python backend script and Jupyter notebook provide analytical simulations using classical orbital elements.
- **Modular Design**: Separates visualization (HTML/JS) from modeling (Python) for clear extensibility and testing.

## 🚀 Live Demo

👉 [Launch the Web App](https://wagiham.github.io/satellite-tracker/)

## Technical Overview

1. **Frontend Development**:  
   - Used `CesiumJS` for rendering Earth and satellite objects.  
   - Integrated `Satellite.js` to convert TLE data into geocentric coordinates in real-time.

2. **Backend Orbit Analysis**:  
   - Developed `orbit_simulator.py` to implement basic orbital mechanics calculations (e.g., Keplerian orbits).
   - Built `orbit-analysis.ipynb` to visualize orbits and validate simulation against real TLE paths.

3. **Deployment**:  
   - Hosted on GitHub Pages with static assets.  
   - Project structured to exclude environment files (e.g., virtualenv) for clean repo cloning and testing.

## 📈 Future Work

- Implement **collision detection** algorithms based on positional covariance or proximity thresholds.
- Add time controls and user-selected simulation intervals.
- Enhance responsiveness and support touch-based globe manipulation.

## 📁 File Structure

satellite-tracker/
├── index.html # Frontend visualization logic
├── orbit_simulator.py # Orbital mechanics modeling
├── orbit-analysis.ipynb # Orbit plotting and validation

satellite-tracker/
├── index.html # Frontend visualization logic
├── orbit_simulator.py # Orbital mechanics modeling
├── orbit-analysis.ipynb # Orbit plotting and validation





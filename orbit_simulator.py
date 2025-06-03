from poliastro.bodies import Earth
from poliastro.twobody import Orbit
from poliastro.plotting.static import StaticOrbitPlotter
from astropy import units as u
from astropy.time import Time
import numpy as np
import plotly.graph_objs as go

# Generate N satellites in circular orbits with variable inclinations and RAANs
def generate_constellation(n_sats, altitude_km):
    sats = []
    for i in range(n_sats):
        inc = np.deg2rad(np.random.uniform(45, 98))  # Inclination
        raan = np.deg2rad(np.random.uniform(0, 360))  # Right Ascension of Ascending Node
        a = Earth.R + altitude_km * u.km  # Semi-major axis
        ecc = 0.001 * u.one  # Near circular
        orbit = Orbit.from_classical(
            attractor=Earth,
            a=a,
            ecc=ecc,
            inc=inc * u.rad,
            raan=raan * u.rad,
            argp=0 * u.deg,
            nu=0 * u.deg,
            epoch=Time.now()
        )
        sats.append(orbit)
    return sats

# Visualization using Plotly (simplified)
def visualize_orbits(satellites):
    traces = []
    for sat in satellites:
        r = sat.sample(values=np.linspace(0, sat.period.to(u.s).value, 100) * u.s)[0]
        trace = go.Scatter3d(
            x=r[0].to_value(u.km),
            y=r[1].to_value(u.km),
            z=r[2].to_value(u.km),
            mode='lines',
            name='Satellite'
        )
        traces.append(trace)

    fig = go.Figure(data=traces)
    fig.update_layout(
        title="Satellite Orbits",
        scene=dict(
            xaxis_title='X (km)',
            yaxis_title='Y (km)',
            zaxis_title='Z (km)',
            aspectmode='data'
        )
    )
    fig.show()

# Example usage
if __name__ == '__main__':
    constellation = generate_constellation(n_sats=6, altitude_km=600)
    visualize_orbits(constellation)

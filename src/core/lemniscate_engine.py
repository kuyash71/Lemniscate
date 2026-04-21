import math
from src.core.models import MissionConfig

def generate_local_points(config: MissionConfig) -> list[tuple[float, float]]:
    points = []
    n= config.n_waypoints
    a= config.semi_locus
    teta = math.radians(config.orientation)
    for i in range(n):
        t = 2*math.pi*i / n

        x = (a*math.sqrt(2)*math.cos(t) / ((math.sin(t)*math.sin(t)) + 1))
        y = (a*math.sqrt(2)*math.sin(t)*math.cos(t) / ((math.sin(t)*math.sin(t)) + 1))

        x_dt = x*math.cos(teta) + y*math.sin(teta)
        y_dy = -x*math.sin(teta) + y*math.cos(teta)

        points.append((x_dt,y_dy))

    return points

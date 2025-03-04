from utils.functions import process
import json

with open('parallelepipeds.json', 'r') as f:
    parallelepipeds = json.load(f)

characteristics = dict()
for fig, atr_dict in parallelepipeds.items():
    a = float(atr_dict['a'])
    b = float(atr_dict['b'])
    c = float(atr_dict['c'])
    characteristics[fig] = process(a, b, c)

# ---- get  statistic

stat_dict = {
                "avg_diag": [],
                "avg_volume": [],
                "avg_surface_area": [],
                "avg_alpha":[],
                "avg_beta":[],
                "avg_gamma": [],
                "avg_radius_described_sphere": [],
                "avg_volume_described_sphere": []
            }

for fig in characteristics.values():
    stat_dict["avg_diag"].append(float(fig['diag']))
    stat_dict["avg_volume"].append(float(fig['volume']))
    stat_dict["avg_surface_area"].append(float(fig['surface_area']))
    stat_dict["avg_alpha"].append(float(fig['alpha']))
    stat_dict["avg_beta"].append(float(fig['beta']))
    stat_dict["avg_gamma"].append(float(fig['gamma']))
    stat_dict["avg_radius_described_sphere"].append(float(fig['radius_described_sphere']))
    stat_dict["avg_volume_described_sphere"].append(float(fig['volume_described_sphere']))

statistics = {k: str(round(sum(v)/len(v), 2)) for k, v in stat_dict.items()}


with open('characteristics.json', 'w') as f:
    json.dump(characteristics, f, indent=4)

with open('statistics.json', 'w') as f:
    json.dump(statistics, f, indent=4)
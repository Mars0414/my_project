import math as mt 
def get_diag(a:float,b:float,c:float)->float:
  return mt.sqrt(a**2 + b**2 + c**2)

def get_volume(a:float,b:float,c:float)->float:
  return a*b*c

def get_surface(a:float,b:float,c:float)->float:
  return 2* (a*b + a*c + b*c)

def get_alpha(a:float,b:float,c:float)->float:
  return mt.acos(a/mt.sqrt(a**2 + b**2 + c**2))

def get_beta(a:float,b:float,c:float)->float:
  return mt.acos(b/mt.sqrt(a**2 + b**2 + c**2))

def get_gamma(a:float,b:float,c:float)->float:
  return mt.acos(c/mt.sqrt(a**2 + b**2 + c**2))

def get_sphr_radius(a:float,b:float,c:float)->float:
  return mt.sqrt(a**2 + b**2 + c**2) / 2

def get_sphr_volume(a:float,b:float,c:float)->float:
  return 4/3*mt.pi * (mt.sqrt(a**2 + b**2 + c**2) / 2)**3

def process(a:float,b:float,c:float)->dict:
  fig_dict = {
    "diag": str(round(get_diag(a, b, c), 2)),
    "volume": str(round(get_volume(a, b, c), 2)),
    "surface_area": str(round(get_surface(a, b, c), 2)), 
    "alpha": str(round(get_alpha(a, b, c), 2)),
    "beta": str(round(get_beta(a, b, c), 2)),
    "gamma": str(round(get_gamma(a, b, c), 2)),
    "radius_described_sphere": str(round(get_sphr_radius(a, b, c), 2)),
    "volume_described_sphere": str(round(get_sphr_volume(a, b, c), 2))
  }
  return fig_dict

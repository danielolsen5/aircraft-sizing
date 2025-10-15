import numpy as np
Print = True

""" physical properties """ 
w = 90 # gross weight in Newtons 
b = 2.75 # total wingspan in meters 
lamb = 1 # taper ratio
c_r = .3 # root chord length in m 
c_t = lamb * c_r # tip chord length (m)
s = b * .5* (c_r + c_t) # wing area 
A = b**2 / s # aspect ratio keep above 8 to prevent significant vorticies at the wingtip pair with winglets 
rho = 1.225
rho_w = 1.705 # wing "density" kg/m^2
w_w = rho_w * s
w_s = w / s # wing loading
g = 9.8 # gravity

""" flight properties """ 

v_c = 20 # cruse velocity m/s rho = 1.225 # air density kg/m^3 
q = .5 * rho * v_c**2 #dynamic pressure
c_lm = 1.2 #max lift coefficient
c_lmin = -.5

""" Wing, Tail""" 

# design lift coefficient 
c_lr = w / (q * s) 

# stall speed
v_s = np.sqrt((2 * w_s) / (rho * c_lm))

# tail sizing

S_w = s # wing area
b_w = b # wing span
C_w = (c_r * c_t) / 2 # mean chord
L_vt = 1.5 # distance from tail quarter chord to wings mean chord leading edge
L_ht = L_vt 
c_vt = .04 # vertical tail volume coefficient 6.26 for sailplane
c_ht = .7 # horizontal tail volume coefficient 6.27 for sailplane
S_vt = (c_vt * b_w * S_w) / L_vt # vertical tail area
S_ht = (c_ht * C_w * S_w) / L_ht # horizontal tail area
# define dimensions and project
theta = np.radians(45) #tail dihedral angle

lamb_t = .6 # tail taper ratio
c_tr = .18 #tail root chord
c_tt = c_tr * lamb_t # tail tip chord
b_t = (2 * S_ht) / ((c_tr + c_tt) * np.cos(theta)) # tail span on dihedral



"""
Control Surfaces
"""

#rudder sizes
c_rr = .35 * c_tr # rudder chord 25% < x < 50%
b_r = .9 * b_t # rudder span

# aileron sizes
c_a = .3 * c_r # aileron root from figure
b_a = .25 * b # aileron span from figure


"""
flight performance
"""

#steady turn
n_max = (c_lm * .5 * rho * v_c**2) / w_s # load factor 3.9.21
n_min = (c_lmin * .5 * rho * v_c**2) / w_s # 3.9.22

R_pos = v_c**2 / (g * np.sqrt(n_max**2 -1)) # 3.9.20
R_neg = v_c**2 / (g * np.sqrt(n_min**2 -1))
    
    
"""
Dynamic forces  
"""
a_f = np.radians(15) # flap extension angle
s_a = c_a * b_a # individual aileron area
F_a = 2 * q * s_a * (np.sin(a_f))**2

s_r = b_r * .35 * .5 * (c_rr + c_rr) # rudder area
F_r = 2 * q * s_r * (np.sin(a_f))**2 #force on rudder

if Print:
    print("Flight Properties")
    print(f"Required lift coefficient: {c_lr:.4f}")
    print(f"Stall Speed: {v_s:.2f} m/s")
    print(f"Minimum Turn Radius: {R_pos:.2f} m ")
    
    print("Wing Sizes")
    print(f"Wing Span: {b} m ")
    print(f"Chord: {c_r*100} cm")
    print(f"Predicted wing weight {w_w:.2f} kg")
    
    print("Tail Size")
    print(f"Tail Root Chord: {c_tr*100:.2f} cm")
    print(f"Tail Tip Chord: {c_tt*100:.2f} cm")
    print(f"Tail Span: {b_t*100:.2f} cm")
    print(f"Dihedral Angle: {np.degrees(theta)} Deg")
    
    print("Forces")
    print(f"Force on aileron: {F_a:.2f} N")
    print(f"Force on rudder: {F_r:.2f} N")
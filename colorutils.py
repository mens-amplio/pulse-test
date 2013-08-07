import colorsys

# Gamma corrected color values from 0-255
gamma = bytearray(256)
for i in range(256):
    gamma[i] = int(pow(float(i) / 255.0, 2.5) * 255 + 0.5)

# Returns a gamma corrected list of color tuples
def gamma_correct(colors):
    return [ tuple([ gamma[int(i)] for i in c ]) for c in colors ]

# Returns val constrained to the range [min_val, max_val]
def constrain( val, min_val, max_val ):
    if val < min_val: val = min_val
    elif val > max_val: val = max_val
    return val

# HSV->RGB conversion, rounding to integer
def hsv_to_rgb_int(hsv):
    (r,g,b) = colorsys.hsv_to_rgb(*hsv)
    return ( int(r+0.5), int(g+0.5), int(b+0.5) )

# Returns a list of interpolated RGB tuples between rgb1 and rgb2 (inclusive)
# broken down into a given number of steps
def interpolated_list(rgb1, rgb2, steps):
    
    # HSV interpolation is supposed to make for better transitions, but RGB 
    # interpolation looks better to me in this demo. Revisit this later.
    #hsv1 = colorsys.rgb_to_hsv(*rgb1)
    #hsv2 = colorsys.rgb_to_hsv(*rgb2)
    #return [ hsv_to_rgb_int( interpolate(hsv1, hsv2, i, steps) ) for i in range(steps) ]

    # simple RGB interpolation
    return [ interpolate(rgb1, rgb2, i, steps) for i in range(steps) ]
    
# Returns a single step in the interpolation between two tuples
def interpolate(c1, c2, step, step_cnt):
    n = min( len(c1), len(c2) )
    if step_cnt < 2: step_cnt = 2
    step = constrain(step, 0, step_cnt-1)
    fraction = float(step)/(step_cnt-1)
    return tuple( [ linear_interpolate(c1[i], c2[i], fraction) for i in range(n) ] )
    
# Returns a linear mixture of two values. The fraction argument is the 
# weighting of the end value in a [0-1] range
def linear_interpolate(start, end, fraction):
    fraction = constrain(fraction, 0, 1)
    return start + (end - start)*fraction

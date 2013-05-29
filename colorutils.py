import colorsys

# Returns val constrained to the range [min_val, max_val]
def constrain( val, min_val, max_val ):
    if val < min_val: val = min_val
    elif val > max_val: val = max_val
    return val

# HSV->RGB conversion, rounding to integer
def hsv_to_rgb_int(h, s, v):
    (r,g,b) = colorsys.hsv_to_rgb(h, s, v)
    return ( int(r+0.5), int(g+0.5), int(b+0.5) )

# Returns a list of interpolated RGB tuples between rgb1 and rgb2 (inclusive)
# broken down into a given number of steps
def interpolated_list(rgb1, rgb2, steps):
    return [ interpolate(rgb1, rgb2, i, steps) for i in range(steps) ]
    
# Returns a single step in the interpolation between two RGB tuples
def interpolate(rgb1, rgb2, step, step_cnt):
    if step_cnt < 2: step_cnt = 2
    step = constrain(step, 0, step_cnt-1)
    fraction = float(step)/(step_cnt-1)
    hsv1 = colorsys.rgb_to_hsv(*rgb1)
    hsv2 = colorsys.rgb_to_hsv(*rgb2)
    h = linear_interpolate(hsv1, hsv2, 0, fraction)
    s = linear_interpolate(hsv1, hsv2, 1, fraction)
    v = linear_interpolate(hsv1, hsv2, 2, fraction)
    return hsv_to_rgb_int(h,s,v)
    
# Returns a linear mixture of corresponding items from two tuples given by the
# index argument. The fraction argument is the weighting of item 2 in a [0-1] range
def linear_interpolate(one, two, index, fraction):
    fraction = constrain(fraction, 0, 1)
    
    start = one[index]
    end = two[index]
    rval = start + (end - start)*fraction
    return rval
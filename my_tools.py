def shift_coords(x, y, delta_h):
    return (x*delta_h, y*delta_h)

def set_voltage_dynodes(n_dynodes):
    dynodes = []
    potential_dif = 100.0

    for n_dynode  in range(n_dynodes):
        dynodes.append((n_dynode + 1)*potential_dif)
    return dynodes



left = slice(0, -2)
center = slice(1, -1)
right = slice(2, None)
all = slice(None, None)
edades = [12, 11, 24, 36, 8, 6, 10, 41, 32, 58, 14, 50, 7];

def mayorEdades(edad):
    return edad >= 18;

edadesMayores = list(filter(mayorEdades, edades));

print(edadesMayores);
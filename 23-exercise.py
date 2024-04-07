numeros = [4, 9, 16, 25];

numeros2 = [2, 3, 4, 5];

def elevarCuadrado(number):
    return pow(number, 2);

numerosElevados1 = list(map(elevarCuadrado, numeros));
numerosElevados2 = list(map(elevarCuadrado, numeros2));

print(numerosElevados1);
print(numerosElevados2);
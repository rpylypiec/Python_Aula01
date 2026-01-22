CONSTANTE_BONUS = 1000

# 1. Solicite ao usuário que digite o seu nome:
nome_usuario = input("Digite o seu nome:")

# 2. Solicite ao usuário que digite o valor do seu salário.
# Converta a entrada para float.
salario_usuario = float(input("Digite o valor do salário:"))

# 3. Solicite ao usuário que digite o valor do bônus recebido.
# Converta a entrada para float.
valor_bonus = float(input("Digite o valor do bônus recebido:"))

# 4. Calcule o valor do bônus final.
valor_final = CONSTANTE_BONUS + salario_usuario * valor_bonus

# 5. Imprima o nome do usuário e o valor do bônus.
print(f"O usuário: {nome_usuario} possui um bônus de: {valor_final}")

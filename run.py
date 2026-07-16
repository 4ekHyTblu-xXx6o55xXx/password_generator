# from password_generator import PasswordGenerator
#
# gen = PasswordGenerator(length=20)
# print(gen.generate())
from password_generator import PasswordGenerator

gen = PasswordGenerator(length=20)
pwd = gen.generate()
print(f"Пароль: {pwd}")
print(f"Энтропия: {gen.entropy(pwd):.1f} бит")
print(f"Стойкость: {gen.strength_label(gen.entropy(pwd))}")
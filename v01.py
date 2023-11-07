
print('Bem vindo ao programa para entrada com usuario e senha')
print('1 entre com o nome de usuario e em seguida a senha ')

usuario = input('Digite seu nome de usuario: ')
senha = int(input('digite sua senha: '))
senha_correta = 554433

if usuario == 'admin' and senha == senha_correta:
    print('login realizado com sucesso!')
    

else:
    print('Senha e/ou usuario incorreto, tente novamente')

print('fim do codigo')

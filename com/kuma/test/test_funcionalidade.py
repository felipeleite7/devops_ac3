print('Bem-vindo, faça seu login')

email = 'felipe.leite@aluno.fucaldadeimpacta.com.br'
password = 1237

def usuario(usuario, banco):
    if usuario == banco:
        return 'Logando'
        
def senha(senha, banco):
    if senha == banco:
        return 'Logando'
    
def test_aprovado():
	assert usuario(email, 'felipe.leite@aluno.fucaldadeimpacta.com.br') == 'Logando'
    
def test_aprovado_senha():
	assert senha(password, 1237) == 'Logando'
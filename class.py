class Aluno:
    def __init__(self,ra='',digito='',nome='',cidadeNascimento='',dtNascimento='',ufNascimento=''):
        self.ra=ra
        self.digito=digito
        self.nome=nome
        self.cidadeNascimento=cidadeNascimento
        self.dtNascimento=dtNascimento
        self.ufNascimento=ufNascimento

    def getRaDigito(self):
        self.ra=input('Insíra o RA:\n')
        self.digito=input('Insíra o Dígito do RA:\n')
        

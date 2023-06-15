class aluno:
    def __init__(self, nome, idade, n1, n2, n3):
        self.nome = nome
        self.idade = idade
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        
        
    def apresentar(self):
        print('Meu nome é',self.nome, 'e minha idade é', self.idade)
        
        
    def notas(self):
        media = (self.n1+self.n2+self.n3)/3
        if media >= 7:
          print('Aprovado!')
        else:
            print('Reprovado!')
        
aluno1 = aluno('Sergio', 20, 7, 7, 7)
aluno1.apresentar()
aluno1.notas()




 
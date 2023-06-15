class pessoa:
    def __init__(self,nome,idade,cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        
        
    def apresentar(self):
        print('Ola meu nome é:',self.nome)
        
        
    def envelhecer(self,anos):
        self.idade += anos     
        print('A nova idade é:',self.idade)
        
    def mostrarcpf(self):
        print('Esse é meu cpf:',self.cpf)
      
pessoa1 = pessoa('Sergio', 20)
 
pessoa1.apresentar()
pessoa1.idade()

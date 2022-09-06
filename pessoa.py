class Pessoa:
    
    def __init__(self, cpf, nome, idade):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        
    def get_documento(self):
        return self.cpf
    
    def get_nome(self):
        return self.nome
    
    def get_idade(self):
        return self.idade
    
    def is_fumante(self, tipo=""):
        if tipo.upper() == "F":
            return "Sim"
        elif tipo.upper() == "N":
            return "Não"
        else:
            return "Não foi possível identificar" 


def gera_pessoa():
    pessoa = Pessoa("010.868.800-30", "Maria Aparecida", 26)
    fumante = pessoa.is_fumante("N")
    
    print(f"Informações da pessoa:\n \
        CPF: {pessoa.get_cpf()}\n \
        Nome: {pessoa.get_nome()}\n \
        Idade: {pessoa.get_idade()} anos\n \
        Fumante: {fumante}\n")


gera_pessoa()
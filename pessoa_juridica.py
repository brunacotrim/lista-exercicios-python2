from pessoa import Pessoa

class PessoaJuridica(Pessoa):
    
    def __init__(self, cpf, nome, idade, cnpj):
        self.cnpj = cnpj
        super().__init__(cpf, nome, idade)
    
    def get_documento(self):
        return self.cnpj
    

def gera_pessoa_juridica():

    pessoa_juridica = PessoaJuridica("", "Tecnologia Digital Ltda", 10, "64.285.761/0001-10")

    print(f"Informações da pessoa jurídica:\n \
        CNPJ: {pessoa_juridica.get_documento()}\n \
        Nome: {pessoa_juridica.get_nome()}\n \
        Idade: {pessoa_juridica.get_idade()} anos\n")


gera_pessoa_juridica()
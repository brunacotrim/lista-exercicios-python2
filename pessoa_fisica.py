from pessoa import Pessoa

class PessoaFisica(Pessoa):
    
    def __init__(self, cpf, nome, idade, profissao):
        self.profissao = profissao
        super().__init__(cpf, nome, idade)
    
    def get_profissao(self):
        return self.profissao
    
    
def gera_pessoa_fisica():

    pesso_fisica = PessoaFisica("340.902.140-09", "Bruna Viotto Cotrim", 32, "Desenvolvedora de Software")
    profissao = pesso_fisica.get_profissao()

    print(f"Informações da pessoa física:\n \
        CPF: {pesso_fisica.get_documento()}\n \
        Nome: {pesso_fisica.get_nome()}\n \
        Idade: {pesso_fisica.get_idade()} anos\n \
        Profissão: {profissao}")


gera_pessoa_fisica()
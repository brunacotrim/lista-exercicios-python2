class Professor:
    
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.__salario = salario
        
    def get_nome(self):      
        return self.nome
    
    def get_idade(self):      
        return self.idade
        
    def __get_salario(self):      
        return f'R$ {self.__salario:.2f}'

    def acessar_salario(self, usuario):
        if usuario.upper() == "JOAOSILVA":
            return self.__get_salario()
        return f"O usuário {usuario} não tem autorização para acessar esta informação."


def gera_professor():

    professor = Professor("João da Silva", 32, 5126.00)
    salario = professor.acessar_salario("joaosilva")

    print(f"Informações do professor:\n \
        Nome: {professor.get_nome()}\n \
        Idade: {professor.get_idade()} anos\n \
        Salário: {salario}\n")


gera_professor()
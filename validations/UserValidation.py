from validations.Validation import Validation

# define a classe UserValidation, que é uma subclasse de Validation
class UserValidation(Validation):
    # define as regras de validação para cada campo do formulário
    rules = {
        "nome": ["min:0","max:20","required","type:string"],
        "sobrenone": ["min:0","max:20","required","type:string"],
        "email": ["min:0","max:20","required","type:string"],
        "senha": ["min:0","max:20","required","type:string"],
    }

    # define as mensagens de erro para cada regra de validação
    error_msg = {
        "nome.min": "o campo precisa ter no minimo 1 caractere",
        "nome.max": "o campo pode ter no maximo 20 caractere",
        "nome.required": "o campo é requerido",
        "nome.type": "o campro precisa ser tipo texto"
    }

    # define o construtor da classe, que chama o construtor da superclasse Validation
    def __init__(self):
        super().__init__(self.rules or {}, self.error_msg or {})
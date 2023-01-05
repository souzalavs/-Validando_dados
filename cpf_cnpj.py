from validate_docbr import CPF, CNPJ

class Documento:
    @staticmethod
    def cria_novo_documento(documento):
        doc = str(documento)
        if len(doc) == 11:
            return Cpf(documento)
        if len(doc) == 14:
            return Cnpj(documento)
        else: 
            raise ValueError("Documento incorreto")

class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido")
        
    def __str__(self):
        return self.formatador()
    
    def valida(self, cpf):
        validador = CPF()
        return validador.validate(cpf)
            
    def formatador(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
    
class Cnpj:
    def __init__(self, documento):
        documento = str(documento)
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CPNJ inválido")
    
    def valida(self, cnpj):
        validador = CNPJ()
        return validador.validate(cnpj)
    
    def __str__(self):
        return self.formatador()
    
    def formatador(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
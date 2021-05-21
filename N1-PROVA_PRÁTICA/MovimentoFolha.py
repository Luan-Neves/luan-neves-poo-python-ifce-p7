class MovimentoFolha():
    def __init__(self, colaborador, descricao, valor, tipoMovimento):
        self._colaborador = colaborador
        self._descricao = descricao
        self._valor = valor
        self._tipomovimento = tipoMovimento
        
    def getColaborador(self):
        return self._colaborador

    def getDescricao(self):
        return self._descricao

    def getValor(self):
        return self._valor

    def getTipomovimento(self):
        return self._tipomovimento

    def setColaborador(self, colab):
        self._colaborador = colab

    def setDescricao(self, descri):
        self._descricao = descri

    def setValor(self, valor):
        self._valor = valor

    def setTipoMovimento(self, type):
        self._tipomovimento = type
class FolhaPagamento():
    def __init__(self, mes, ano):
        self._mes = mes
        self._ano = ano
        self._totalDesconto = 0.0
        self._totalProvento = 0.0
        self._totalSalario = 0.0
        self.movimentos = []

    def inserirMovimentos(self, mov):
        self.movimentos.append(mov)

    def calcularFolha(self):
        can = ''
        for x in self.movimentos: 
            ca = x.getColaborador().getCodigo()
            if ca != can:
                self._totalSalario += x.getColaborador().getSalario()

            if x.getTipomovimento() == 'P':
                self._totalProvento += x.getValor()
            elif x.getTipomovimento() == 'D':
                self._totalDesconto += x.getValor()

            can = x.getColaborador().getCodigo()
    
        return f'\nTotal de Salários:  {self.getTotalSalarios()}\
                 \nTotal de Proventos: {self.getTotalProventos()}\
                 \nTotal de Descontos: {self.getTotalDescontos()}\
                 \nTotal a Pagar:      {self.getTotalSalarios() + self.getTotalProventos() - self.getTotalDescontos()}\n'
    
    def getMes(self):
        return self._mes

    def getTotalDescontos(self):
        return self._totalDesconto

    def getTotalProventos(self):
        return self._totalProvento

    def getTotalSalarios(self):
        return self._totalSalario


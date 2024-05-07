class Palestrante:
    def __init__(self, id, biografia, especializacao, outroseventos, comentarios, avaliacoes) -> None:
        self.id = id
        self.biografia = biografia
        self.especializacao = especializacao
        self.outroseventos = outroseventos
        self.comentarios = comentarios
        self.avaliacoes = avaliacoes

class Sessao:
    def __init__(self, id, descricao, horarios, localizacao, comentarios) -> None:
        self.id = id
        self.descricao = descricao
        self.horarios = horarios
        self.localizacao = localizacao
        self.comentarios = comentarios
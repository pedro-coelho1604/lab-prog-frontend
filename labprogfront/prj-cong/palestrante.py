class Palestrante:
    def __init__(id, biografia, especializacao, outroseventos, comentarios, avaliacoes, self) -> None:
        self.id = id
        self.biografia = biografia
        self.especializacao = especializacao
        self.outroseventos = outroseventos
        self.comentarios = comentarios
        self.avaliacoes = avaliacoes

class Sessao:
    def __init__(id, descricao, horarios, localizacao, comentarios, self) -> None:
        self.id = id
        self.descricao = descricao
        self.horarios = horarios
        self.localizacao = localizacao
        self.comentarios = comentarios
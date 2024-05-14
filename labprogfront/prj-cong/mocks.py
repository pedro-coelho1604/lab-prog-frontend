from palestra import Palestra
from palestrante import Palestrante

# Criando das Palestras
palestra1 = Palestra(
    1,
    'Atividade física para todos',
    'Essa palestra pode mostrar a importância da atividade física para a saúde geral, independentemente da idade ou nível de condicionamento físico. O palestrante pode falar sobre os diferentes tipos de exercícios, como encontrar uma atividade que você goste e como se manter motivado.',
    22,
    'Maio',
    [1],
    'img/exercicio.png',
    'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d472693.95083578053!2d-44.02402927596853!3d-22.243057371872034!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x99311c850808bf%3A0xc2a1c73968947a77!2sCentro%20de%20Conven%C3%A7%C3%B5es%20General%20Sombra!5e0!3m2!1spt-BR!2sbr!4v1715646658642!5m2!1spt-BR!2sbr'
)

palestra2 = Palestra(
    2,
    'Alimentação para uma vida mais saudável',
    'Essa palestra pode abordar os benefícios de uma alimentação balanceada e rica em nutrientes para a saúde física e mental. O palestrante pode falar sobre como escolher os alimentos certos, como preparar refeições saudáveis e saborosas e como evitar alimentos processados e açucarados.',
    30,
    'Maio',
    [1, 2 ],
    'img/alimentacao.png',
    'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d472693.95083578053!2d-44.02402927596853!3d-22.243057371872034!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x99311c850808bf%3A0xc2a1c73968947a77!2sCentro%20de%20Conven%C3%A7%C3%B5es%20General%20Sombra!5e0!3m2!1spt-BR!2sbr!4v1715646658642!5m2!1spt-BR!2sbr'

)

palestra3 = Palestra(
    3,
    'Sono e bem-estar',
    'Essa palestra pode abordar a importância de uma boa noite de sono para a saúde física e mental. O palestrante pode falar sobre os hábitos de sono saudáveis, como criar uma rotina relaxante à noite, evitar a cafeína e o álcool antes de dormir e criar um ambiente de sono propício.',
    10,
    'Junho',
    [3],
    'img/sono.png',
    'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d472693.95083578053!2d-44.02402927596853!3d-22.243057371872034!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x99311c850808bf%3A0xc2a1c73968947a77!2sCentro%20de%20Conven%C3%A7%C3%B5es%20General%20Sombra!5e0!3m2!1spt-BR!2sbr!4v1715646658642!5m2!1spt-BR!2sbr'

)

palestras = [
    palestra1,
    palestra2,
    palestra3
]

# Criando dos Palestrantes
palestrante1 = Palestrante(
    1,
    'Drauzio Varella',
    'Médico oncologista e escritor brasileiro, conhecido por sua comunicação clara e acessível sobre temas de saúde. Ele apresenta o programa de TV "Dr. House" e é autor de diversos livros, como "Guia Prático de Saúde" e "O Médico em Casa". Drauzio Varella é referência nacional em saúde e bem-estar, e suas palestras são sempre informativas e inspiradoras.',
    'img/drauzio-varella.png'
)

palestrante2 = Palestrante(
    2,
    'Fernanda Brum',
    'Psicóloga e palestrante brasileira, especialista em inteligência emocional e gestão de estresse. Ela é autora do livro "Mente Calma, Vida Leve" e ministra palestras sobre como lidar com o estresse, ansiedade e outras emoções difíceis. Fernanda Brum é uma palestrante motivadora que ajuda as pessoas a viverem uma vida mais feliz e saudável.',
    'img/fernanda-brum.png'
)

palestrante3 = Palestrante(
    3,
    'Marcelo Veronesi',
    'Médico oncologista e escritor brasileiro, especialista em medicina integrativa. Ele é autor do livro "Mais Saúde, Menos Doutor" e defende um enfoque holístico da saúde, que leva em consideração o bem-estar físico, mental, emocional e social. Marcelo Veronesi é um palestrante inspirador que mostra como podemos cuidar da nossa saúde de forma mais completa e eficaz.',
    'img/marcelo-veronesi.png'
)

palestrantes = [
    palestrante1,
    palestrante2,
    palestrante3
]
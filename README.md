# RPG Quest Python

Protótipo de combate por turnos em Python, criado para praticar orientação a objetos, estado de personagens e cálculo de dano.

## Funcionalidades atuais

- Personagens com vida, ataque e defesa.
- Validação de atributos básicos dos personagens.
- Redução de dano conforme a defesa, com dano mínimo de um ponto.
- Combate em rodadas com valores aleatórios de dano.
- Limite de dez rodadas; se ambos continuarem vivos, o resultado é `Draw`.
- Exibição do combate e do resultado no terminal.
- Escolha do nome do herói e de um entre três inimigos pela linha de comando.
- Semente opcional para reproduzir uma batalha com os mesmos valores aleatórios.
- Exportação opcional de resultado JSON para integrar outras interfaces.
- Testes automatizados para atributos, dano, vitória, combate inválido e empate por limite de rodadas.

O README descreve somente o comportamento implementado em `main.py`; inventário, equipamentos e progressão de experiência ainda não fazem parte do protótipo.

## Requisitos

- Python 3.10+ recomendado
- Nenhuma dependência externa para a versão atual

## Executar

```bash
python main.py
python main.py --hero-name João --enemy orc --seed 42
python main.py --hero-name João --enemy orc --seed 42 --format json
```

Com `--format json`, a saída é um objeto JSON válido contendo `winner`, estado final de `hero` e `enemy` (nome, vida atual e máxima), `max_rounds` e `events` (mensagens do combate). O padrão continua sendo `--format text`, compatível com a saída antiga. Com a mesma `--seed`, a simulação gera resultados reproduzíveis, úteis para integrar uma interface web ou testar a lógica.

As opções de inimigo são `goblin`, `orc` e `spider`. Use a mesma semente para reproduzir a sequência de dano. O argumento `--rounds` aceita somente inteiros de **1 a 1000**; entradas inválidas exibem uma mensagem de uso e saem com código 2, sem traceback, tanto em texto quanto em JSON.

## Testes

```bash
python -m unittest discover -s tests -v
```

## Estrutura

```text
.
├── main.py
├── tests/
│   └── test_main.py
├── README.md
└── VSCODE_SETUP.md
```

## Próximas melhorias

- Separar regras de combate e interface de terminal.
- Ampliar a validação de tipos dos atributos de entrada.

## Objetivo de aprendizagem

O projeto é um exercício incremental de Python. A prioridade é manter regras simples, testar os casos extremos e documentar cada funcionalidade conforme for implementada.

## Validação e manutenção

Consulte o [guia técnico de validação](docs/GUIA_DE_VALIDACAO.md) antes de alterar o código: ele reúne os comandos, casos de regressão e limites atuais do projeto.

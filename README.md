# RPG Quest Python

Protótipo de combate por turnos em Python, criado para praticar orientação a objetos, estado de personagens e cálculo de dano.

## Funcionalidades atuais

- Personagens com vida, ataque e defesa.
- Validação de atributos básicos dos personagens.
- Redução de dano conforme a defesa, com dano mínimo de um ponto.
- Combate em rodadas com valores aleatórios de dano.
- Limite padrão de dez rodadas, configurável de 1 a 1000; se ambos continuarem vivos, o resultado é `Draw`.
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

Com `--format json`, a saída é um objeto JSON válido contendo `winner`, estado final de `hero` e `enemy` (nome, vida atual e máxima), `max_rounds` e `events` (mensagens do combate). A exportação usa escapes JSON para preservar acentos e símbolos em ambientes com codificação legada. O padrão continua sendo `--format text`, compatível com a saída antiga. Com a mesma `--seed`, a simulação gera resultados reproduzíveis, úteis para integrar uma interface web ou testar a lógica.

As opções de inimigo são `goblin`, `orc` e `spider`. Use a mesma semente para reproduzir a sequência de dano. O argumento `--rounds` aceita somente inteiros de **1 a 1000**; entradas inválidas exibem uma mensagem de uso e saem com código 2, sem traceback, tanto em texto quanto em JSON.

## Regras de combate e integração

O herói começa com 100 HP, ataque 18 e defesa 5. A tabela abaixo descreve os adversários definidos em `main.py`:

| Inimigo | HP | Ataque | Defesa |
| --- | ---: | ---: | ---: |
| goblin | 40 | 12 | 2 |
| orc | 70 | 15 | 4 |
| spider | 30 | 10 | 1 |

Em cada rodada, o herói ataca primeiro, somando de 1 a 5 ao ataque. Se o monstro sobreviver, responde com ataque acrescido de 1 a 3. A defesa reduz o dano, com mínimo de 1, limitado à vida restante. `battle()` altera o HP dos personagens recebidos; crie novas instâncias para repetir um combate desde o início. O parâmetro `emit` permite capturar mensagens sem imprimir no terminal.

Nomes são aparados, limitados a 80 caracteres e não podem conter caracteres de controle ASCII. Vida máxima deve ser positiva; ataque e defesa devem ser inteiros não negativos, sem booleanos. A CLI rejeita entradas inválidas com código 2.

Para salvar uma simulação reproduzível em arquivo:

```bash
python main.py --hero-name Arthur --enemy orc --seed 42 --rounds 20 --format json > batalha.json
```

O resultado JSON não registra a semente: preserve também os argumentos usados caso queira repetir a simulação.

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

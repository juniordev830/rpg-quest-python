# RPG Quest Python

Protótipo de combate por turnos em Python, criado para praticar orientação a objetos, estado de personagens e cálculo de dano.

## Funcionalidades atuais

- Personagens com vida, ataque e defesa.
- Redução de dano conforme a defesa.
- Combate em rodadas com valores aleatórios de dano.
- Limite de rodadas para encerrar o combate.
- Exibição do resultado no terminal.

O README descreve somente o comportamento implementado em `main.py`; inventário, equipamentos, progressão de experiência e outras mecânicas podem ser adicionados em etapas futuras.

## Requisitos

- Python 3.10+ recomendado
- Nenhuma dependência externa para a versão atual

## Executar

```bash
python main.py
```

## Estrutura

```text
.
├── main.py
├── .gitignore
└── README.md
```

## Próximas melhorias

- Separar regras de combate e interface de terminal.
- Corrigir o tratamento do resultado quando o combate termina por limite de rodadas.
- Testes automatizados cobrem validação de atributos, dano, vitória e empate.
- Permitir escolher personagem e inimigo sem editar o código.
- Adicionar configurações para tornar as rodadas reproduzíveis nos testes.

## Objetivo de aprendizagem

O projeto é um exercício incremental de Python. A prioridade é manter regras simples, testar os casos extremos e documentar cada funcionalidade conforme for implementada.

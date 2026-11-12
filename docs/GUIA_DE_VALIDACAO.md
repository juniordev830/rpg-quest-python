# Verificação e evolução — RPG Quest Python

## Escopo confirmado

Combate de turnos em Python com semente opcional, escolha de inimigo e saída JSON.

## Localização do código

`main.py`, `tests/test_main.py`, `tests/test_cli.py`.

## Verificar localmente

`python main.py --help` para ver opções; `python -m pytest tests -q` para regressão.

Use dados fictícios e registre no PR o comando, ambiente e resultado observado. Para projetos sem runtime instalado, marque a verificação como pendente em vez de afirmar que passou.

## Casos de regressão a cobrir

Verificar dano mínimo, empates no limite de dez rodadas, semente reproduzível, valores de defesa extremos e tratamento de entradas CLI inválidas.

## Limitações e próximo incremento

Não confundir com RPG 3D executável; a implementação da main é de terminal. Evoluir inventário somente com testes para estado e regras.

## Critérios de revisão

- [ ] O comportamento alterado está descrito com exemplo reproduzível.
- [ ] Há teste ou procedimento de validação compatível com o código real.
- [ ] Nenhuma chave, dado pessoal ou arquivo gerado foi incluído sem necessidade.
- [ ] A documentação distingue o implementado do planejado.

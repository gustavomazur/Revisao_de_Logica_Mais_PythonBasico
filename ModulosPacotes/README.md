# Módulos e Pacotes

Conteúdo do curso **Curso em Vídeo — Módulos e Pacotes em Python**.
Prática de organização de código em módulos, importação e criação de pacotes.

## Pré-requisitos

- Python 3.x

## O que são módulos e pacotes

> Organização do código, facilidade na manutenção, ocultação de código detalhado e
> reutilização em outros projetos. Se ficar muito grande, a solução é usar pacotes:
> cada pasta é um pacote, e dentro dela ficam vários módulos (`__init__.py`).

## Estrutura

| Exercício | Tema |
|-----------|------|
| aula22.py | Importando `uteis.numeros` — fatorial e dobro de um número |
| ex107 | Funções `metade`, `dobro` e `aumentar` do módulo `exercio107/moeda.py` |
| ex108 | Formatação com a função `moeda()` — valores em R$ |
| ex109 | Formatação com parâmetro opcional (`True`) para mostrar ou não o valor formatado |
| ex110 | Função `resumo()` no módulo `exercio110` — preço com aumento e redução |
| ex111 | Pacote `exercio111/utilidades/moeda` — função `resumo()` do pacote |
| ex112 | Pacote `exercio112/utilidades` — `dado.leiaDinheiro()` + `moeda.resumo()` |
| uteis/ | Pacote com `__init__.py` e subpacote `numeros/` (fatorial, dobro) |

## Observações

- Os módulos usados por cada exercício ficam dentro das pastas `exercio107` a `exercio112`.
- Os pacotes `utilidades` e `uteis` possuem arquivos `__init__.py` para serem importados como pacotes.
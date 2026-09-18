# Tratamento de Erros e Exceções

Conteúdo do curso **Curso em Vídeo — Tratamento de Erros (Aula 23)**.
Prática de `try`, `except`, `else` e `finally` para tratar exceções em Python.

## Pré-requisitos

- Python 3.x
- Conexão com a internet (apenas para o ex114)

## Estrutura

| Exercício | Tema |
|-----------|------|
| aula23/explicao23.py | Explicação de exceções (`NameError`, `ValueError`, `ZeroDivisionError`, `TypeError`, `IndexError`, `ModuleNotFoundError`) + exemplo prático com `try/except/else/finally` |
| ex113 | Funções `leiaInt()` e `leiaFloat()` — validação com `try/except` e `KeyboardInterrupt` |
| ex114 | Verifica se um site está acessível usando `urllib.request` (LinkedIn) |

## Observações

- O ex113 pede o número até o usuário digitar um valor válido, usando cores ANSI nos erros.
- O ex114 retorna o código de status HTTP do site ou avisa se ele não estiver acessível.
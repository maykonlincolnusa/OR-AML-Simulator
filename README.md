# OR AML Simulator

Gerador de dados sintéticos para testar modelos, regras e investigações de prevenção à lavagem de dinheiro sem usar dados pessoais reais.

## MVP

- Gerar clientes, contas e transações normais reproduzíveis por seed.
- Simular fan-in, fan-out, ciclo, pass-through e fracionamento.
- Exportar CSV com rótulo e explicação do cenário.
- Validar valores, moedas, timestamps e integridade referencial.

## Próximo passo

O pacote já gera, por seed, transações normais e cenários de ciclo, pass-through e fracionamento. Próximo: adicionar exportação CSV e um CLI compatível com o OR Trace.


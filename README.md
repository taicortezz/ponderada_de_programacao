# Projeto de Aferição de Qualidade: Case Netflix
## Engenharia de Software e Especificação como Código

Este projeto demonstra o conceito de Requisitos como Código, onde critérios de aceitação (RF) e atributos de qualidade (RNF) são validados automaticamente por testes executáveis. O objetivo é garantir que a arquitetura suporte a operação mesmo em cenários de falha.

## 1. Mapeamento de Requisitos (Matriz de Rastreabilidade)

| Tipo | Requisito | Atributo ISO 25010 | Tática | Mecanismo |
| :--- | :--- | :--- | :--- | :--- |
| **RF1** | Persistência na "Minha Lista" | Adequação Funcional | Apoio à Operação | Armazenamento de Estado |
| **RNF1** | Resiliência na Recomendação | **Confiabilidade** (Maturidade e Tolerância a Falhas) | **Recuperar** | **Fallback** (Lista Padrão) |
| **RNF2** | Performance de Resposta | **Eficiência de Performance** (Comportamento Temporal) | **Detectar** | **SLA de Latência** |



## 2. Abordagem Técnica
Para garantir uma aferição determinística, utilizamos a biblioteca `unittest.mock`. 
- **RF1:** Validamos não apenas o retorno da função, mas a integridade da lista após a operação.
- **RNF1 e RNF2:** Simulamos uma falha crítica no serviço de IA (IA-Service) usando `side_effect`. O código deve detectar a falha em tempo real, ativar o Fallback (Recuperação) e manter o tempo de resposta dentro do SLA de 200ms.


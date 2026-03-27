Feature: Sistema de Recomendação e Lista Pessoal

  @funcional
  Scenario: RF1 - Adicionar conteúdos à lista pessoal e persistir corretamente
    Given que o usuário "Tainá" está autenticado
    When ela adiciona o filme "Stranger Things" à sua lista
    Then o sistema deve confirmar o salvamento
    And o filme "Stranger Things" deve estar presente na lista do perfil

  @nao_funcional
  Scenario: RNF1/RNF2 - Tolerância a falhas e Performance no serviço de IA
    Given que o serviço de recomendações personalizadas (IA) está instável
    When o usuário acessa a página inicial do sistema
    Then o sistema deve RECUPERAR a operação exibindo a "Lista Padrão"
    And a lista retornada não deve estar vazia
    And o tempo total de resposta deve ser inferior a 200ms
from behave import given, when, then
from unittest.mock import MagicMock
import time

# Módulos do Sistema (Simulação da Lógica de Negócio) 

class NetflixSystem:
    def __init__(self, usuario):
        self.usuario = usuario
        self.minha_lista = []
        self.ia_service = None # Serviço de recomendação externo

    def salvar_na_lista(self, titulo):
        # simulando persistencia de dados
        if titulo:
            self.minha_lista.append(titulo)
            return True
        return False

    def carregar_home(self):
        try:
            # tentativa de integração com serviço de IA
            return self.ia_service.get_personalizada()
        except Exception:
            # Tática de robustez: RECUPERAR (ISO 25010 - Tolerância a Falhas)
            # Mecanismo: Fallback para conteúdo estático de segurança
            return ["Top 10 Brasil", "Populares", "Lançamentos"]

# Implementação dos Steps de Aferição 

@given('que o usuário "{nome}" está autenticado')
def step_impl(context, nome):
    context.app = NetflixSystem(usuario=nome)

@when('ela adiciona o filme "{filme}" à sua lista')
def step_impl(context, filme):
    context.status_operacao = context.app.salvar_na_lista(filme)

@then('o sistema deve confirmar o salvamento')
def step_impl(context):
    assert context.status_operacao is True

@then('o filme "{filme}" deve estar presente na lista do perfil')
def step_impl(context, filme):
    # Validação rigorosa do RF (Persistência)
    assert filme in context.app.minha_lista

@given('que o serviço de recomendações personalizadas (IA) está instável')
def step_impl(context):
    context.app = NetflixSystem(usuario="Tainá")
    # Configuração do MOCK com side_effect para simular falha real de integração
    context.app.ia_service = MagicMock()
    context.app.ia_service.get_personalizada.side_effect = Exception("Timeout/Internal Error")

@when('o usuário acessa a página inicial do sistema')
def step_impl(context):
    start = time.time()
    context.resultado_home = context.app.carregar_home()
    context.latencia = (time.time() - start) * 1000 # Cálculo em milissegundos

@then('o sistema deve RECUPERAR a operação exibindo a "{lista}"')
def step_impl(context, lista):
    # aferição da Tática de Recuperação
    assert "Top 10 Brasil" in context.resultado_home

@then('a lista retornada não deve estar vazia')
def step_impl(context):
    # Garantia de que o fallback entregou valor útil ao usuário
    assert len(context.resultado_home) > 0

@then('o tempo total de resposta deve ser inferior a 200ms')
def step_impl(context):
    # aferição de RNF: Eficiência de Performance (ISO 25010)
    assert context.latencia < 200, f"Latência alta: {context.latencia}ms"
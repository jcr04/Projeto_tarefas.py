from app.domain.entities.prioridade import Prioridade
from app.domain.value_objects.data_de_criacao import DataDeCriacao
from app.repositories.repositorio_tarefas import RepositorioTarefas
from app.services.servico_tarefas import ServicoTarefas
from app.presentation.views.tarefas_view import TarefasView
from app.presentation.controllers.tarefas_controller import TarefasController


if __name__ == "__main__":

    repositorio = RepositorioTarefas()
    servico_tarefas = ServicoTarefas(repositorio)
    view = TarefasView()
    controller = TarefasController(servico_tarefas, view)
    
    # Criação de tarefas
    controller.criar_tarefa("Comprar leite", "Ir à mercearia", "Alta", DataDeCriacao(2023, 9, 12))
    controller.criar_tarefa("Estudar Python", "Capítulo 5", "Baixa", DataDeCriacao(2023, 9, 13))
    
    # Listagem de tarefas
    controller.listar_tarefas()
    
    # Conclusão de tarefas
    controller.concluir_tarefa(1)
    
    # Listagem de tarefas pendentes
    controller.listar_tarefas_por_estado(False)
    
    # Edição de tarefas
    controller.editar_tarefa(2, titulo="Estudar Python - Capítulo 6")
    
    # Listagem de tarefas após edição
    controller.listar_tarefas()
    
    # Conclusão de tarefas com data de conclusão
    controller.concluir_tarefa(DataDeCriacao(2023, 10, 1))
    
    # Listagem de tarefas por prioridade
    controller.listar_tarefas_por_prioridade("Alta")
    
    # Deleção de tarefas
    controller.deletar_tarefa(1)
    
    # Atualização de prioridade de tarefas
    controller.atualizar_prioridade(2, Prioridade("Média", 2))
    
    # Listagem de tarefas por categoria
    controller.listar_tarefas_por_categoria("Trabalho")
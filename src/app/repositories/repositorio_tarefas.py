class RepositorioTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        return self.tarefas
    
    def deletar_tarefa(self, id_tarefa):
        self.tarefas = [tarefa for tarefa in self.tarefas if tarefa.id != id_tarefa]

    def obter_tarefa(self, id_tarefa):
        for tarefa in self.tarefas: 
            if tarefa.id == id_tarefa:
                return tarefa
        return None
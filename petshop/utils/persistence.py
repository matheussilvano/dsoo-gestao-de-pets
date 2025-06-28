import pickle
from registry.registry import (
    dono_controller,
    produto_controller,
    servico_controller,
    agendamento_controller,
    despesa_controller,
    venda_controller,
)

# Nome do arquivo onde os dados serão salvos
DATA_FILE = "petshop_data.pkl"

def save_data():
    """
    Coleta os dados de todos os controllers e os salva em um arquivo usando pickle.
    """
    # Coletamos as listas de dados diretamente dos controllers
    data = {
        "donos": dono_controller._donos,
        "produtos": produto_controller._produtos,
        "servicos": servico_controller._servicos,
        "agendamentos": agendamento_controller._agendamentos,
        "despesas": despesa_controller._despesas,
        "vendas": venda_controller._vendas,
    }

    try:
        with open(DATA_FILE, "wb") as f:
            pickle.dump(data, f)
        print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar os dados: {e}")

def load_data():
    """
    Carrega os dados de um arquivo e os restaura nos controllers.
    """
    try:
        with open(DATA_FILE, "rb") as f:
            data = pickle.load(f)

            # Restauramos as listas nos controllers
            dono_controller._donos = data.get("donos", [])
            produto_controller._produtos = data.get("produtos", [])
            servico_controller._servicos = data.get("servicos", [])
            agendamento_controller._agendamentos = data.get("agendamentos", [])
            despesa_controller._despesas = data.get("despesas", [])
            venda_controller._vendas = data.get("vendas", [])
            
            print("Dados carregados com sucesso!")
            # Retorna True se os dados foram carregados
            return True 
            
    except FileNotFoundError:
        print("Arquivo de dados não encontrado. Iniciando com sistema zerado.")
        # Retorna False se o arquivo não existe
        return False
    except Exception as e:
        print(f"Ocorreu um erro ao carregar os dados: {e}")
        # Retorna False em caso de outro erro
        return False
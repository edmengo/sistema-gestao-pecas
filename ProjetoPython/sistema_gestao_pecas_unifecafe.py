import os

class Peca:
    def __init__(self, id_peca, peso, cor, comprimento):
        self.id_peca = id_peca
        self.peso = peso
        self.cor = cor.lower()
        self.comprimento = comprimento
        self.aprovada = False
        self.motivos_reprovacao = []
        self.avaliar_qualidade()

    def avaliar_qualidade(self):
        self.aprovada = True
        self.motivos_reprovacao = []

        if self.peso < 95 or self.peso > 105:
            self.aprovada = False
            self.motivos_reprovacao.append(f"Peso inválidO ({self.peso}g)")

        if self.comprimento < 10 or self.comprimento > 20:
            self.aprovada = False
            self.motivos_reprovacao.append(f"Comprimento inválida ({self.comprimento}cm)")

        if self.cor not in ['azul', 'verde']:
            self.aprovada = False
            self.motivos_reprovacao.append(f"Cor inválida ({self.cor})")

    def __str__(self):
        status = "APROVADA" if self.aprovada else "REPROVADA"
        info = f"ID: {self.id_peca} | Peso: {self.peso}g | Cor: {self.cor} | Comprimento: {self.comprimento}cm | Status: {status}"
        if not self.aprovada:
            info += f"\n  Motivos: {', '.join(self.motivos_reprovacao)}"
        return info


class Caixa:
    CAPACIDADE_MAXIMA = 10

    def __init__(self, numero):
        self.numero = numero
        self.pecas = []
        self.fechada = False

    def adicionar_peca(self, peca):
        if len(self.pecas) < self.CAPACIDADE_MAXIMA and not self.fechada:
            self.pecas.append(peca)
            if len(self.pecas) == self.CAPACIDADE_MAXIMA:
                self.fechar()
            return True
        return False

    def fechar(self):
        self.fechada = True

    def __str__(self):
        status = "FECHADA" if self.fechada else "ABERTA"
        return f"Caixa #{self.numero} - {status} - {len(self.pecas)}/{self.CAPACIDADE_MAXIMA} peças"


class SistemaGestao:
    def __init__(self):
        self.pecas_aprovadas = []
        self.pecas_reprovadas = []
        self.caixas = [Caixa(1)]
        self.proximo_id = 1

    def cadastrar_peca(self, peso, cor, comprimento):
        peca = Peca(self.proximo_id, peso, cor, comprimento)
        self.proximo_id += 1

        if peca.aprovada:
            self.pecas_aprovadas.append(peca)
            if not self.caixas[-1].adicionar_peca(peca):
                nova_caixa = Caixa(len(self.caixas) + 1)
                self.caixas.append(nova_caixa)
                nova_caixa.adicionar_peca(peca)
            print(f"\nPeça #{peca.id_peca} APROVADA e armazenada!")
        else:
            self.pecas_reprovadas.append(peca)
            print(f"\nPeça #{peca.id_peca} REPROVADA!")
            print(f"  Motivos: {', '.join(peca.motivos_reprovacao)}")

        return peca

    def listar_pecas_aprovadas(self):
        if not self.pecas_aprovadas:
            print("\nNenhuma peça aprovada cadastrada.")
            return

        print("\n" + "*"*70)
        print("PEÇAS APROVADAS")
        print("*"*70)
        for peca in self.pecas_aprovadas:
            print(peca)
        print(f"\nTotal: {len(self.pecas_aprovadas)} peça(s)")

    def listar_pecas_reprovadas(self):
        if not self.pecas_reprovadas:
            print("\nNenhuma peça reprovada cadastrada.")
            return

        print("\n" + "*"*70)
        print("PEÇAS REPROVADAS")
        print("*"*70)
        for peca in self.pecas_reprovadas:
            print(peca)
        print(f"\nTotal: {len(self.pecas_reprovadas)} peça(s)")

    def remover_peca(self, id_peca):
        for i, peca in enumerate(self.pecas_aprovadas):
            if peca.id_peca == id_peca:
                self.pecas_aprovadas.pop(i)
                for caixa in self.caixas:
                    for j, p in enumerate(caixa.pecas):
                        if p.id_peca == id_peca:
                            caixa.pecas.pop(j)
                            caixa.fechada = False
                            break
                print(f"\nPeça #{id_peca} removida com sucesso!")
                return True

        for i, peca in enumerate(self.pecas_reprovadas):
            if peca.id_peca == id_peca:
                self.pecas_reprovadas.pop(i)
                print(f"\nPeça #{id_peca} removida com sucesso!")
                return True

        print(f"\nPeça #{id_peca} não encontrada!")
        return False

    def listar_caixas_fechadas(self):
        caixas_fechadas = [c for c in self.caixas if c.fechada]

        if not caixas_fechadas:
            print("\nNenhuma caixa fechada.")
            return

        print("\n" + "*"*70)
        print("CAIXAS FECHADAS")
        print("*"*70)
        for caixa in caixas_fechadas:
            print(f"\n{caixa}")
            print("Peças armazenadas:")
            for peca in caixa.pecas:
                print(f"  - ID: {peca.id_peca} | Peso: {peca.peso}g | Cor: {peca.cor} | Comp: {peca.comprimento}cm")
        print(f"\nTotal: {len(caixas_fechadas)} caixa(s) fechada(s)")

    def gerar_relatorio(self):
        print("\n" + "*"*70)
        print("RELATÓRIO - SGP")
        print("*"*70)

        print(f"\nRESUMO GERAL:")
        print(f"   Total de peças processadas: {len(self.pecas_aprovadas) + len(self.pecas_reprovadas)}")
        print(f"   Peças aprovadas: {len(self.pecas_aprovadas)}")
        print(f"   Peças reprovadas: {len(self.pecas_reprovadas)}")

        print(f"\nARMAZENAMENTO:")
        print(f"   Total de caixas: {len(self.caixas)}")
        print(f"   Caixas fechadas: {len([c for c in self.caixas if c.fechada])}")
        print(f"   Caixas em uso: {len([c for c in self.caixas if not c.fechada])}")

        if self.pecas_reprovadas:
            print(f"\nANÁLISE DE REPROVAÇÕES:")
            motivos = {}
            for peca in self.pecas_reprovadas:
                for motivo in peca.motivos_reprovacao:
                    if motivo not in motivos:
                        motivos[motivo] = 0
                    motivos[motivo] += 1

            print("   Motivos de reprovação:")
            for motivo, quantidade in motivos.items():
                print(f"   - {motivo}: {quantidade} ocorrência(s)")

        taxa_aprovacao = (len(self.pecas_aprovadas) / (len(self.pecas_aprovadas) + len(self.pecas_reprovadas)) * 100) if (len(self.pecas_aprovadas) + len(self.pecas_reprovadas)) > 0 else 0
        print(f"\nTAXA DE APROVAÇÃO: {taxa_aprovacao:.2f}%")
        print("*"*70)


def exibir_menu():
    print("\n" + "*"*70)
    print(" SISTEMA DE GESTÃO DE PEÇAS")
    print("*"*70)
    print("1. Cadastrar peça")
    print("2. Listar peças aprovadas")
    print("3. Listar peças reprovadas")
    print("4. Listar caixas fechadas")
    print("5. Remover peça cadastrada")
    print("6. Gerar relatório")
    print("0. Sair")
    print("*"*70)


def obter_numero(mensagem, tipo=float):
    while True:
        try:
            valor = tipo(input(mensagem))
            return valor
        except ValueError:
            print("Por favor digite uma opção válida.")


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    #os.system('cls' if os.name == 'nt' else 'clear')
    limpar_tela()

    sistema = SistemaGestao()

    print("\n" + "*"*70)
    print("         --- BEM-VINDO AO SGP UNIFECAFE--- ")
    print("*"*70)

    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            limpar_tela()
            print("\n--- CADASTRAR PEÇA ---")
            peso = obter_numero("Peso (g): ", float)
            comprimento = obter_numero("Comprimento (cm): ", float)
            cor = input("Cor: ").strip()
            sistema.cadastrar_peca(peso, cor, comprimento)

        elif opcao == "2":
            limpar_tela()
            sistema.listar_pecas_aprovadas()

        elif opcao == "3":
            limpar_tela()
            sistema.listar_pecas_reprovadas()

        elif opcao == "4":
            limpar_tela()
            sistema.listar_caixas_fechadas()

        elif opcao == "5":
            limpar_tela()
            print("\n--- REMOVER PEÇA ---")
            id_peca = obter_numero("ID da peça a remover: ", int)
            sistema.remover_peca(id_peca)

        elif opcao == "6":
            limpar_tela()
            sistema.gerar_relatorio()

        elif opcao == "0":
            print("\n" + "*"*70)
            print("Encerrando sistema...")
            print("Obrigado por usar o Sistema de Gestão de Peças Unifecafe!")
            print("*"*70 + "\n")
            break

        else:
            limpar_tela()
            print("\nOpção inválida! Tente novamente.")

        input("\nPressione ENTER para continuar...")
        limpar_tela()

if __name__ == "__main__":
    main()

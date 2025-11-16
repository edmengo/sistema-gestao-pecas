Sistema de Automação: Gestão de Peças Industriais

Sobre o Projeto Sistema desenvolvido em Python para automação do controle de produção e qualidade de peças industriais.
A solução substitui processos manuais de inspeção, reduzindo atrasos, falhas de conferência e custos operacionais.

Funcionalidades 
• Cadastro automático de peças com validação de qualidade 
• Avaliação automática baseada em critérios pré-definidos 
• Armazenamento inteligente em caixas (10 peças/caixa) 
• Gerenciamento automático de caixas (fechamento e abertura de novas) 
• Relatórios consolidados com estatísticas detalhadas 
• Rastreamento de peças reprovadas com motivos específicos • Remoção de peças cadastradas

Critérios de Qualidade Uma peça é aprovada quando atende TODOS os seguintes critérios:

Característica Critério de Aprovação Peso Entre 95g e 105g Cor Azul ou Verde Comprimento Entre 10cm e 20cm

Como Executar Pré-requisitos 
• Python 3.7 ou superior instalado 
• Nenhuma biblioteca externa é necessária (usa apenas bibliotecas padrão)

Passo a Passo

Clone o repositório ou baixe o arquivo 
git clone https://github.com/edmengo/sistema-gestao-pecas.git 
cd sistema-gestao-pecas

Execute o programa python sistema_gestao_pecas.py

Interaja com o menu o Use os números de 0 a 6 para navegar pelas opções o Siga as instruções na tela para cada operação Menu do Sistema

Cadastrar peça

Listar peças aprovadas

Listar peças reprovadas

Listar caixas fechadas

Remover peça cadastrada

Gerar relatório

Sair

Exemplos de Uso

Exemplo 1: Cadastrando uma Peça Aprovada Entrada: Escolha uma opção: 1 Peso (g): 100 Cor: azul Comprimento (cm): 15

Saída: Peça #1 APROVADA e armazenada! Exemplo 2: Cadastrando uma Peça Reprovada Entrada:

Escolha uma opção: 1 Peso (g): 110 Cor: vermelho Comprimento (cm): 25

Saída: Peça #2 REPROVADA! Motivos: Peso fora do padrão (110.0g), Cor inválida (vermelho), Comprimento fora do padrão (25.0cm)

Exemplo 3: Relatório Final Saída:

RESUMO GERAL: Total de peças processadas: 25 Peças aprovadas: 20 Peças reprovadas: 5

ARMAZENAMENTO: Total de caixas: 2 Caixas fechadas: 2 Caixas em uso: 0

ANÁLISE DE REPROVAÇÕES: Motivos de reprovação:

Peso fora do padrão (110.0g): 2 ocorrência(s)
Cor inválida (vermelho): 3 ocorrência(s)
TAXA DE APROVAÇÃO: 80.00%

Estrutura do Código Classes Principais

Peca Representa uma peça individual com: 
• Atributos: id, peso, cor, comprimento, status 
• Método avaliar_qualidade(): valida critérios automaticamente

Caixa Gerencia o armazenamento de peças: 
• Capacidade máxima: 10 peças 
• Fechamento automático ao atingir limite 
• Controle de estado (aberta/fechada)

SistemaGestao Sistema principal que coordena: 
• Cadastro e avaliação de peças 
• Gerenciamento de caixas 
• Geração de relatórios 
• Operações CRUD de peças

Lógica de Programação Aplicada 
• Estruturas Condicionais: Validação de critérios de qualidade 
• Estruturas de Repetição: Navegação no menu e iteração de listas 
• Orientação a Objetos: Classes para modularização 
• Listas e Arrays: Armazenamento dinâmico de dados 
• Funções: Reutilização de código e organização 
• Tratamento de Exceções: Validação de entradas do usuário

Benefícios da Solução 
• Redução de erros: Eliminação de falhas humanas na inspeção 
• Agilidade: Processamento instantâneo de validações 
• Rastreabilidade: Histórico completo de peças e motivos de reprovação 
• Economia: Redução de custos operacionais 
• Análise: Relatórios detalhados para tomada de decisão

Expansões Futuras Este protótipo pode ser expandido para:

• Inteligência Artificial: Predição de falhas e otimização de qualidade 
• Banco de Dados: Persistência permanente de informações 
• Interface Gráfica: Visual com gráficos em tempo real 
• API REST: Integração com outros sistemas

link do video: https://drive.google.com/file/d/1rce09yKZXigR_dOwcom0GKLRjcZliSWR/view?usp=drive_link

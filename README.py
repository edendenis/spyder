#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar o `Spyder` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar o `Spyder` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _In this document are contained the main commands and settings to set up/install the `Spyder` on `Linux Ubuntu`._

# ## Descrição [2]
# 
# ### `Spyder`
# 
# O Spyder é um ambiente de desenvolvimento integrado (IDE) de código aberto e especializado em Python, projetado para cientistas de dados e programadores que trabalham com análise de dados, aprendizado de máquina e processamento numérico. Ele oferece uma variedade de recursos poderosos, incluindo um editor de código com realce de sintaxe, janelas interativas para visualização de variáveis e gráficos, integração com bibliotecas populares de ciência de dados, como NumPy e Pandas, além de uma interface de usuário intuitiva que simplifica o processo de análise de dados. O Spyder também suporta a criação de notebooks Jupyter, o que o torna uma escolha valiosa para tarefas de exploração de dados e prototipagem rápida em Python. Com sua ênfase na produtividade e na análise de dados, o Spyder é uma ferramenta essencial para profissionais que trabalham em projetos de ciência de dados e programação científica.

# ## 1. Como configurar/instalar o `Spyder` no Linux Ubuntu [1]
# 
# Para instalar o `Spyder` no Linux Ubuntu, você pode seguir estes passos:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# 3. **Instale o `Spyder`:** Você pode instalar o `Spyder` diretamente dos repositórios do Ubuntu usando o `apt`. No terminal, digite: `sudo apt install spyder -y`
# 
# 4. **Executar o `Spyder`:** Depois de instalado, você pode iniciar o `Spyder` a partir do terminal com o comando: `spyder`
# 
#     Ou pode encontrá-lo e abri-lo através do menu de aplicativos do seu sistema.
# 
# **Nota:** Se você deseja uma versão específica do `Spyder` ou quer garantir que está obtendo a versão mais recente, pode considerar instalá-lo dentro de um ambiente virtual `Python` usando o `pip`. Para isso, você precisaria instalar o `Python` e o `pip`, criar um ambiente virtual e então instalar o `Spyder` nesse ambiente. No entanto, para a maioria dos usuários, a instalação direta pelo `apt` como descrito acima é suficiente e mais simples.

# ## 2. Código completo para configurar/instalar
# 
# Para instalar o `Spyder` no Linux Ubuntu sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt clean                                                            
#     sudo apt autoclean
#     sudo apt autoremove -y
#     sudo apt update
#     sudo apt --fix-broken install
#     sudo apt clean
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     sudo apt install spyder -y
#     spyder
#     ```
# 

# ## Referências
# 
# [1] OPENAI. ***Instalar spyder no ubuntu:*** https://chat.openai.com/c/5c1a1acc-664b-4adc-8464-c8e597ca02ad (texto adaptado). ChatGPT. Acessado em: 22/11/2023 08:25.
# 
# [2] OPENAI. ***Vs code: editor popular:*** https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42 (texto adaptado). ChatGPT. Acessado em: 21/11/2023 09:46.

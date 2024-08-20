
# Projeto de Engenharia de Dados na AWS(Teste)

Este projeto demonstra um pipeline de engenharia de dados construído na AWS, utilizando diversos serviços em nuvem para computação, armazenamento, processamento de dados e análises.

## Arquitetura do Projeto

### 1. **Computação**
   - **Amazon EC2**: Usado para executar cargas de trabalho flexíveis e gerenciar scripts ou aplicações personalizadas.
   - **AWS Lambda**: Funções serverless acionadas por eventos, com escalabilidade automática e execução sob demanda.

### 2. **Ferramentas de Desenvolvimento**
   - **AWS CodeCommit**: Serviço de controle de versão totalmente gerenciado, hospedando os repositórios Git do projeto.

### 3. **Integração de Aplicações**
   - **Amazon Simple Notification Service (SNS)**: Gerencia notificações e mensagens acionadas por eventos.
   - **Amazon Simple Queue Service (SQS)**: Gerencia filas de mensagens para comunicação desacoplada entre serviços.

### 4. **Armazenamento**
   - **Amazon Simple Storage Service (S3)**: Armazenamento escalável e seguro para dados brutos, processados e logs.

### 5. **Análises**
   - **Amazon Kinesis**: Processamento e análise de streams de dados em tempo real.
   - **AWS Glue**: Serviço de ETL (Extração, Transformação e Carga) para preparar e catalogar dados.
   - **Amazon Athena**: Serviço de consultas SQL para análise direta dos dados armazenados no S3.

## Pipeline do Projeto

O pipeline de engenharia de dados está estruturado da seguinte forma:

### 1. **Ingestão de Dados**:
   - Streams de dados em tempo real são ingeridos usando o **Amazon Kinesis**.
   - Arquivos de dados (ex.: CSV, JSON) são carregados no **Amazon S3**.

### 2. **Processamento e Transformação de Dados**:
   - Funções **AWS Lambda** são acionadas para transformações leves e tarefas acionadas por eventos.
   - **AWS Glue** lida com tarefas complexas de ETL, transformando os dados e armazenando os dados processados no S3.

### 3. **Armazenamento de Dados**:
   - Dados brutos são armazenados no **Amazon S3** para armazenamento a longo prazo.
   - Dados processados e transformados também são armazenados no S3, organizados em diferentes camadas (bronze, prata, ouro).

### 4. **Análise e Consulta de Dados**:
   - **Amazon Athena** é usado para realizar consultas SQL diretamente nos dados do S3.
   - Dados processados ficam disponíveis para ferramentas de business intelligence (BI) e relatórios.

### 5. **Monitoramento e Notificações**:
   - **Amazon SNS** envia notificações com base em eventos ou falhas no pipeline.
   - **Amazon SQS** gerencia filas de mensagens para processamento distribuído e tratamento de eventos.

## Fluxo do Pipeline

1. **Coleta de Dados**  
   - O Kinesis coleta dados em tempo real ou arquivos são enviados para o S3.

2. **Processamento Inicial**  
   - Lambda ou EC2 processam ou transformam os dados conforme necessário.

3. **ETL com Glue**  
   - Glue executa jobs de ETL e prepara os dados para análise.

4. **Armazenamento Estruturado**  
   - Os dados são organizados em camadas no S3 (Bronze, Prata, Ouro).

5. **Consultas e Análises**  
   - Athena realiza consultas SQL nos dados para geração de insights e relatórios.

6. **Notificações e Monitoramento**  
   - SNS e SQS gerenciam a comunicação e notificações baseadas em eventos.

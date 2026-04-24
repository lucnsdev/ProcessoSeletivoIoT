## 📝 Relatório do Candidato

# ESTAÇÃO METEREOLOGICA ![icon_app](https://github.com/user-attachments/assets/54547d9b-73a4-44f0-9d83-cae41c8efea3)

### 👤 Identificação do Candidato
- **Nome completo:**  LUCAS DO NASCIMENTO SOUZA
- **GitHub:**  https://github.com/lucnsdev/sobre-o-lucas

---

## 1️⃣ Visão Geral da Solução
- O objetivo é demostrar o funcionamento de uma simples estação metereologica com visualização dos dados e controle dos periféricos via App Android, fazendo uso do protocolo MQTT.
- O sistema embarcado simulado faz a leitura dos sensores e controla os periféricos de saída de acordo com os comandos recebidos via app.
- O LED roxo que é controledo por PWM e o valor do mesmo é recebido via MQTT, enviado pelo app.
- O relé que é controlado por comando via app.
- O servo motor também é controlado via app, que envia o valor do angulo e o esp32 aplica por meio de PWM.
- O usuário interage com ele por meio do App Android disponibilizado aqui no Google Drive:
- [App Estção Metereologica - APK, 142Kb](https://drive.google.com/file/d/1J9Z7MekcTMKlXneIEJD-uHdjjl-hFbEw/view?usp=drive_link)
- [Repositório do Código fonte em Java](https://github.com/lucnsdev/App-PNAAT-IoT-Project)
<br>
<img height="480" alt="Captura de tela 2026-04-24 125124" src="https://github.com/user-attachments/assets/86dfe8db-120e-4852-9888-e25d82bcf82d" />

---

## O app de visualização dos dados, controle do relé, servo e led.
- O app é bem simples.
- É feito uso do protocolo MQTT para envio e recebimendo de dados de sensores e controle dos periféricos de saídas.
- Com ele é possivel controlar a intensidade do brilho do led roxo, a Seekbar do app controla o nivel do PWM.
- O angulo de inclinação do eixo do servo motor é controlado pela ArcSeekBar do app. No app se controla o angulo de inclinação.
- O Esp32 recebe os dados no formato JSON e extrai os dados de controle para os periféricos de saída.
<br>
<img width="240" alt="Screenshot_20260424_132946_PNAAT IoT Project" src="https://github.com/user-attachments/assets/903a7e83-9beb-46eb-9c6a-27d928594d0f" />
<img width="240" alt="Screenshot_20260424_132744_PNAAT IoT Project" src="https://github.com/user-attachments/assets/0f7ec971-1ac0-44c2-b2a1-438b9d3b9825" />


---

## 2️⃣ Arquitetura do Sistema Embarcado

Arquitetura lógica do projeto:

- Inicialmente o código executa as inicializações necessárias dos sensores e pinos, definindo quais serão saídas e entradas.
- Depois inicia o controlador Wifi do Esp32 e se conecta a uma rede WiFi virtual (`sta_if.connect`)
- Logo após a conexão com a internet ser estabelecida, o sistema se conecta a um Broker MQTT. E subscreve o topico (`/lucns/estacao_metereologica/android`)
- Após as inicializações o sistema entra no bloco de repetição infinita (`while(True)`).
- Alguns ds componentes interagem entre si por meio das variações da temperatura. O LED RGB varia suas cores de acordo com a temperatura.

---

## 3️⃣ Componentes Utilizados na Simulação

Liste os principais componentes definidos no `diagram.json`, por exemplo:

- Tipo de placa utilizada  
- LEDs, botões, sensores, atuadores, etc.  
- Função de cada componente no sistema  

---

## 4️⃣ Decisões Técnicas Relevantes

Explique brevemente decisões importantes tomadas durante o desenvolvimento, como:

- Organização do código  
- Uso de funções, estados ou constantes  
- Estratégias para temporização ou controle lógico  

---

## 5️⃣ Resultados Obtidos

Descreva o comportamento final do sistema:

- O que funciona corretamente  
- Quais requisitos foram atendidos  
- Resultado observado na simulação do Wokwi  

---

## 6️⃣ Comentários Adicionais (Opcional)

Utilize este espaço para comentar, se desejar:

- Dificuldades encontradas  
- Limitações da solução  
- Melhorias que você faria com mais tempo  
- Principais aprendizados durante o desafio  

---

> ✅ Este relatório faz parte da avaliação técnica.  
> Clareza, objetividade e organização são tão importantes quanto o funcionamento do código.

---

## 🆘 Suporte

Em caso de dúvidas:

- Consulte o material dos cursos EAD
- Leia atentamente este README
- Analise os logs das GitHub Actions
- Utilize os canais oficiais para contato com os instrutores

Boa sorte no processo seletivo.
Mostre sua capacidade de pensar como um engenheiro de sistemas embarcados.
****

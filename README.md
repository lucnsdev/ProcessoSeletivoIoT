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
<br>
<img height="480" alt="Captura de tela 2026-04-24 125124" src="https://github.com/user-attachments/assets/86dfe8db-120e-4852-9888-e25d82bcf82d" />

---

## O app de visualização dos dados, controle do relé, servo motor e led.
- O app é bem simples.
- Foi desenvolvido em Java puro, sem uso de libs e sem frameworks o que torna o app extremamente leve (`142Kb`) apenas e sem dependencias.
- É feito uso do protocolo MQTT para envio e recebimendo de dados de sensores e controle dos periféricos de saídas.
- Com ele é possivel controlar a intensidade do brilho do led roxo, a Seekbar do app controla o nivel do PWM.
- O angulo de inclinação do eixo do servo motor é controlado pela ArcSeekBar do app.
- O Esp32 se conecta a rede virtual WiFi, depois se conecta ao Broker e envia/recebe os dados no formato JSON e extrai os dados de controle para controlar os periféricos de saída.
- O usuário interage com o simulador alterando os valores do sensor de temperatura e humidade, também  é possível interagir através do array de switch's que há no circuito, e claro, por meio do App Android disponibilizado o APK no Google Drive e repositório do Github:
- [App Estção Metereologica - APK, 142Kb](https://drive.google.com/file/d/1J9Z7MekcTMKlXneIEJD-uHdjjl-hFbEw/view?usp=drive_link)
- [Repositório do Código fonte em Java](https://github.com/lucnsdev/App-PNAAT-IoT-Project)
<br>
<img width="240" alt="Screenshot_20260424_132946_PNAAT IoT Project" src="https://github.com/user-attachments/assets/903a7e83-9beb-46eb-9c6a-27d928594d0f" />
<img width="240" alt="Screenshot_20260424_132744_PNAAT IoT Project" src="https://github.com/user-attachments/assets/0f7ec971-1ac0-44c2-b2a1-438b9d3b9825" />


---

## 2️⃣ Arquitetura do Sistema Embarcado

Arquitetura lógica do projeto:

- Inicialmente o código, no enbarcado, executa as inicializações necessárias dos sensores e pinos, definindo quais serão saídas e entradas.
- Depois inicia o controlador Wifi do Esp32 e se conecta a uma rede WiFi virtual (`sta_if.connect`)
- Logo após a conexão com a internet ser estabelecida, o sistema se conecta a um Broker MQTT. E subscreve o topico (`/lucns/estacao_metereologica/android`)
- Após as inicializações o sistema entra no bloco de repetição infinita, uma loop (`while(True)`).
- Alguns dos componentes interagem entre si por meio das variações da temperatura. O LED RGB varia suas cores de acordo com a temperatura.

## 2️⃣.1️⃣ Principais Logicas
- Os dados são enviados ao app se qualquer dado tiver seu valor alterado. Por exemplo, se a temperatura for alterada, ou a humidade, ou o estado de algum switch for mudado, o app receberá as alterações. Praticamente em tempo real.
- **O delay maximo entre uma alteração de valores no circuito simulado e a mostragem dos dados atualizados na tela do smartphone é de no maximo 2 segundos.**
---

## 3️⃣ Componentes Utilizados na Simulação

Os principais componentes definidos no `diagram.json`, são:

- O embarcado escolhido foi o ESP32 pois ele possui radio integrado, possibilitando conexões WiFi.
- Existe um sensor de temperatura e humidade o (`DHT22`).
- O angulo do servo motor define o angulo de posicionamento do sensor de raios UV em relação ao posicionamento do sol. Para posicionar outros sensores de luz.
- Há um array de switch's Eles são conectados a pinos configurados com (`PULL_UP`) o que torna desnecessario o resistor de 10KOhms acoplado para manter o pino em nivel baixo ou alto.
- O LED RGB foi adicionado apenas para haver uma interação local do proprio simulador. Ele varia sua cor de acordo com a temperatura registrada no sensor.
- Foi colocado um LED roxo para controla-lo analogicamente via PWM, simulando algum tipo de alteração que pode ser necéssario em algum ajuste de sensor de uma estação metereologica.
- O relé esta ali apenas para simular o acionamento de um motor 220V que severia para realizar a abertura de uma janela no teto superior da estrutura da estação metereologica. O LED acoplado a ele seria o motor que seria usado para acionar a abertuta de alguma janela ou portão que expõe os sensores a céu aberto.

---

## 4️⃣ Decisões Técnicas Relevantes

Explique brevemente decisões importantes tomadas durante o desenvolvimento, como:

- Organização do código foi feita de forma que ficasse legivel a qualquer pessoa e de facil compreensão.
- AS funções foram criadas para separar cada bloco de execução e facilitar a compreensão de quem for ler.  
- A Estratégia para temporização é bem simples. Como não há a necessidade de leituras constantes de sensores ou de dezenas de envios dos dados por segundo, foi adicionado um (`time.sleep(1)`) para retardar a execução. Tempos menores que 1 segundo pode fazer o servidor MQTT desconectar o cliente.

---

## 5️⃣ Resultados Obtidos

Descreva o comportamento final do sistema:

- Tudo funciona corretamente.
- Todos os requisitos são atendidos.
- Os resultados observados na simulação pode ser visualizado no próprio Wokwi por meio do link abaixo e a interação da interface grafica peo app disponibilizado.
- [WOKWI - Simulador de Estação Metereologica, por @lucns](https://wokwi.com/projects/462025088630933505)

---

## 6️⃣ Comentários Adicionais (Opcional)

- A unica dificuldade foi entender qual o problema do Actions.  
- As limitações se dá por conta dos poucos componentes existentes no WOKWI e também a lentidão nas simulações. Como sujestão deixo o [TinckerCad](https://www.tinkercad.com/circuits).
- Melhorias que você faria com mais tempo  
- Principais aprendizados durante o desafio

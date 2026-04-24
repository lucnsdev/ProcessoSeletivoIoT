## 📝 Relatório do Candidato

# ESTAÇÂO METEREOLOGICA <img width="162" height="162" alt="ic_launcher_foreground" src="https://github.com/user-attachments/assets/5e4836bf-3130-425f-8b70-d95bab10b9fc" />


---

### 👤 Identificação do Candidato

- **Nome completo:**  LUCAS DO NASCIMENTO SOUZA
- **GitHub:**  https://github.com/lucnsdev/sobre-o-lucas

---

## 1️⃣ Visão Geral da Solução


- O objetivo é demostrar o funcionamento de uma simples estação metereologica com visualização dos dados e controle dos periféricos via App Android.
- O sistema embarcado simulado faz a leitura dos sensores e controla os periféricos de saída de acordo com os comandos recebidos via app.
- O LED roxo que é controledo por PWM e o relé que é controlado por comando via App. 
- O usuário interage com ele por meio do App Android disponibilizado aqui no Google Drive:
- [App Estção Metereologica - 142Kb](https://drive.google.com/file/d/1J9Z7MekcTMKlXneIEJD-uHdjjl-hFbEw/view?usp=drive_link)

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

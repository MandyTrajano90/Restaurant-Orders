# Restaurant Orders 🍽️

Este projeto foi desenvolvido para consolidar o aprendizado sobre as estruturas de dados Hashmap, implementado em Python pela classe Dict e a estrutura Conjunto, implementado em Python pela classe Set. Ambas as estruturas possuem implementações muito similares e, em alguns casos, podem ser utilizadas de forma intercambiável e em outros casos, não.

<details>
  <summary><strong>👨‍💻 O que foi desenvolvido:</strong></summary>
    <p>O Restaurante  🍝 🦐 Chapa Quente 🍛 🥘 precisa de uma ferramenta de construção de cardápios. O restaurante necessita desta ferramenta para que possa, de maneira simples, gerar seus cardápios considerando possíveis restrições alimentares e também a disponibilidade dos ingredientes em estoque. Hoje, a gestão das receitas e de estoque do restaurante acontece de forma muito ineficiente através de arquivos csv e, por essa razão, as pessoas fundadoras do estabelecimento desejam melhorar esta gestão.</p>
    <p> Ao longo deste projeto construi testes para classes Ingredient e Dish, implementei uma nova classe para mapear os pratos e suas respectivas receitas (ingredientes e quantidades), também implementei uma classe que gera os cardápios que devem ser mostrados para as pessoas que frequentam o estabelecimento e outra que faz a gestão de estoque dos ingredientes.</p>
</details>

<details>
  <summary><strong>🚵 Habilidades exercitadas:</strong></summary></br>
  - Praticar o conceito de `Hashmaps` através das estruturas de dados `Dict` e `Set` do Python; </br>
  - Praticar os conhecimentos de testes de software; </br>
  - Praticar os conhecimentos de orientação a objetos. </br>

</details>

## Instalando o projeto
<details>
  <summary><strong>📋Passo a passo</strong></summary><br />

  1. Clone o repositório

  - Use o comando: `git clone git@github.com:Mandytrajano90/Restaurant-Orders.git`.
  - Entre na pasta do repositório que você acabou de clonar:
    - `cd Restaurant-Orders`

  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`

  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.<br />
  👀 Caso precise desativar o ambiente virtual, execute o comando "deactivate". <br />
  ⚠️ Lembre-se de ativar novamente o ambiente virtual quando voltar a trabalhar no projeto.
</details>

<details>
  <summary><strong>🛠 Testes</strong></summary><br />

  👀 **Para executar os testes certifique-se de que você está com o ambiente virtual ativado.**

  <strong>Executar os testes</strong>

  ```bash
  $ python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```
</details>

## 👁️ Dê uma olhada no código



https://github.com/user-attachments/assets/bbf98390-c9ac-4b59-b0fa-08fc61105908


<!-- Olá, Tryber!
Esse é apenas um arquivo inicial para o README do seu projeto.
É essencial que você preencha esse documento por conta própria, ok?
Não deixe de usar nossas dicas de escrita de README de projetos, e deixe sua criatividade brilhar!
:warning: IMPORTANTE: você precisa deixar nítido:
- quais arquivos/pastas foram desenvolvidos por você; 
- quais arquivos/pastas foram desenvolvidos por outra pessoa estudante;
- quais arquivos/pastas foram desenvolvidos pela Trybe.
-->

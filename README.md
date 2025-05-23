# Sistema de Gerenciamento de Pet Shop / Clínica Veterinária 🐾

Projeto desenvolvido como parte da disciplina **INE5605 — Desenvolvimento de Sistemas Orientados a Objetos** da **Universidade Federal de Santa Catarina (UFSC)**.

## 🎯 Objetivo

Desenvolver um sistema em Python, utilizando os princípios da programação orientada a objetos, para gerenciar os serviços de um pet shop ou clínica veterinária.

O sistema permite:
- Cadastro e organização de **pets**, **donos**, **serviços oferecidos** e **agendamentos**
- Histórico de serviços realizados
- Cálculo do valor total gasto por dono
- Exportação dos dados (opcional)

## ✅ Funcionalidades

- 📋 **Cadastro completo de pets e donos**
  - Inclusão, remoção e edição
  - Um pet pertence a **um único dono**
  - Um dono pode ter **vários pets**

- 🛠️ **Gerenciamento de serviços**
  - Como banho, tosa, consultas, etc.
  - Cadastro, edição e remoção de serviços

- 🗓️ **Agendamento**
  - Somente donos cadastrados podem agendar
  - Verificação de conflitos de horário
  - Apenas datas futuras são permitidas
  - Cancelamento com registro de data/hora

- 🧾 **Histórico e cálculo**
  - Listagem de serviços realizados por pet
  - Cálculo de valor total gasto por dono

- 📞 **Atualização rápida de dados**
  - Alteração fácil de telefone e endereço dos donos

## 📌 Regras de Negócio

- Pet deve conter: Nome, Espécie, Raça, Idade (número inteiro positivo) e Dono
- Serviços só podem ser agendados se estiverem cadastrados
- Não é permitido agendar dois serviços no mesmo horário para o mesmo pet
- Agendamentos para o passado não são permitidos
- O cancelamento de agendamentos deve ser registrado

## 🔒 Restrições

- Sem integração com banco de dados externo
- Sem autenticação/login
- Sem controle financeiro detalhado
- Foco apenas nos serviços (não há controle de estoque)
- Persistência apenas local (ex: arquivos `.csv`, `.json` ou `.txt`)
- Histórico limitado à sessão (salvo se exportado)

## 🧩 Modelagem OOP

- **Associação**: Agendamento associa Pet, Dono e Serviço
- **Agregação**: Dono contém uma lista de Pets
- **Composição**: Agendamento é composto por Pet e Serviço — se excluído, perde o vínculo

## 🧑‍🏫 Professores Responsáveis

- Douglas Hiura Longo  
- André Brascher

---

Desenvolvido com foco educacional e aplicação dos conceitos fundamentais de orientação a objetos.

UML: https://drive.google.com/file/d/1BwNR0RDe3__Q2UZbS8SxWrNjEoo66J6J/view?usp=drive_link

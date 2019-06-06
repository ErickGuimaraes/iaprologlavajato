ano(2014).
ano(2015).
ano(2016).
ano(2017).
ano(2018).
ano(2019).

mes(janeiro).
mes(fevereiro).
mes(marco).
mes(abril).
mes(maio).
mes(junho).
mes(julho).
mes(agosto).
mes(setembro).
mes(outubro).
mes(novembro).
mes(dezembro).

pais(brasil).
pais(suica).
pais(estados_unidos).
pais(portugal).
pais(holanda).

empresa(petrobras).
empresa(odebrecht).
empresa(oas).
empresa(camargo_correa).
empresa(queiroz_galvao).
empresa(utc_engenharia).
empresa(andrade_gutierrez).
empresa(engevix).
empresa(iesa_oleo_e_gas).
empresa(toyo_setal).
empresa(mendes_junior).
empresa(galvao_engenharia).
empresa(skanska).
empresa(promon_engenharia).

crime(organizacao_criminosa).
crime(crime_contra_sistema_financeiro_nacional).
crime(falsidade_ideologica).
crime(lavagem_dinheiro).

doleiro(alberto_youssef).
diretor_petrobras(paulo_roberto_costa).

procurador(Pessoa) :-
   nome(procurador).

procurador(carlos_fernando_lima).
procurador(felipe_delia_camargo).
procurador(deltan_dallagnol).
procurador(roberson_henrique_pozzobon).

nome(carlos_fernado_lima).
nome(felipe_delia_camargo).
nome(erika_marena).
nome(alberto_yousef).
nome(deltan_dallagnol).
nome(roberson_henrique_pozzobon).
nome(paulo_roberto_costa).


cidade(curitiba).
cidade(brasilia).
cidade(rio_de_janeiro).
cidade(sao_paulo).

delegado(erika_marena).

nomeoperacao(lava_jato).

pessoa(erika_marena).
pessoa(felipe_delia_camargo).
pessoa(carlos_fernando_lima).
pessoa(alberto_yousef).
pessoa(deltan_dallagnol).
pessoa(roberson_henrique_pozzobon).
pessoa(paulo_roberto_costa).


nomeiaOperacao(Pessoa , Nome_Operacao) :-
    delegado(Pessoa),
    nomeoperacao(Nome_Operacao).

inicioOperacao(Nome_Operacao, Ano) :-
   nomeoperacao(Nome_Operacao),
   Ano is 2014.

lavaDinheiro(Pessoa, Crime) :-
    doleiro(Pessoa),
    Crime is lavagem_dinheiro.

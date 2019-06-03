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

procurador(carlos_fernado_lima).
procurador(felipe_delia_camargo).

delegado(erika_marena).

nomeoperacao(lava_jato).

pessoa(erika_marena).

nomeiaOperacao(Pessoa , Nome_Operacao) :-
    delegado(Pessoa),
    nomeoperacao(Nome_Operacao).

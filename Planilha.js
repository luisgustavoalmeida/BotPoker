var executadoNesteIntervalo = false;
var executadoNesteIntervaloTime = false;
const MAX_TENTATIVAS = 3; // Número máximo de tentativas

function test() {
    ordenarPlanilha("T1", "J", false) // coloca a coluna valores do R1 em ordem decrescente
}


function verificarHorario() {
    var horaAtual = new Date();

    //Logger.log(horaAtual);
    //Logger.log(executadoNesteIntervalo);

    // Definir os intervalos de tempo
    var intervalos = [
        {inicio: {horas: 23, minutos: 10}, fim: {horas: 23, minutos: 30}, funcao: ordenarR1},
        {inicio: {horas: 23, minutos: 40}, fim: {horas: 23, minutos: 58}, funcao: ordenarR1Parte2},
        {inicio: {horas: 4, minutos: 43}, fim: {horas: 4, minutos: 58}, funcao: ordenarR2},
        {inicio: {horas: 9, minutos: 43}, fim: {horas: 9, minutos: 58}, funcao: ordenarR3},
        {inicio: {horas: 14, minutos: 43}, fim: {horas: 14, minutos: 58}, funcao: ordenarR4},
        {inicio: {horas: 19, minutos: 43}, fim: {horas: 19, minutos: 58}, funcao: ordenarR5},
        {inicio: {horas: 0, minutos: 5}, fim: {horas: 0, minutos: 15}, funcao: apagarTodaPlanilha}
    ];


    for (var i = 0; i < intervalos.length; i++) {
        var intervalo = intervalos[i];
        var inicioIntervalo = new Date();
        inicioIntervalo.setHours(intervalo.inicio.horas, intervalo.inicio.minutos, 0, 0);
        var fimIntervalo = new Date();
        fimIntervalo.setHours(intervalo.fim.horas, intervalo.fim.minutos, 0, 0);

        if (horaAtual >= inicioIntervalo && horaAtual <= fimIntervalo) {
            Logger.log('hora de executar');
            // Verificar se já foi executado neste intervalo
            if (!executadoNesteIntervalo) {
                Logger.log('Executa R' + (i + 1));
                executadoNesteIntervalo = true;
                intervalo.funcao();
                return;
            }
            Logger.log('ja foi executado');
            return;
        }

    }
    executadoNesteIntervalo = false;
    Logger.log(executadoNesteIntervalo);
    Logger.log('Fora de todos os intervalos');
}


function verificarHorarioOrdenarTime() {
    var horaAtual = new Date();

    //Logger.log(horaAtual);
    //Logger.log(executadoNesteIntervalo);

    // Definir os intervalos de tempo
    var intervalos = [
        {inicio: {horas: 4, minutos: 58}, fim: {horas: 5, minutos: 0}, funcao: ordenarPlanilha("R2", "K", true)},
        {inicio: {horas: 9, minutos: 58}, fim: {horas: 10, minutos: 0}, funcao: ordenarPlanilha("R3", "K", true)},
        {inicio: {horas: 14, minutos: 58}, fim: {horas: 15, minutos: 0}, funcao: ordenarPlanilha("R4", "K", true)},
        {inicio: {horas: 19, minutos: 58}, fim: {horas: 20, minutos: 0}, funcao: ordenarPlanilha("R5", "K", true)}
    ];


    for (var i = 0; i < intervalos.length; i++) {
        var intervalo = intervalos[i];
        var inicioIntervalo = new Date();
        inicioIntervalo.setHours(intervalo.inicio.horas, intervalo.inicio.minutos, 0, 0);
        var fimIntervalo = new Date();
        fimIntervalo.setHours(intervalo.fim.horas, intervalo.fim.minutos, 0, 0);

        if (horaAtual >= inicioIntervalo && horaAtual <= fimIntervalo) {
            Logger.log('hora de executar');
            // Verificar se já foi executado neste intervalo
            if (!executadoNesteIntervaloTime) {
                intervalo.funcao();
                executadoNesteIntervaloTime = true;
                return;
            }
            Logger.log('ja foi executado');
            return;
        }

    }
    executadoNesteIntervaloTime = false;
    Logger.log(executadoNesteIntervaloTime);
    Logger.log('Fora de todos os intervalos');
}


function ordenarT1() {
    let tentativas = 0;
    var dataAtual = new Date();
    var diaSemana = dataAtual.getDay();// 0 = domingo, 1 = segunda-feira, ..., 6 = sábado

    // Loop para tentar a execução até atingir o número máximo de tentativas
    while (tentativas < MAX_TENTATIVAS) {
        try {
            if (diaSemana === 0) {
               // Executar apenas aos domingos
               ordenarPlanilha("T1", "J", false) //valores do R1 em ordem decrescente
            } else {
                // Executar nos outros dias da semana, exceto domingo
               ordenarPlanilha("T1", "L", false); // colocar a pontuação em ordem decrescente
            }

            //ordenarPlanilha("T1", "M", true); // colocar as contas nao upadas na parte superior
            copiarColunaParaColuna("T1", "J", "E"); // copia os valores do R1 para T1
            copiarColunaParaColuna("T1", "K", "G"); // copia o horario do R1 anterior para T1
            testarValoresColunaE()
            pontuacaoTarefas()
            testarValoresColunaG_R1_T1("T1") // marcas as contas que não devem entar
            ordenarPlanilha("T1", "G", true);// Coluna G em ordem crescente para colocar as caídas no final

            // Se chegou até aqui sem lançar erro, encerra o loop
            executadoNesteIntervalo = true;
            break;
        } catch (error) {
            // Registra o erro no console
            Logger.log('Erro ao executar ordenação T1: ' + error.message);
            tentativas++;
            Utilities.sleep(15000); // Aguarda 15 segundos antes de tentar novamente
            executadoNesteIntervalo = false;
        }
    }
}

function ordenarR1() {
    let tentativas = 0;

    // Loop para tentar a execução até atingir o número máximo de tentativas
    while (tentativas < MAX_TENTATIVAS) {
        try {
            // Deve ser apagada as 23:00 antes de começar a fazer o R1
            var dataAtual = new Date();
            var diaSemana = dataAtual.getDay();// 0 = domingo, 1 = segunda-feira, ..., 6 = sábado

            apagarColunaF("R1");
            definirFormatoHora("R1")
            copiarColunaParaColuna("R1", "J", "E"); // copia os valores das fixas
            copiarColunaParaColuna("R1", "K", "G"); // copia o horario do R anterior

            if (diaSemana === 6) {
                // Executar apenas aos sábados ultimo dia do tarefas
                ordenarPlanilha("R1", "E", true);  // ordenar pelo valor de fichas

            } else {
                // Executar nos outros dias da semana, exceto domingo
                ordenarPlanilha("R1", "L", false); // colocar a pontuação em ordem decrescente
            }

            // Se chegou até aqui sem lançar erro, encerra o loop
            executadoNesteIntervalo = true;
            break;
        } catch (error) {
            // Registra o erro no console
            Logger.log('Erro ao executar ordenação R1: ' + error.message);
            tentativas++;
            Utilities.sleep(15000); // Aguarda 15 segundos antes de tentar novamente
            executadoNesteIntervalo = false;
        }
    }
}

function ordenarR1Parte2() {
    let tentativas = 0;

    // Loop para tentar a execução até atingir o número máximo de tentativas
    while (tentativas < MAX_TENTATIVAS) {
        try {
            // Deve ser apagada as 23:00 antes de começar a fazer o R1
            testarValoresColunaG_R1_T1("R1") // marcas as contas que não devem entar

            ordenarPlanilha("R1", "G", true);// Coluna G em ordem crescente para colocar as caídas no final

            // Se chegou até aqui sem lançar erro, encerra o loop
            executadoNesteIntervalo = true;
            break;
        } catch (error) {
            // Registra o erro no console
            Logger.log('Erro ao executar ordenação R1: ' + error.message);
            tentativas++;
            Utilities.sleep(15000); // Aguarda 15 segundos antes de tentar novamente
            executadoNesteIntervalo = false;
        }
    }
}

function ordenarR2() {
    let tentativas = 0;

    // Loop para tentar a execução até atingir o número máximo de tentativas
    while (tentativas < MAX_TENTATIVAS) {
        try {

            ordenarPlanilha("R2", "K", true);  // horario do R anteior
            copiarColunaParaColuna("R2", "J", "E"); // copia os valores das fixas
            copiarColunaParaColuna("R2", "K", "G"); // copia o horario do R anterior
            testarValoresColunaG("R2"); // marcas as contas que não devem entar

            // Se chegou até aqui sem lançar erro, encerra o loop
            executadoNesteIntervalo = true;
            break;
        } catch (error) {
            // Registra o erro no console
            Logger.log('Erro ao executar ordenação R2: ' + error.message);
            tentativas++;
            Utilities.sleep(15000); // Aguarda 15 segundos antes de tentar novamente
            executadoNesteIntervalo = false;
        }
    }
}

function ordenarR3() {
    let tentativas = 0;

    // Loop para tentar a execução até atingir o número máximo de tentativas
    while (tentativas < MAX_TENTATIVAS) {
        try {
            // Ordena a planilha "R3" por fichas de forma decrescente e por horas de forma crescente

            ordenarPlanilha("R3", "K", true);  // horario do R anteior

            copiarColunaParaColuna("R3", "J", "E"); // copia os valores das fixas
            copiarColunaParaColuna("R3", "K", "G"); // copia o horario do R anterior
            testarValoresColunaG("R3"); // marcas as contas que não devem entar

            // Se chegou até aqui sem lançar erro, encerra o loop
            executadoNesteIntervalo = true;
            break;
        } catch (error) {
            // Registra o erro no console
            Logger.log('Erro ao executar ordenação R3: ' + error.message);
            tentativas++;
            Utilities.sleep(15000); // Aguarda 15 segundos antes de tentar novamente
            executadoNesteIntervalo = false;
        }
    }
}

function ordenarR4() {
    let tentativas = 0;

    // Loop para tentar a execução até atingir o número máximo de tentativas
    while (tentativas < MAX_TENTATIVAS) {
        try {
            // Ordena a planilha "R4" por fichas de forma decrescente e por horas de forma crescente

            ordenarPlanilha("R4", "K", true);  // horario do R anteior

            copiarColunaParaColuna("R4", "J", "E"); // copia os valores das fixas
            copiarColunaParaColuna("R4", "K", "G"); // copia o horario do R anterior
            testarValoresColunaG("R4"); // marcas as contas que não devem entar

            // Se chegou até aqui sem lançar erro, encerra o loop
            executadoNesteIntervalo = true;
            break;
        } catch (error) {
            // Registra o erro no console
            Logger.log('Erro ao executar ordenação R4: ' + error.message);
            tentativas++;
            Utilities.sleep(15000); // Aguarda 15 segundos antes de tentar novamente
            executadoNesteIntervalo = false;
        }
    }
}

function ordenarR5() {
    let tentativas = 0;

    // Loop para tentar a execução até atingir o número máximo de tentativas
    while (tentativas < MAX_TENTATIVAS) {
        try {
            // Ordena a planilha "R5" por fichas de forma decrescente e por horas de forma crescente
            ordenarPlanilha("R5", "K", true);  // horario do R anteior

            copiarColunaParaColuna("R5", "J", "E"); // copia os valores das fixas
            copiarColunaParaColuna("R5", "K", "G"); // copia o horario do R anterior
            testarValoresColunaG("R5"); // marcas as contas que não devem entar

            // Se chegou até aqui sem lançar erro, encerra o loop
            executadoNesteIntervalo = true;
            break;
        } catch (error) {
            // Registra o erro no console
            Logger.log('Erro ao executar ordenação R5: ' + error.message);
            tentativas++;
            Utilities.sleep(15000); // Aguarda 15 segundos antes de tentar novamente
            executadoNesteIntervalo = false;
        }
    }
}


function apagarTodaPlanilha() {
    let tentativas = 0;

    // Lista de guias a serem processadas
    const guias = ["R2", "R3", "R4", "R5", "T1"];

    // Loop para tentar realizar a operação até atingir o número máximo de tentativas
    while (tentativas < MAX_TENTATIVAS) {
        try {
            // Loop para processar cada guia
            guias.forEach(function (nomeGuia) {
                apagarColunaF(nomeGuia);
                definirFormatoHora(nomeGuia)
            });

            // Se chegou até aqui sem erros, sai do loop
            break;
        } catch (error) {
            Logger.log('Erro ao executar apagarTodaPlanilha: ' + error.message);
            tentativas++;
            Utilities.sleep(15000); // Espera 15 segundos antes de tentar novamente
        }
    }

    // Mensagem de log caso as tentativas se esgotem
    if (tentativas === MAX_TENTATIVAS) {
        Logger.log('Não foi possível executar apagarTodaPlanilha após ' + MAX_TENTATIVAS + ' tentativas.');
    }
}

function definirFormatoHora(nomeGuia) {
    let tentativas = 0;

    while (tentativas < MAX_TENTATIVAS) {
        try {
            var planilha = SpreadsheetApp.getActiveSpreadsheet();
            var guia = planilha.getSheetByName(nomeGuia);

            if (!guia) {
                throw new Error('A guia especificada não existe.');
            }

            var colunaG = guia.getRange("G:G");
            var colunaK = guia.getRange("K:K");

            // Definir formato de hora nas colunas G e K
            colunaG.setNumberFormat("HH:mm:ss");
            colunaK.setNumberFormat("HH:mm:ss");

            Logger.log('Formato de hora definido nas colunas G e K com sucesso.');

            break; // Sair do loop se não houver erros

        } catch (error) {
            Logger.log('Erro ao executar definirFormatoHora: ' + error.message);
            tentativas++;
            Utilities.sleep(15000); // Espera 15 segundos antes de tentar novamente
        }
    }
}


function ordenarPlanilha(nomeGuia, coluna, ordemCrescente) {
    let tentativas = 0;
    let ordenadoComSucesso = false;

    // Loop para tentar ordenar a planilha até atingir o número máximo de tentativas ou até ser bem-sucedido
    while (tentativas < MAX_TENTATIVAS && !ordenadoComSucesso) {
        try {
            // Obter a planilha ativa
            var planilha = SpreadsheetApp.getActiveSpreadsheet();

            // Obter a guia pelo nome
            var guia = planilha.getSheetByName(nomeGuia);

            // Verificar se a guia existe
            if (!guia) {
                throw new Error("Guia não encontrada.");
            }

            // Definir a primeira linha onde os dados começam
            var primeiraLinha = 2;

            // Obter a última linha preenchida na guia
            var ultimaLinha = guia.getLastRow();

            // Verificar se há dados para ordenar
            if (ultimaLinha < primeiraLinha) {
                throw new Error("Não há dados para ordenar.");
            }

            // Definir o intervalo com base na primeira e última linha
            var intervalo = guia.getRange("A" + primeiraLinha + ":M" + ultimaLinha);

            var colunaIndice = getColumnIndex(coluna);

            // Ordernar a planilha com base na coluna especificada em ordem crescente ou decrescente
            intervalo.sort({column: colunaIndice, ascending: ordemCrescente});

            // Marcar como bem-sucedido para sair do loop
            ordenadoComSucesso = true;
        } catch (error) {
            // Logar o erro e incrementar o número de tentativas
            Logger.log(`Erro ao ordenar planilha: ${error.message}`);
            tentativas++;

            // Aguardar 15 segundos antes de tentar novamente
            Utilities.sleep(15000);
        }
    }

    // Mensagem se não for possível ordenar após o número máximo de tentativas
    if (!ordenadoComSucesso) {
        Logger.log(`Não foi possível ordenar após ${MAX_TENTATIVAS} tentativas.`);
    }
}

function copiarValoresColuna(nomeGuia) {
    let tentativas = 0;
    let copiaConcluida = false;

    while (tentativas < MAX_TENTATIVAS && !copiaConcluida) {
        try {
            // Obter a planilha ativa
            var planilha = SpreadsheetApp.getActiveSpreadsheet();

            // Obter a guia pelo nome
            var guia = planilha.getSheetByName(nomeGuia);

            // Verificar se a guia existe
            if (!guia) {
                throw new Error("Guia não encontrada.");
            }

            // Obter os dados da coluna "J" valor das fichas
            var valoresOrigemJ = guia.getRange("J2:J" + guia.getLastRow()).getValues();
            // Obter os dados da coluna "K" para a guia "T1"
            var valoresOrigemL = (nomeGuia === "T1") ? guia.getRange("L2:L" + guia.getLastRow()).getValues() : null;

            // Verificar se há dados para copiar
            if (valoresOrigemJ.length === 0) {
                throw new Error("Não há dados para copiar.");
            }

            // Mapear os valores da coluna "I" para a coluna "E"
            guia.getRange("E2:E" + (valoresOrigemJ.length + 1)).setValues(valoresOrigemJ);

            if (valoresOrigemL) {
                // Verificar se há dados para a coluna "K"
                if (valoresOrigemL.length === 0) {
                    throw new Error("Não há dados para copiar na coluna 'L'.");
                }

                // Mapear os valores da coluna "L" para a coluna "F" para a guia "T1" Pontos
                guia.getRange("F2:F" + (valoresOrigemL.length + 1)).setValues(valoresOrigemL);
            }

            // Forçar a atualização imediata da planilha
            SpreadsheetApp.flush();

            // Indicar que a cópia foi concluída com sucesso
            copiaConcluida = true;

            Logger.log("Cópia concluída com sucesso.");
        } catch (error) {
            // Logar o erro
            Logger.log(`Erro ao copiar valores da coluna: ${error.message}`);

            // Incrementar o número de tentativas
            tentativas++;

            // Aguardar 15 segundos antes de tentar novamente
            Utilities.sleep(15000);
        }
    }

    if (!copiaConcluida) {
        Logger.log(`Não foi possível concluir a cópia após ${MAX_TENTATIVAS} tentativas.`);
    }
}

function copiarColunaParaColuna(nomeGuia, colunaOrigem, colunaDestino) {
    let tentativas = 0;
    let copiaConcluida = false;

    while (tentativas < MAX_TENTATIVAS && !copiaConcluida) {
        try {
            var planilha = SpreadsheetApp.getActiveSpreadsheet();
            var guia = planilha.getSheetByName(nomeGuia);

            if (!guia) {
                throw new Error('A guia especificada não existe.');
            }

            var primeiraLinha = 2;
            var ultimaLinha = guia.getLastRow();
            var colunaOrigemRange = guia.getRange(primeiraLinha, getColumnIndex(colunaOrigem), ultimaLinha - primeiraLinha + 1, 1);
            var colunaDestinoRange = guia.getRange(primeiraLinha, getColumnIndex(colunaDestino), ultimaLinha - primeiraLinha + 1, 1);

            var valoresOrigem = colunaOrigemRange.getValues();

            colunaDestinoRange.setValues(valoresOrigem);

            copiaConcluida = true; // Definir como true se a cópia foi bem-sucedida

            Logger.log('Valores da coluna ' + colunaOrigem + ' copiados para a coluna ' + colunaDestino + ' com sucesso.');

        } catch (error) {
            Logger.log('Erro ao executar copiarColunaParaColuna: ' + error.message);
            tentativas++;
            Utilities.sleep(15000); // Espera 15 segundos antes de tentar novamente
        }
    }
}

// Função auxiliar para obter o índice da coluna a partir do nome
function getColumnIndex(coluna) {
    return coluna.toUpperCase().charCodeAt(0) - 'A'.charCodeAt(0) + 1;
}


function copiarValoresColunaPontos(nomeGuia) {
    let tentativas = 0;
    let copiaConcluida = false;

    while (tentativas < MAX_TENTATIVAS && !copiaConcluida) {
        try {
            // Obtém a planilha ativa
            var planilha = SpreadsheetApp.getActiveSpreadsheet();
            // Obtém a guia pelo nome fornecido
            var guia = planilha.getSheetByName(nomeGuia);

            // Verifica se a guia existe
            if (!guia) {
                throw new Error('Guia não encontrada.');
            }

            // Obtém os dados da coluna "L" a partir da segunda linha
            var ultimaLinha = guia.getLastRow();
            if (ultimaLinha < 2) {
                throw new Error('Não há dados para copiar.');
            }

            var valoresOrigem = guia.getRange(2, 12, ultimaLinha - 1, 1).getValues();

            // Obtém o intervalo da coluna "F" correspondente
            var intervaloDestino = guia.getRange(2, 6, ultimaLinha - 1, 1);

            // Copia os valores para o intervalo de destino
            intervaloDestino.setValues(valoresOrigem);

            // Se chegou até aqui sem lançar erro, marca a cópia como concluída
            copiaConcluida = true;
        } catch (error) {
            // Registra o erro no console
            Logger.log('Erro ao copiar valores da coluna "K" para "F": ' + error.message);
            tentativas++;
            Utilities.sleep(15000); // Aguarda 15 segundos antes de tentar novamente
        }
    }
}

function apagarColunaF(nomeGuia) {
    let tentativas = 0;
    let exclusaoConcluida = false; // Flag para indicar se a exclusão foi concluída

    // Loop para tentar a exclusão até atingir o número máximo de tentativas ou concluir com sucesso
    while (tentativas < MAX_TENTATIVAS && !exclusaoConcluida) {
        try {
            var dataAtual = new Date();
            var diaSemana = dataAtual.getDay(); // 0 = domingo, 1 = segunda-feira, ..., 6 = sábado

            // Obtém a planilha ativa
            var planilha = SpreadsheetApp.getActiveSpreadsheet();
            // Obtém a guia pelo nome fornecido
            var guia = planilha.getSheetByName(nomeGuia);

            // Verifica se a guia existe
            if (!guia) {
                throw new Error('Guia não encontrada.');
            }

            var primeiraLinha = 2; // Primeira linha a partir da qual a coluna será apagada
            var ultimaLinha = guia.getLastRow(); // Última linha preenchida na guia

            if (nomeGuia === "R1") {
                if (diaSemana === 6) {
                    // apaga a colua F apenas no sabado antes das 0h
                    var colunaPontuacao = 6; // Número da coluna F pontuação das contas
                    var intervaloPontuacao = guia.getRange(primeiraLinha, colunaPontuacao, ultimaLinha - primeiraLinha + 1);
                    intervaloPontuacao.clearContent();
                }
                // Define as colunas a serem apagadas
                var colunasParaApagar = [4, 8]; // Números das colunas D e H
                // Apaga as colunas especificadas
                colunasParaApagar.forEach(function (coluna) {
                    var intervaloParaApagar = guia.getRange(primeiraLinha, coluna, ultimaLinha - primeiraLinha + 1);
                    intervaloParaApagar.clearContent();
                });
            }

            if (nomeGuia === "T1") {
                if (diaSemana === 0) {
                    // apaga a colua F apnas no domingo
                    var colunaPontuacao = 6; // Número da coluna F pontuação das contas
                    var intervaloPontuacao = guia.getRange(primeiraLinha, colunaPontuacao, ultimaLinha - primeiraLinha + 1);
                    intervaloPontuacao.clearContent();
                }
                // Define as colunas a serem apagadas
                var colunasParaApagar = [4, 8]; // Números das colunas D e H
                // Apaga as colunas especificadas
                colunasParaApagar.forEach(function (coluna) {
                    var intervaloParaApagar = guia.getRange(primeiraLinha, coluna, ultimaLinha - primeiraLinha + 1);
                    intervaloParaApagar.clearContent();
                });
            }

            if (nomeGuia !== "R1" && nomeGuia !== "T1") {
                // Define as colunas a serem apagadas
                var colunasParaApagar = [4, 6, 8]; // Números das colunas D, F e H
                // Apaga as colunas especificadas
                colunasParaApagar.forEach(function (coluna) {
                    var intervaloParaApagar = guia.getRange(primeiraLinha, coluna, ultimaLinha - primeiraLinha + 1);
                    intervaloParaApagar.clearContent();
                });
            }


            // Se chegou até aqui sem lançar erro, marca a exclusão como concluída
            exclusaoConcluida = true;
        } catch (error) {
            // Registra o erro no console
            Logger.log('Erro ao apagar colunas: ' + error.message);
            tentativas++;
            Utilities.sleep(15000); // Aguarda 15 segundos antes de tentar novamente
        }
    }
}

function escreverZeroNaColunaG(nomeGuia) {
    let tentativas = 0;

    // Loop para tentar realizar a operação até atingir o número máximo de tentativas
    while (tentativas < MAX_TENTATIVAS) {
        try {
            // Obter a planilha ativa e a guia pelo nome especificado
            var planilha = SpreadsheetApp.getActiveSpreadsheet();
            var guia = planilha.getSheetByName(nomeGuia);

            // Verifica se a guia existe
            if (guia == null) {
                throw new Error('A guia especificada não existe.');
            }

            // Obtém os dados da coluna B a partir da segunda linha
            var dadoscolunaB = guia.getRange("B2:B" + guia.getLastRow()).getValues();

            // Array para armazenar os valores da coluna G
            var valoresColunaG = [];

            // Percorre os dados da coluna B e adiciona os valores à coluna G
            dadoscolunaB.forEach(function (row) {
                var valorCelulaB = row[0];

                // Verifica se a célula da coluna B está vazia
                if (valorCelulaB !== "") {
                    // Adiciona "00:00:00" aos valores da coluna G para cada célula não vazia
                    valoresColunaG.push(["00:00:00"]);
                }
            });

            // Verifica se há valores a serem escritos na coluna G
            if (valoresColunaG.length > 0) {
                var primeiraCelulaG = "G2";
                var ultimaCelulaG = "G" + (valoresColunaG.length + 1);
                var intervaloColunaG = guia.getRange(primeiraCelulaG + ":" + ultimaCelulaG);

                // Escreve os valores na coluna G
                intervaloColunaG.setValues(valoresColunaG);
            }

            // Se chegou até aqui sem erros, sai do loop
            break;
        } catch (error) {
            Logger.log('Erro ao executar escreverZeroNaColunaG: ' + error.message);
            tentativas++;
            Utilities.sleep(15000); // Espera 15 segundos antes de tentar novamente
        }
    }

    // Mensagem de log caso as tentativas se esgotem
    if (tentativas === MAX_TENTATIVAS) {
        Logger.log('Não foi possível executar escreverZeroNaColunaG após ' + MAX_TENTATIVAS + ' tentativas.');
    }
}


function testarValoresColunaG(nomeGuia) {
    let tentativas = 0;

    while (tentativas < MAX_TENTATIVAS) {
        try {
            const planilha = SpreadsheetApp.getActiveSpreadsheet();
            const guia = planilha.getSheetByName(nomeGuia);

            if (!guia) {
                throw new Error('A guia especificada não existe.');
            }

            const primeiraLinha = 2;
            const ultimaLinha = guia.getLastRow();
            const colunaG = guia.getRange(primeiraLinha, 7, ultimaLinha - primeiraLinha + 1, 1);
            const colunaD = guia.getRange(primeiraLinha, 4, ultimaLinha - primeiraLinha + 1, 1);

            const valoresG = colunaG.getValues();

            // Percorrer os valores e testar a coluna G
            for (var i = 0; i < valoresG.length; i++) {
                var valorG = valoresG[i][0];

                if (isNaN(valorG)) {
                    // Se não for um número, colocar "x" na coluna D na linha correspondente
                    colunaD.getCell(i + 1, 1).setValue("x");
                }
                // Se estiver vazio, não mudar nada
            }

            Logger.log('Teste de valores da coluna G concluído com sucesso.');
            break; // Sair do loop se não houver erros

        } catch (error) {
            Logger.log('Erro ao executar testarValoresColunaG: ' + error.message);
            tentativas++;
            Utilities.sleep(15000); // Espera 15 segundos antes de tentar novamente
        }
    }
}

function testarValoresColunaG_R1_T1(nomeGuia) {
    let tentativas = 0;

    while (tentativas < MAX_TENTATIVAS) {
        try {
            const planilha = SpreadsheetApp.getActiveSpreadsheet();
            const guia = planilha.getSheetByName(nomeGuia);

            if (!guia) {
                throw new Error('A guia especificada não existe.');
            }

            const primeiraLinha = 2;
            const ultimaLinha = guia.getLastRow();
            const colunaG = guia.getRange(primeiraLinha, 7, ultimaLinha - primeiraLinha + 1, 1);
            const colunaD = guia.getRange(primeiraLinha, 4, ultimaLinha - primeiraLinha + 1, 1);

            const valoresG = colunaG.getValues();

            // Percorrer os valores e testar a coluna G
            for (var i = 0; i < valoresG.length; i++) {
                var valorG = valoresG[i][0];
                // Verificar se o valor não é um número e não está vazio
                if (valorG !== '' && !isNaN(valorG)) {
                    // Se for número e diferente de vazio, escrever "00:00:00" na coluna G
                    colunaG.getCell(i + 1, 1).setValue("00:00:00");
                } else if (isNaN(valorG)) {
                    // Se não for um número, colocar "x" na coluna D na linha correspondente
                    colunaD.getCell(i + 1, 1).setValue("x");
                }
            }

            Logger.log('Teste de valores da coluna G concluído com sucesso.');
            break; // Sair do loop se não houver erros

        } catch (error) {
            Logger.log('Erro ao executar testarValoresColunaG: ' + error.message);
            tentativas++;
            Utilities.sleep(15000); // Espera 15 segundos antes de tentar novamente
        }
    }
}


function macaraCaidas(nomeGuia) {
    let tentativas = 0;

    // Loop para tentar realizar a operação até atingir o número máximo de tentativas
    while (tentativas < MAX_TENTATIVAS) {
        try {
            // Obter a planilha ativa e a guia pelo nome especificado
            var planilha = SpreadsheetApp.getActiveSpreadsheet();
            var guia = planilha.getSheetByName(nomeGuia);

            // Verifica se a guia existe
            if (guia == null) {
                throw new Error('A guia especificada não existe.');
            }

            var primeiraLinha = 2; // Primeira linha da coluna J
            var ultimaLinha = guia.getLastRow(); // Última linha preenchida na guia

            // Obter intervalo das colunas K, G e D
            var colunaK = guia.getRange(primeiraLinha, 11, ultimaLinha - primeiraLinha + 1, 1);
            var colunaG = guia.getRange(primeiraLinha, 7, ultimaLinha - primeiraLinha + 1, 1);
            var colunaD = guia.getRange(primeiraLinha, 4, ultimaLinha - primeiraLinha + 1, 1);

            // Obter os valores das colunas J, G e D em uma única operação
            var valores = colunaK.getValues();

            // Percorrer os valores e aplicar as modificações diretamente no intervalo correspondente
            for (var i = 0; i < valores.length; i++) {
                var valor = valores[i][0];

                // Verificar se o valor não é um número
                if (isNaN(valor)) {
                    // Colar o valor na coluna G na linha correspondente
                    colunaG.getCell(i + 1, 1).setValue(valor);

                    // Marcar a coluna D com um "x" na linha correspondente
                    colunaD.getCell(i + 1, 1).setValue("x");
                }
            }

            // Se chegou até aqui sem erros, sai do loop
            break;
        } catch (error) {
            Logger.log('Erro ao executar macaraCaidas: ' + error.message);
            tentativas++;
            Utilities.sleep(15000); // Espera 15 segundos antes de tentar novamente
        }
    }

    // Mensagem de log caso as tentativas se esgotem
    if (tentativas === MAX_TENTATIVAS) {
        Logger.log('Não foi possível executar macaraCaidas após ' + MAX_TENTATIVAS + ' tentativas.');
    }
}

function maracaCaidas2(nomeGuia) {
    let tentativas = 0;

    // Loop para tentar realizar a operação até atingir o número máximo de tentativas
    while (tentativas < MAX_TENTATIVAS) {
        try {
            // Obter a planilha ativa e a guia pelo nome especificado
            var planilha = SpreadsheetApp.getActiveSpreadsheet();
            var guia = planilha.getSheetByName(nomeGuia);

            // Verifica se a guia existe
            if (guia == null) {
                throw new Error('A guia especificada não existe.');
            }

            var primeiraLinha = 2; // Primeira linha da coluna J
            var ultimaLinha = guia.getLastRow(); // Última linha preenchida na guia

            // Obter intervalo das colunas K, G e D
            var colunaK = guia.getRange(primeiraLinha, 11, ultimaLinha - primeiraLinha + 1, 1);
            var colunaG = guia.getRange(primeiraLinha, 7, ultimaLinha - primeiraLinha + 1, 1);
            var colunaD = guia.getRange(primeiraLinha, 4, ultimaLinha - primeiraLinha + 1, 1);

            // Obter os valores da coluna K em uma única operação
            var valoresK = colunaK.getValues();

            // Percorrer os valores e copiar para a coluna G, e marcar a coluna D conforme necessário
            for (var i = 0; i < valoresK.length; i++) {
                var valorK = valoresK[i][0];

                // Colar o valor na coluna G na linha correspondente
                colunaG.getCell(i + 1, 1).setValue(valorK);

                // Verificar se o valor não é um número
                if (isNaN(valorK)) {
                    // Se não for um número, colocar "x" na coluna D na linha correspondente
                    colunaD.getCell(i + 1, 1).setValue("x");
                } else {
                    // Se for um número, limpar a coluna D na linha correspondente
                    colunaD.getCell(i + 1, 1).setValue("");
                }
            }

            // Se chegou até aqui sem erros, sai do loop
            break;
        } catch (error) {
            Logger.log('Erro ao executar macaraCaidas: ' + error.message);
            tentativas++;
            Utilities.sleep(15000); // Espera 15 segundos antes de tentar novamente
        }
    }
}


function testarValoresColunaE() {

    for (let tentativas = 0; tentativas < MAX_TENTATIVAS; tentativas++) {
        try {
            const planilha = SpreadsheetApp.getActiveSpreadsheet();
            const guiaT1 = planilha.getSheetByName('T1');

            if (!guiaT1) {
                throw new Error('Guia T1 não encontrada.');
            }

            const rangeE = guiaT1.getRange('E:E');
            //const rangeD = guiaT1.getRange('D:D');
            const dadosT1 = rangeE.getValues();
            const valoresE = rangeE.getValues().flat();
            //const valoresD = rangeD.getValues().flat();

            for (let i = 1; i < dadosT1.length; i++) {
                const valorE = valoresE[i];
                //const valorD = valoresD[i];

                if (typeof valorE === 'number' && valorE < 40000) {
                    guiaT1.getRange('D' + (i + 1)).setValue('v');
                }
                // Se não for número ou não for menor que 40000, mantém o valor existente em D.
            }

            break;

        } catch (error) {
            console.error(`Erro na tentativa ${tentativas + 1}: ${error}`);
            Utilities.sleep(15000);
        }
    }
}


function poucaFicha() {
    var planilha = SpreadsheetApp.getActiveSpreadsheet();
    var guia = planilha.getSheetByName("T1");

    var ultimaLinha = guia.getRange("B2:B").getLastRow();
    var valoresColunaJ = guia.getRange("J2:J" + ultimaLinha).getValues();
    var valoresColunaD = guia.getRange("D2:D" + ultimaLinha).getValues();

    var valoresParaAtualizar = [];

    for (var i = 0; i < valoresColunaJ.length; i++) {
        var valorI = valoresColunaJ[i][0];
        var valorD = valoresColunaD[i][0];

        if (valorI < 1000 && valorI !== "" && valorD !== "v") {
            valoresParaAtualizar.push(["v"]);
        } else {
            valoresParaAtualizar.push([valorD]);
        }
    }

    // Atualizar os valores na coluna D em um único passo
    guia.getRange("D2:D" + (ultimaLinha + 1)).setValues(valoresParaAtualizar);
}


function pontuacaoTarefas() {
    let tentativas = 0;

    // Loop para tentar realizar a operação até atingir o número máximo de tentativas
    while (tentativas < MAX_TENTATIVAS) {
        try {
            // Obter a planilha ativa e a guia pelo nome "T1"
            var guia = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("T1");

            // Verifica se a guia existe
            if (!guia) {
                throw new Error('A guia "T1" não existe.');
            }

            var colunaL = 12; // Coluna L
            var colunaD = 4;  // Coluna D

            var pontuacaoMinima = 140 + (new Date().getDay() * 10); // Aumenta 10 pontos a cada dia da semana

            var valoresColunaL = guia.getRange(1, colunaL, guia.getLastRow(), 1).getValues();
            var valoresColunaD = guia.getRange(1, colunaD, guia.getLastRow(), 1).getValues();
            var valoresColunaDNovos = [];

            for (var linha = 0; linha < valoresColunaL.length; linha++) {
                var valorCelulaL = valoresColunaL[linha][0];
                var valorCelulaD = valoresColunaD[linha][0];
                var status = (valorCelulaL >= pontuacaoMinima) ? "ok" : valorCelulaD;
                valoresColunaDNovos.push([status]);
            }

            // Define os novos valores da coluna D em massa
            guia.getRange(1, colunaD, valoresColunaDNovos.length, 1).setValues(valoresColunaDNovos);

            // Se chegou até aqui sem erros, sai do loop
            break;
        } catch (error) {
            Logger.log('Erro ao executar pontuacaoTarefas: ' + error.message);
            tentativas++;
            Utilities.sleep(15000); // Espera 15 segundos antes de tentar novamente
        }
    }

    // Mensagem de log caso as tentativas se esgotem
    if (tentativas === MAX_TENTATIVAS) {
        Logger.log('Não foi possível executar pontuacaoTarefas após ' + MAX_TENTATIVAS + ' tentativas.');
    }
}

function agendarExecucaoR1R2R3R4R5() {
    let tentativas = 0;
    let agendadoComSucesso = false;

    var horarios = [
        {hora: 23, minuto: 50, funcao: "ordenarR1"},
        {hora: 4, minuto: 50, funcao: "ordenarR2"},
        {hora: 9, minuto: 50, funcao: "ordenarR3"},
        {hora: 14, minuto: 50, funcao: "ordenarR4"},
        {hora: 19, minuto: 50, funcao: "ordenarR5"}
    ];

    while (tentativas < MAX_TENTATIVAS && !agendadoComSucesso) {
        for (var i = 0; i < horarios.length; i++) {
            var dataAtual = new Date();
            var horario = horarios[i];
            var dataAgendada = new Date(
                dataAtual.getFullYear(),
                dataAtual.getMonth(),
                dataAtual.getDate(),
                horario.hora,
                horario.minuto,
                0
            );

            // Calcula o tempo até o próximo horário
            var tempoAteHorario = dataAgendada - dataAtual;

            try {
                // Cria o gatilho para o evento atual
                ScriptApp.newTrigger(horario.funcao)
                    .timeBased()
                    .after(tempoAteHorario)
                    .create();

                agendadoComSucesso = true;
            } catch (error) {
                Logger.log(`Erro ao agendar execução para ${horario.funcao}: ${error.message}`);
                tentativas++;
                agendadoComSucesso = false;
                Utilities.sleep(60000);
                i--; // Reduz o índice para tentar novamente o mesmo evento na próxima iteração
            }
        }
    }

    if (!agendadoComSucesso) {
        Logger.log(`Não foi possível agendar a execução após ${MAX_TENTATIVAS} tentativas.`);
    }
}

const HORARIOS_EXECUCAO = [
    {hora: 23, minuto: 45},  // R1
    {hora: 4, minuto: 45},   // R2
    {hora: 9, minuto: 45},   // R3
    {hora: 14, minuto: 45},  // R4
    {hora: 19, minuto: 45}   // R5
];

function agendarExecucaoR1() {
    agendarExecucao(0);
}

function agendarExecucaoR2() {
    agendarExecucao(1);
}

function agendarExecucaoR3() {
    agendarExecucao(2);
}

function agendarExecucaoR4() {
    agendarExecucao(3);
}

function agendarExecucaoR5() {
    agendarExecucao(4);
}

function agendarExecucao(index) {
    let tentativas = 0;
    let agendadoComSucesso = false;

    while (tentativas < MAX_TENTATIVAS && !agendadoComSucesso) {
        try {
            const dataAtual = new Date();
            const {hora, minuto} = HORARIOS_EXECUCAO[index];
            const dataAgendada = new Date(
                dataAtual.getFullYear(),
                dataAtual.getMonth(),
                dataAtual.getDate(),
                hora,
                minuto,
                0
            );

            let diferenca = dataAgendada.getTime() - dataAtual.getTime();
            if (diferenca < 0) {
                // Se o horário agendado já passou hoje, agendar para o mesmo horário no dia seguinte
                diferenca += 24 * 60 * 60 * 1000; // Adiciona 24 horas em milissegundos
            }

            ScriptApp.newTrigger(`ordenarR${index + 1}`)
                .timeBased()
                .after(diferenca)
                .create();

            agendadoComSucesso = true;
        } catch (error) {
            Logger.log(`Erro ao agendar execução: ${error.message}`);
            tentativas++;
            Utilities.sleep(60000); // Espera 1 minuto antes de tentar novamente
        }
    }

    if (!agendadoComSucesso) {
        Logger.log(`Não foi possível agendar a execução após ${MAX_TENTATIVAS} tentativas.`);
    }
}


function verificarPcParado() {
    // Obtém a planilha ativa e a guia chamada "IP"
    var planilha = SpreadsheetApp.getActiveSpreadsheet();
    var guia = planilha.getSheetByName("IP");

    // Defina as células da coluna C que você deseja verificar
    var primeiraCelula = 1;
    var ultimaCelula = 51;
    var celulasIndividuais = [];
    var celulasIguais = [];
    var celulasDiferentes = [];

    // Itera sobre as células da coluna C para encontrar as que têm status "Ativado" na coluna D
    for (var i = primeiraCelula; i <= ultimaCelula; i++) {
        var statusAtivado = guia.getRange("D" + i).getValue();

        // Verifica se o status está marcado como "Ativado"
        if (statusAtivado === "Ativado") {
            celulasIndividuais.push("C" + i);
        }
    }

    // Armazena os valores anteriores em uma propriedade de script
    var propriedade = PropertiesService.getScriptProperties();
    var valoresAnteriores = propriedade.getProperty("valoresAnteriores");
    //Logger.log("valores anteriores: "+ valoresAnteriores );

    var listaValoresAtuais = [];

    if (!valoresAnteriores) {
        // Se não há valores anteriores, armazena os valores atuais
        var valoresAtuais = {};

        // Itera sobre as células individuais
        for (var i = 0; i < celulasIndividuais.length; i++) {
            var valorAtual = guia.getRange(celulasIndividuais[i]).getValue();
            valoresAtuais[celulasIndividuais[i]] = valorAtual;
            listaValoresAtuais += celula + ": " + valorAtual + "\n";
        }

        // Armazena os valores atuais como valores anteriores
        propriedade.setProperty("valoresAnteriores", JSON.stringify(valoresAtuais));

    } else {
        valoresAnteriores = JSON.parse(valoresAnteriores);

        // Verifica se o número de valores anteriores é igual ao número de células individuais
        var aoMenosUmaDiferente = false;

        for (var i = 0; i < celulasIndividuais.length; i++) {
            var valorAtual = guia.getRange(celulasIndividuais[i]).getValue();

            // Verifica se o valor atual é igual ao valor anterior
            if (valorAtual === valoresAnteriores[celulasIndividuais[i]]) {
                aoMenosUmaDiferente = true;
                celulasIguais.push(celulasIndividuais[i]); // Adiciona o nome da célula à lista
            } else {
                celulasDiferentes.push(celulasIndividuais[i]); // Adiciona o nome da célula à lista de diferentes
            }
        }

        // Se houver células diferentes, envia um e-mail
        if (aoMenosUmaDiferente) {
            var mensagem = "Computadores parados: \n";

            for (var i = 0; i < celulasIguais.length; i++) {
                var celulaAtual = celulasIguais[i];
                mensagem += celulaAtual + " - id:\n" + guia.getRange("E" + celulaAtual.substring(1)).getValue() + "\n\n";
            }

            // Imprime a mensagem no console
            Logger.log("Mensagem: " + mensagem);

            enviarMensagemTelegram(mensagem)
            //testaTimeEnviar(mensagem);
        }

        // Copia os valores da coluna 'Q' para 'R', 'P' para 'Q', 'O' para 'P', e assim por diante até 'G' para 'H'
        for (var coluna = 17; coluna >= 7; coluna--) { // Começa da coluna 'Q' (coluna 17) e vai até a coluna 'G' (coluna 7)
            var rangeOrigem = guia.getRange(primeiraCelula, coluna, ultimaCelula - primeiraCelula + 1);
            var rangeDestino = guia.getRange(primeiraCelula, coluna + 1, ultimaCelula - primeiraCelula + 1);
            rangeOrigem.copyTo(rangeDestino, {formatOnly: false});
        }

        // Escreve "OK" ou "Atenção" na coluna E com base nas diferenças
        for (var i = 0; i < celulasDiferentes.length; i++) {
            var celulaAtual = guia.getRange("G" + celulasDiferentes[i].substring(1));
            celulaAtual.setValue("OK");
            celulaAtual.setFontColor("green"); // Define a cor do texto como azul
        }
        for (var i = 0; i < celulasIguais.length; i++) {
            var celulaAtual = guia.getRange("G" + celulasIguais[i].substring(1));
            celulaAtual.setValue("Atenção");
            celulaAtual.setFontColor("red"); // Define a cor do texto como vermelho
        }

        // Atualiza os valores anteriores com os valores atuais
        var valoresAtuais = {};

        for (var i = 0; i < celulasIndividuais.length; i++) {
            var valorAtual = guia.getRange(celulasIndividuais[i]).getValue();
            valoresAtuais[celulasIndividuais[i]] = valorAtual;
        }
        propriedade.setProperty("valoresAnteriores", JSON.stringify(valoresAtuais));
    }
}


function testaTimeEnviar(mensagem) {

    //Verifica o horário atual
    var horarioAtual = new Date();
    var hora = horarioAtual.getHours();
    var minutos = horarioAtual.getMinutes();
    //Logger.log(hora + ":" + minutos);

    // Define os intervalos de horário nos quais o e-mail não será enviado
    var intervalosNaoEnviar = [
        {inicio: 4, fim: 5, minInicio: 50, minFim: 05},
        {inicio: 9, fim: 10, minInicio: 50, minFim: 05},
        {inicio: 14, fim: 15, minInicio: 50, minFim: 05},
        {inicio: 19, fim: 20, minInicio: 50, minFim: 05}
    ];

    var enviarMensagem = true;
    for (var i = 0; i < intervalosNaoEnviar.length; i++) {
        var intervalo = intervalosNaoEnviar[i];
        if (
            // Verifica se a hora atual está dentro do intervalo
            (hora === intervalo.inicio && minutos >= intervalo.minInicio) ||
            (hora === intervalo.fim && minutos <= intervalo.minFim) ||
            (hora > intervalo.inicio && hora < intervalo.fim)
        ) {
            enviarMensagem = false;
            break;
        }
    }

    if (enviarMensagem) {
        enviarMensagemTelegram(mensagem)
    } else {
        Logger.log("Mensagem não enviada devido ao horário.");
    }
}


function enviarMensagemTelegram(mensagem) {
    var token = "6446494638:AAE5lkb9s74m_5R8DE-z2uDqt5PrYEQUTo8"; // Substitua pelo seu token de acesso
    var chatId = "-1001971264843"; // Substitua pelo ID do chat para o qual deseja enviar a mensagem

    var url = "https://api.telegram.org/bot" + token + "/sendMessage?chat_id=" + chatId + "&text=" + encodeURIComponent(mensagem);

    var response = UrlFetchApp.fetch(url);
    Logger.log(response.getContentText());
}


function copiarDadosParaGuiaDestino(guiaDestinoNome) {
    try {
        // Abra a planilha ativa
        var planilha = SpreadsheetApp.getActiveSpreadsheet();

        // Especifica a guia de origem
        var guiaOrigemNome = "Dados";

        // Obtenha a guia de origem
        var guiaOrigem = planilha.getSheetByName(guiaOrigemNome);

        // Verifique se a guia de origem foi encontrada
        if (!guiaOrigem) {
            console.error('Guia de origem não encontrada.');
            return;
        }

        // Obtenha os dados da guia de origem
        var dadosOrigem = guiaOrigem.getRange('A:C').getValues();

        // Obtenha a guia de destino
        var guiaDestino = planilha.getSheetByName(guiaDestinoNome);

        // Verifique se a guia de destino foi encontrada
        if (!guiaDestino) {
            console.error('Guia de destino não encontrada:', guiaDestinoNome);
            return;
        }

        // Obtenha os dados da guia de destino
        var dadosDestino = guiaDestino.getRange('A:C').getValues();

        // Limpe as colunas B e C na guia de destino a partir da segunda linha
        guiaDestino.getRange(2, 2, guiaDestino.getLastRow(), 2).clear();

        // Itera sobre os dados de origem, começando da segunda linha
        for (var i = 1; i < dadosOrigem.length; i++) {
            // Encontre o ID na guia de destino
            var id = dadosOrigem[i][0];

            // Procure o ID na guia de destino
            for (var j = 1; j < dadosDestino.length; j++) {
                if (dadosDestino[j][0] == id) {
                    // Se encontrado, copie os valores das colunas B e C da guia de origem para as colunas B e C da guia de destino
                    guiaDestino.getRange('B' + (j + 1)).setValue(dadosOrigem[i][1]);
                    guiaDestino.getRange('C' + (j + 1)).setValue(dadosOrigem[i][2]);
                    break;
                }
            }
        }

        // Exibe mensagem de log ao concluir a cópia para a guia específica
        console.log('Concluído para ' + guiaDestinoNome);
        // Exibe mensagem de log na interface da planilha
        SpreadsheetApp.getUi().alert('Concluído para ' + guiaDestinoNome);

    } catch (e) {
        console.error('Ocorreu um erro:', e.toString());

        // Tratamento de exceções: Aguarde 15 segundos antes de tentar novamente
        Utilities.sleep(15000);

        // Chama a função novamente
        copiarDadosParaGuiaDestino(guiaDestinoNome);
    }
}

// Exemplo de uso da função com o nome da guia de destino como parâmetro
// copiarDadosParaGuiaDestino("R1");

function copiarDadosParaR1() {
    copiarDadosParaGuiaDestino("R1");
}

function copiarDadosParaR2() {
    copiarDadosParaGuiaDestino("R2");
}

function copiarDadosParaR3() {
    copiarDadosParaGuiaDestino("R3");
}

function copiarDadosParaR4() {
    copiarDadosParaGuiaDestino("R4");
}

function copiarDadosParaR5() {
    copiarDadosParaGuiaDestino("R5");
}

function copiarDadosParaT1() {
    copiarDadosParaGuiaDestino("T1");
}


function copiarDadosParaOutrasGuias() {
    try {
        // Abra a planilha ativa
        var planilha = SpreadsheetApp.getActiveSpreadsheet();

        // Especifique as guias de destino
        var guiasDestinoNomes = ["R1", "R2", "R3", "R4", "R5", "T1"];

        // Especifica a guia de origem
        var guiaOrigemNome = "Dados";

        // Obtenha a guia de origem
        var guiaOrigem = planilha.getSheetByName(guiaOrigemNome);

        // Verifique se a guia de origem foi encontrada
        if (!guiaOrigem) {
            console.error('Guia de origem não encontrada.');
            return;
        }

        // Obtenha os dados da guia de origem
        var dadosOrigem = guiaOrigem.getRange('A:C').getValues();

        // Itera sobre as guias de destino
        guiasDestinoNomes.forEach(function (guiaDestinoNome) {
            // Obtenha a guia de destino
            var guiaDestino = planilha.getSheetByName(guiaDestinoNome);

            // Verifique se a guia de destino foi encontrada
            if (!guiaDestino) {
                console.error('Guia de destino não encontrada:', guiaDestinoNome);
                return;
            }

            // Obtenha os dados da guia de destino
            var dadosDestino = guiaDestino.getRange('A:C').getValues();

            // Limpe as colunas B e C na guia de destino a partir da segunda linha
            guiaDestino.getRange(2, 2, guiaDestino.getLastRow(), 2).clear();

            // Itera sobre os dados de origem, começando da segunda linha
            for (var i = 1; i < dadosOrigem.length; i++) {
                // Encontre o ID na guia de destino
                var id = dadosOrigem[i][0];

                // Procure o ID na guia de destino
                for (var j = 1; j < dadosDestino.length; j++) {
                    if (dadosDestino[j][0] == id) {
                        // Se encontrado, copie os valores das colunas B e C da guia de origem para as colunas B e C da guia de destino
                        guiaDestino.getRange('B' + (j + 1)).setValue(dadosOrigem[i][1]);
                        guiaDestino.getRange('C' + (j + 1)).setValue(dadosOrigem[i][2]);
                        break;
                    }
                }
            }

            // Exibe mensagem de log ao concluir a cópia para a guia específica
            console.log('Concluído para ' + guiaDestinoNome);
        });

        // Exibe mensagem de log ao concluir todas as cópias
        console.log('Cópias concluídas para todas as guias de destino.');

    } catch (e) {
        console.error('Ocorreu um erro:', e.toString());

        // Tratamento de exceções: Aguarde 15 segundos antes de tentar novamente
        Utilities.sleep(15000);

        // Chama a função novamente
        copiarDadosParaOutrasGuias();
    }
}

function copiarColunaGparaJ(guiaOrigemNome, guiaDestinoNome) {
    let tentativas = 0;

    while (tentativas < MAX_TENTATIVAS) {
        try {
            // Abra a planilha ativa
            var planilha = SpreadsheetApp.getActiveSpreadsheet();

            // Especifique as guias de origem e destino
            var guiaOrigem = planilha.getSheetByName(guiaOrigemNome);
            var guiaDestino = planilha.getSheetByName(guiaDestinoNome);

            // Verifique se as guias foram encontradas
            if (!guiaOrigem || !guiaDestino) {
                throw new Error('Guia não encontrada.');
            }

            // Obtenha os dados da guia de origem e destino
            var dadosOrigem = guiaOrigem.getRange('A:G').getValues();
            var dadosDestino = guiaDestino.getRange('A:J').getValues();

            // Limpe a coluna J na guia de destino
            guiaDestino.getRange('J:J').clear();

            // Criar um objeto para armazenar dados da guia de destino
            var mapaDestino = {};

            // Preencher o objeto com os dados da guia de destino
            for (var k = 1; k < dadosDestino.length; k++) {
                var idDestino = dadosDestino[k][0];
                mapaDestino[idDestino] = k + 1; // +1 para corresponder ao índice da linha da planilha
            }

            // Itere sobre os dados de origem
            for (var i = 1; i < dadosOrigem.length; i++) {
                // Encontre o ID na guia de destino
                var id = dadosOrigem[i][0];

                // Verifique se o ID está no objeto de mapeamento
                if (mapaDestino[id] !== undefined) {
                    // Se encontrado, copie o valor da coluna G da guia de origem para a coluna J da guia de destino
                    guiaDestino.getRange('J' + mapaDestino[id]).setValue(dadosOrigem[i][6]);
                }
            }

            // Saia do loop se a execução for bem-sucedida
            break;

        } catch (error) {
            console.error('Erro na tentativa ' + (tentativas + 1) + ': ' + error.toString());
            tentativas++;
            Utilities.sleep(15000); // Aguarde 15 segundos antes de tentar novamente
        }
    }
}

function copiarColunaComVLOOKUP2(guiaOrigemNome, guiaDestinoNome) {
    let tentativas = 0;

    while (tentativas < MAX_TENTATIVAS) {
        try {
            // Abra a planilha ativa
            var planilha = SpreadsheetApp.getActiveSpreadsheet();

            // Especifique as guias de origem e destino
            var guiaOrigem = planilha.getSheetByName(guiaOrigemNome);
            var guiaDestino = planilha.getSheetByName(guiaDestinoNome);

            // Verifique se as guias foram encontradas
            if (!guiaOrigem || !guiaDestino) {
                throw new Error('Guia não encontrada.');
            }

            // Obtenha os dados da guia de origem e destino
            var dadosOrigem = guiaOrigem.getRange('A:G').getValues();
            var dadosDestino = guiaDestino.getRange('A:J').getValues();

            // Limpe as colunas I e J na guia de destino a partir da linha 2
            guiaDestino.getRange('I2:J').clear();

            // Criar um objeto para armazenar dados da guia de destino
            var mapaDestino = {};

            // Preencher o objeto com os dados da guia de destino
            for (var k = 1; k < dadosDestino.length; k++) {
                var idDestino = dadosDestino[k][0];
                mapaDestino[idDestino] = k + 1; // +1 para corresponder ao índice da linha da planilha
            }

            // Itere sobre os dados de origem a partir da linha 2
            for (var i = 1; i < dadosOrigem.length; i++) {
                // Encontre o ID na guia de destino
                var id = dadosOrigem[i][0];

                // Verifique se o ID está no objeto de mapeamento
                if (mapaDestino[id] !== undefined) {
                    // Se encontrado, copie os valores da coluna E e G da guia de origem para as colunas I e J da guia de destino
                    guiaDestino.getRange('I' + mapaDestino[id]).setValue(dadosOrigem[i][4]); // Coluna E
                    guiaDestino.getRange('J' + mapaDestino[id]).setValue(dadosOrigem[i][6]); // Coluna G
                }
            }

            // Saia do loop se a execução for bem-sucedida
            break;

        } catch (error) {
            console.error('Erro na tentativa ' + (tentativas + 1) + ': ' + error.toString());
            tentativas++;
            Utilities.sleep(15000); // Aguarde 15 segundos antes de tentar novamente
        }
    }
}

function attLinkCelulaF2ParaF1() {

    for (let tentativas = 0; tentativas < MAX_TENTATIVAS; tentativas++) {
        try {
            const planilha = SpreadsheetApp.getActiveSpreadsheet();
            const guiaDados = planilha.getSheetByName('Dados');

            if (!guiaDados) {
                throw new Error('Guia de dados não encontrada.');
            }

            const valorCelulaF2 = guiaDados.getRange('F2').getValue();
            guiaDados.getRange('F1').setValue(valorCelulaF2);

            break;

        } catch (error) {
            console.error('Erro na tentativa ' + (tentativas + 1) + ': ' + error.toString());
            Utilities.sleep(15000);
        }
    }
}


function copiarLevel() {
    try {
        // Abra a planilha ativa
        var planilha = SpreadsheetApp.getActiveSpreadsheet();

        // Especifica a guia de origem
        var guiaOrigemNome = "T1";
        var guiaDestinoNome = "R1";

        // Obtenha a guia de origem
        var guiaOrigem = planilha.getSheetByName(guiaOrigemNome);

        // Verifique se a guia de origem foi encontrada
        if (!guiaOrigem) {
            console.error('Guia de origem não encontrada.');
            return;
        }

        // Obtenha os dados da guia de origem
        var dadosOrigem = guiaOrigem.getRange('A:I').getValues();

        // Obtenha a guia de destino
        var guiaDestino = planilha.getSheetByName(guiaDestinoNome);

        // Verifique se a guia de destino foi encontrada
        if (!guiaDestino) {
            console.error('Guia de destino não encontrada:', guiaDestinoNome);
            return;
        }

        // Obtenha os dados da guia de destino
        var dadosDestino = guiaDestino.getRange('A:I').getValues();

        // Itera sobre os dados de origem, começando da segunda linha
        for (var i = 1; i < dadosOrigem.length; i++) {
            // Encontre o ID na guia de destino
            var id = dadosOrigem[i][0];

            // Procure o ID na guia de destino
            for (var j = 1; j < dadosDestino.length; j++) {
                if (dadosDestino[j][0] == id) {
                    // Se encontrado, copie os valores das colunas B e C da guia de origem para as colunas B e C da guia de destino
                    guiaDestino.getRange('I' + (j + 1)).setValue(dadosOrigem[i][8]);
                    break;
                }
            }
        }

        // Exibe mensagem de log ao concluir a cópia para a guia específica
        console.log('Concluído para ' + guiaDestinoNome);
        // Exibe mensagem de log na interface da planilha
        // SpreadsheetApp.getUi().alert('Concluído para ' + guiaDestinoNome);

    } catch (e) {
        console.error('Ocorreu um erro:', e.toString());

        // Tratamento de exceções: Aguarde 15 segundos antes de tentar novamente
        Utilities.sleep(15000);

        // Chama a função novamente
        copiarDadosParaGuiaDestino(guiaDestinoNome);
    }
}


function copiarLevelParaOutrasGuias() {
    try {
        // Abra a planilha ativa
        var planilha = SpreadsheetApp.getActiveSpreadsheet();

        // Especifique as guias de destino
        var guiasDestinoNomes = ["R2", "R3", "R4", "R5", "T1"];

        // Especifica a guia de origem
        var guiaOrigemNome = "R1";

        // Obtenha a guia de origem
        var guiaOrigem = planilha.getSheetByName(guiaOrigemNome);

        // Verifique se a guia de origem foi encontrada
        if (!guiaOrigem) {
            console.error('Guia de origem não encontrada.');
            return;
        }

        // Obtenha os dados da guia de origem
        var dadosOrigem = guiaOrigem.getRange('A:I').getValues();

        // Itera sobre as guias de destino
        guiasDestinoNomes.forEach(function (guiaDestinoNome) {
            // Obtenha a guia de destino
            var guiaDestino = planilha.getSheetByName(guiaDestinoNome);

            // Verifique se a guia de destino foi encontrada
            if (!guiaDestino) {
                console.error('Guia de destino não encontrada:', guiaDestinoNome);
                return;
            }

            // Obtenha os dados da guia de destino
            var dadosDestino = guiaDestino.getRange('A:I').getValues();

            // Itera sobre os dados de origem, começando da segunda linha
            for (var i = 1; i < dadosOrigem.length; i++) {
                // Encontre o ID na guia de destino
                var id = dadosOrigem[i][0];

                // Procure o ID na guia de destino
                for (var j = 1; j < dadosDestino.length; j++) {
                    if (dadosDestino[j][0] == id) {
                        // Se encontrado, copie os valores das colunas B e C da guia de origem para as colunas B e C da guia de destino
                        guiaDestino.getRange('I' + (j + 1)).setValue(dadosOrigem[i][8]);
                        break;
                    }
                }
            }

            // Exibe mensagem de log ao concluir a cópia para a guia específica
            console.log('Concluído para ' + guiaDestinoNome);
        });

        // Exibe mensagem de log ao concluir todas as cópias
        console.log('Cópias concluídas para todas as guias de destino.');

    } catch (e) {
        console.error('Ocorreu um erro:', e.toString());

        // Tratamento de exceções: Aguarde 15 segundos antes de tentar novamente
        Utilities.sleep(15000);

        // Chama a função novamente
        copiarDadosParaOutrasGuias();
    }
}

function copiarValorFichasAposRecolher() {
    try {
        // Abra a planilha ativa
        var planilha = SpreadsheetApp.getActiveSpreadsheet();

        // Especifique as guias de destino
        var guiasDestinoNomes = ["R3", "R4", "R5"];

        // Especifica a guia de origem
        var guiaOrigemNome = "Recolher";

        // Obtenha a guia de origem
        var guiaOrigem = planilha.getSheetByName(guiaOrigemNome);

        // Verifique se a guia de origem foi encontrada
        if (!guiaOrigem) {
            console.error('Guia de origem não encontrada.');
            return;
        }

        // Obtenha os dados da guia de origem
        var dadosOrigem = guiaOrigem.getRange('B:E').getValues();

        // Itera sobre as guias de destino
        guiasDestinoNomes.forEach(function (guiaDestinoNome) {
            // Obtenha a guia de destino
            var guiaDestino = planilha.getSheetByName(guiaDestinoNome);

            // Verifique se a guia de destino foi encontrada
            if (!guiaDestino) {
                console.error('Guia de destino não encontrada:', guiaDestinoNome);
                return;
            }

            // Obtenha os dados da guia de destino
            var dadosDestino = guiaDestino.getRange('B:E').getValues();

            // Itera sobre os dados de origem, começando da segunda linha
            for (var i = 1; i < dadosOrigem.length; i++) {
                // Encontre o ID na guia de destino
                var id = dadosOrigem[i][0];

                // Procure o ID na guia de destino
                for (var j = 1; j < dadosDestino.length; j++) {
                    if (dadosDestino[j][0] == id) {
                        // Se encontrado, copie os valores das colunas B e C da guia de origem para as colunas B e C da guia de destino
                        guiaDestino.getRange('E' + (j + 1)).setValue(dadosOrigem[i][3]);
                        break;
                    }
                }
            }

            // Exibe mensagem de log ao concluir a cópia para a guia específica
            console.log('Concluído para ' + guiaDestinoNome);
        });

        // Exibe mensagem de log ao concluir todas as cópias
        console.log('Cópias concluídas para todas as guias de destino.');

    } catch (e) {
        console.error('Ocorreu um erro:', e.toString());

        // Tratamento de exceções: Aguarde 15 segundos antes de tentar novamente
        Utilities.sleep(15000);

        // Chama a função novamente
        copiarDadosParaOutrasGuias();
    }
}
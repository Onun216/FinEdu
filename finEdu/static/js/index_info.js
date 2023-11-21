function sp500Info() {
    let sp500_info = 'O S&P 500 é um índice de mercado que segue o desempenho das 500 maiores empresas de capital aberto dos Estados Unidos, com base na capitalização de mercado.' +
        '<br>É um dos índices mais amplamente seguidos do mundo e é considerado um indicador importante do desempenho do mercado de ações dos EUA.' +
        '<br>O S&P 500 é composto por empresas de uma ampla gama de setores, incluindo tecnologia, saúde, finanças, industrial e bens de consumo. As empresas são selecionadas para o índice com base em uma série de fatores, incluindo tamanho, liquidez e representatividade de setor.' +
        '<br>O desempenho do S&P 500 é medido pela variação do seu preço ao longo do tempo. O preço do índice é calculado como a média ponderada dos preços das ações das empresas que o compõem.' +
        '<br>' +
        '<br>O S&P 500 é um índice ponderado por capitalização de mercado, o que significa que o peso de cada empresa no índice é determinado pelo seu tamanho de capitalização de mercado. As empresas com maior capitalização de mercado têm um peso maior no índice do que as empresas com menor capitalização de mercado.' +
        '<br>O S&P 500 é um índice de retorno total, o que significa que inclui dividendos. Os dividendos são pagos pelos lucros das empresas para seus acionistas. Os dividendos são reinvestidos no índice, o que ajuda a impulsionar seu crescimento ao longo do tempo.'

    document.getElementById('spy-info').innerHTML = sp500_info;
}

function ndqCompInfo() {
    let ndqComp_info = 'O Nasdaq Composite 100 é um índice de ações composto por 100 das maiores empresas não financeiras listadas na Nasdaq Stock Market, com base na capitalização de mercado.' +
        '<br>O índice é ponderado pela capitalização de mercado, o que significa que as empresas com maior capitalização de mercado têm um peso maior no índice.' +
        '<br>O Nasdaq Composite 100 é um índice de crescimento, o que significa que as empresas que o compõem são geralmente empresas inovadoras com potencial de crescimento futuro. O índice é dominado por empresas de tecnologia, como Apple, Microsoft, Amazon e Alphabet.' +
        '<br>O Nasdaq Composite 100 é um índice volátil, o que significa que seu preço pode flutuar significativamente em um curto período de tempo. Os investidores devem estar cientes desse risco antes de investir no índice.'

    document.getElementById('ndq-info').innerHTML = ndqComp_info;
}
function djiInfo() {
    let dji_info = ' O Dow Jones Industrial Average (DJIA) é um índice de mercado de ações de 30 grandes empresas de capital aberto listadas nas bolsas de valores dos Estados Unidos. O DJIA é um dos índices de ações mais antigos e mais conhecidos do mundo.' +
        '<br>O DJIA é um índice ponderado por preço, o que significa que o preço de cada ação individual tem um impacto no valor do índice. As empresas com preços de ações mais altos têm um peso maior no índice.' 
        '<br>O DJIA é considerado um índice de referência para o mercado de ações dos EUA. Muitos profissionais consideram que ele é uma representação inadequada do mercado de ações dos EUA em geral quando comparado a um índice de mercado mais amplo, como o S&P 500.'

    document.getElementById('dji-info').innerHTML = dji_info;
}

function russell2000Info() {
    let russell2000_info = 'O Russell 2000 é um índice de mercado de ações de 2.000 pequenas empresas de capital aberto listadas nas bolsas de valores dos Estados Unidos. O índice é ponderado por capitalização de mercado, o que significa que as empresas com maior capitalização de mercado têm um peso maior no índice.' +
        '<br>O Russell 2000 é considerado um índice de referência para o mercado de ações de pequenas empresas dos EUA.'  +
        '<br>O Russell 2000 é geralmente considerado um índice de crescimento, pois as empresas que o compõem são geralmente empresas inovadoras com potencial de crescimento futuro.' +
        '<br> No entanto, o índice também pode ser visto como um índice cíclico, pois o desempenho das pequenas empresas tende a ser mais afetado pelos ciclos econômicos do que o desempenho das grandes empresas.'

    document.getElementById('russell-info').innerHTML = russell2000_info;
}

function normalizedReturnInfo() {
    let normR_info = '' +
        '<br>' 
        

    document.getElementById('normR-info').innerHTML = normR_info;
}


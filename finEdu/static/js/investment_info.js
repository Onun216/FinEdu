function indexInfo() {
    let index = 'Um índice é uma medida do desempenho de um mercado ou segmento do mercado e é calculado com base no preço de um conjunto de ativos, como ações por exemplo.' +
                '<br>Os índices são usados por investidores para medir o desempenho dos seus investimentos, bem como para comparar o desempenho de diferentes mercados ou segmentos do mercado.' +
                '<br>' +
                "<br>O S&P 500 é um índice de ações que mede o desempenho das 500 maiores empresas de capital aberto nos Estados Unidos. O índice é calculado pela Standard & Poor's, uma agência de classificação de crédito." +
                '<br>O S&P 500 é um dos índices mais amplamente seguidos do mundo e é frequentemente usado como uma medida do desempenho do mercado de ações dos EUA.' +
                '<br>O Dow Jones Industrial Average (DJIA) é um índice de ações que mede o desempenho de 30 das maiores empresas de capital aberto nos Estados Unidos.' +
                '<br>O Nasdaq Composite é um índice de ações que mede o desempenho de todas as empresas listadas na Nasdaq, a bolsa de valores eletrónica dos Estados Unidos.' +
                '<br>' +
                '<br>Um índice é como um termómetro que mede a temperatura do mercado financeiro. ' +
                '<br>' +
                '<br>Se o S&P 500 está a subir, significa que as ações das empresas que compõem o índice estão a valorizar. Se está a cair, significa que as ações das empresas que compõem o índice estão a desvalorizar.' +
                '<br>' +
                '<br>Enquanto que um índice é uma medida do desempenho de um mercado ou segmento do mercado, um ETF, ou Exchange-Traded Fund, é um tipo de fundo de investimento que segue um índice.' +
                '<br>A principal diferença entre um ETF e um índice é que um ETF é um investimento que pode ser comprado e vendido na bolsa de valores, como uma ação. Um índice, por outro lado, é apenas uma medida do desempenho de um mercado ou segmento do mercado.' +
                '<br>A principal diferença entre um ETF e um índice é que um ETF é um investimento que pode ser comprado e vendido na bolsa de valores, como uma ação.' +
                '<brETFs são mais líquidos do que fundos de índice, o que significa que podem ser comprados e vendidos mais facilmente.' +
                '<br>' +
                '<br>Em geral, ETFs são uma boa opção para investidores que procuram um investimento acessível, líquido e diversificado. Índices são uma boa opção para investidores que procuram uma medida do desempenho de um mercado ou segmento do mercado.' +          
                '<br>' +
                '<br>Os ETFs são uma forma acessível de investir em uma variedade de mercados.'
    
    return index;  
}

function stockInfo() {
    let stock = 'Uma ação é uma unidade de propriedade de uma empresa, uma parcela do capital social de uma empresa. Ao comprar uma ação, o investidor torna-se um proprietário parcial da empresa.' +
               '<br>As ações são negociadas em bolsas de valores e seu preço flutua de acordo com a oferta e a procura.' +    
               '<br>O preço de uma ação é determinado pela oferta e procura. Se mais pessoas quiserem comprar uma ação do que vender, o preço da ação subirá. Se mais pessoas quiserem vender uma ação do que comprar, o preço da ação cairá.' +
               '<br>Os acionistas têm certos direitos, incluindo o direito de receber dividendos, o direito de votar em assembleias gerais de acionistas e o direito de receber uma parte do património da empresa em caso de liquidação.' +
               '<br>' +
               '<br>Existem dois tipos principais de ações:' +
                    '<br> - Ações ordinárias: são as ações mais comuns e conferem aos acionistas o direito de voto em assembleias gerais de acionistas e o direito de receber dividendos.' +
                    '<br> - Ações preferenciais: conferem aos acionistas o direito de receber dividendos antes dos acionistas ordinários e o direito de receber um valor predeterminado em caso de liquidação da empresa.' +

               '<br>Para investir em ações, é necessário abrir uma conta de corretagem. Uma corretora é uma empresa que intermedia a compra e venda de ações.' +
               '<br>Depois de abrir uma conta de corretagem, o investidor pode comprar e vender ações através da plataforma da corretora.' +
               '<br>' +
               '<br>Investir em ações é um investimento de risco. O preço das ações pode subir ou cair, e os investidores podem perder dinheiro.'
            
    return stock; 
}
function bondInfo() {
    let bond = 'Uma obrigação financeira é um título de dívida emitido por uma entidade, que pode ser uma empresa, um governo ou outra instituição' +
               '<br>Quando um investidor compra uma obrigação, está a emprestar dinheiro à entidade emissora. Em troca, o investidor recebe uma remuneração, geralmente na forma de juros.' +
               '<br>' +
               '<br>As obrigações são um tipo de investimento de renda fixa, o que significa que o investidor sabe com antecedência quanto receberá de juros. O valor nominal da obrigação é o valor que será reembolsado ao investidor no vencimento.' +
               '<br>Existem vários tipos de obrigações, cada um com suas próprias características.' + 
               '<br>' +
               '<br>Alguns dos tipos mais comuns de obrigações incluem:' + 
                    '<br> - Obrigações corporativas: são emitidas por empresas para financiar suas atividades.' +
                    '<br> - Obrigações governamentais: são emitidas por governos para financiar suas despesas.' +
                    '<br> - Obrigações municipais: são emitidas por municípios para financiar projetos de infraestrutura.' +
                    '<br> - Obrigações indexadas: são indexadas a um índice de inflação, o que significa que os juros pagos são ajustados de acordo com a inflação.'
    return bond; 
}

// Estrutura permite que as 3 funções sejam projectadas nun só div container depois de accionar um dos 3 butões
document.getElementById('index-info').addEventListener("click", function() {
    var content = indexInfo();
    document.getElementById('investment-info').innerHTML = content;
});

document.getElementById('stock-info').addEventListener("click", function() {
    var content = stockInfo();
    document.getElementById('investment-info').innerHTML = content;
});

document.getElementById('bond-info').addEventListener("click", function() {
    var content = bondInfo();
    document.getElementById('investment-info').innerHTML = content;
});


function sp500norm() {
    let norm = 'O gráfico representa o retorno normalizado do S&P500 desde 1957 até 2023 e vemos que o retorno máximo, em Janeiro de 2022, chegou aos 10282%. De 1957 até hoje, mesmo incluindo subidas e descidas de preço, o S&P500 teve um retorno de mais de 9000%.' +
        '<br>Um olhar mais atento mostra que o Crash de 1987, em Outubro, levou a uma queda de 31,50% no espaço de menos de 1 mês. O COVID, por exemplo, levou a uma queda que começou em Fevereiro de 2020 e terminou em Março de 2020, acumulando um perda de 33,6%.' +
        '<br>' +
        '<br>Insere dois valores para ver qual foi o ganho ou a perda!'

    document.getElementById('sp500-norm').innerHTML = norm;
}


const btn = document.getElementById('btn');
const calc = document.getElementById('calc');

// Função que recebe input e calcula o ganho ou perda entre dois valores. 
function gainOrloss() {
    const num1 = parseFloat(document.getElementById('start-price').value);
    const num2 = parseFloat(document.getElementById('end-price').value);
    const result = document.getElementById('result');
    if (num2 > num1) {
        let diff = num2 - num1;
        result.value = `${diff.toFixed(2)}%`;

    } else {
        let diff = num1 - num2;
        let div = (diff / num1) * 100;
        result.value = `${-div.toFixed(2)}%`;
    }
}
calc.addEventListener('click', () => {
    gainOrloss();
});
btn.addEventListener('click', () => {
    document.getElementById('start-price').value = ' ';
    document.getElementById('end-price').value = ' ';
    document.getElementById('result').value = ' ';
});


var nome = "Jogador"
var exp = 1000
var nivel

if (exp<1001){
    nivel = "Ferro"
}
else if (1000<exp<2001){
    nivel = "Bronze"
}
else if (2000<exp<3001){
    nivel = "Prata"
}
else if (3000<exp<4000){
    nivel = "Ouro"
}
else if (4000<exp<5000){
    nivel = "Platina"
}
else if (5000<exp<6000){
    nivel = "Ascedente"
}
else if (6000<exp<7000){
    nivel = "Imortal"
}
else{
    nivel = "Radiante"
}

console.log(`O Herói de nome ${nome} está no nível de ${nivel}`)

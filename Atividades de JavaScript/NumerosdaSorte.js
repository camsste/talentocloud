for (let i = 0; i < numerosDaSorte.length; i++ ){
    if(numerosDaSorte[i] % 2 == 0 && numerosDaSorte[i] < 50){
      console.log(numerosDaSorte[i] + " é par e menor que 50.")
    } else if (numerosDaSorte[i] < 50) {
      console.log(numerosDaSorte[i] + " é menor que 50.")
    } else {
      console.log(numerosDaSorte[i] + " é maior que 50.")
    }
  }
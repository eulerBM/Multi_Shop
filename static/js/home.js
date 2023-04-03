var carrinho = 2

function get_id(id, request){
    

    fetch('/carrin/', {
    method: 'POST',
    body: JSON.stringify({
        id: id,
        request: request }),
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(response => {
    if (response.ok) {
        console.log('Produto adicionado ao carrinho!')
        document.getElementById('carrinho').innerHTML = carrinho++;
        alert("Produto adicionado com sucesso ao carrinho")
        

    } else {
      console.error('Ocorreu um erro ao adicionar o produto ao carrinho!')
      alert("Ja existe no carrinho")
    }
  })
  .catch(error => {
    console.error('Ocorreu um erro ao enviar a requisição:', error)
  })

    
}






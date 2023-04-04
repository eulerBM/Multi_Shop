var carrinho = 1
var like_objetc = 0

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
        response.json().then(data => {
          if (data.message === "Produto adicionado ao carrinho com sucesso!") {
            carrinho++;
            document.getElementById('carrinho').innerHTML = carrinho;
          }
          alert(data.message);
        });
    } else {
      console.error('Ocorreu um erro ao adicionar o produto ao carrinho!')
    }
  })
  .catch(error => {
    console.error('Ocorreu um erro ao enviar a requisição:', error)
  });
}



function like(id, request){
    
    fetch('/like/', {
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
      response.json().then(data => {
        if (data.message === "Like dado com sucesso") {
          like_objetc++;
          document.getElementById('like_01').innerHTML = like_objetc;
        }
        alert(data.message);
      });
  } else {
    console.error('Ocorreu um erro ao dar like')
  }
})
.catch(error => {
  console.error('Ocorreu um erro ao enviar a requisição:', error)
});
}






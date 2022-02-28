let buttonStoreName;
let storeName;
const form = document.getElementById('client-form')
const code = document.querySelector('.code')
const cards = document.getElementById('cards')
const body = document.querySelector('body')
const response = []
const selectedCards = []

const img3comLink = `
<div class="card">
  <img class="card-img-top" src="../static/images/client/Fidelidade3.PNG" alt="Card image cap">
  <div class="card-body">
    <a href="/beneficios" onclick="getStoreName()">Consultar benéficio Farmácia Nunes</a>
  </div>
</div>`

const img4comLink = `
<div class="card">
  <img class="card-img-top" src="../static/images/client/Fidelidade4.PNG" alt="Card image cap">
  <div class="card-body">
    <a href="/beneficios" onclick="getStoreName()">Consultar benéficio Bar Avião</a>
  </div>
</div> `

const img3 = `
<div class="card">
  <img class="card-img-top" src="../static/images/client/Fidelidade3.PNG" alt="Card image cap" style="width: 286px; height: 180px;">
  <div class="card-body">
  <a href="/beneficios" onclick="getStoreName()">Consultar benéficio Farmácia Nunes</a>
  </div>
</div>  `

const img4 = `
<div class="card">
  <img class="card-img-top" src="../static/images/client/Fidelidade4.PNG" alt="Card image cap" style="width: 286px; height: 180px;">
  <div class="card-body">
  <a href="/beneficios" onclick="getStoreName()">Consultar benéficio Bar Xand</a>
  </div>
</div> `

handleInsertImage()

function handleInsertImage() {
  let stores;

  if (localStorage.getItem('@e-fidelity:stores')) {
    stores = localStorage.getItem('@e-fidelity:stores').split(',')
  }

  if (stores != null) {
    if (stores.find(element => element == "12")) {
      cards.innerHTML += img3comLink
      response.push("12")
    }

    if (stores.find(element => element == "123")) {
      cards.innerHTML += img4comLink
      response.push("123")
    }

    if (stores.find(element => element == "1234")) {
      cards.innerHTML += img3
      response.push("1234")
    }

    if (stores.find(element => element == "12345")) {
      cards.innerHTML += img4
      response.push("12345")
    }
  }
}

function showAlert(message) {
  const wrapper = document.createElement('div')
  wrapper.innerHTML = '<div class="alert">' + message +'</div>'

  body.append(wrapper)

  setTimeout(() => {
    wrapper.parentNode.removeChild(wrapper)
  }, 3000)
}

function handleInsertCard(code, image) {
  let stores;

  if (localStorage.getItem('@e-fidelity:stores')) {
    stores = localStorage.getItem('@e-fidelity:stores').split(',')
  }

  if (stores != null) {
    if (stores.find(element => element == code)) {
      showAlert("Cartão fidelidade já adicionado!")
    } else {
      cards.innerHTML += image
      response.push(code)
  
      localStorage.setItem('@e-fidelity:stores', response)
    }
  } else {
    cards.innerHTML += image
    response.push(code)

    localStorage.setItem('@e-fidelity:stores', response)
  }
}

function validationInsertCard() {
  switch (code.value) {
    case "12":
      handleInsertCard("12", img3comLink)
      break
    case "123":
      handleInsertCard("123", img4comLink)
      break
    case "1234":
      handleInsertCard("1234", img3)
      break
    case "12345":
      handleInsertCard("12345", img4)
      break
    default:
      showAlert("Código inválido!", 'danger')
  }
}

form.addEventListener('submit', e => {
  e.preventDefault()

  validationInsertCard()
})

function getStoreName() {
  const buttonStore = document.querySelector('.card-body a')
  const storeName = buttonStore.innerHTML.slice(20, buttonStore.innerHTML.length)
  
  localStorage.setItem('@e-fidelity:storeName', storeName)
}
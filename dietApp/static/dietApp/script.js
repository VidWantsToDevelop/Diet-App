registerClicked = 0
loginClicked = 0
document.addEventListener('DOMContentLoaded', () => {
  //Initial variables
  let registerWrapper = document.querySelector('.wrapper-register1')
  let loginWrapper = document.querySelector('.wrapper-register2')
  let registerForm = document.querySelector('#button-register')
  let loginForm = document.querySelector('#button-login')
  let logoutButton = document.querySelector('#button-logout')
  let statisticsForm = document.querySelector('.statistics')

  //ArrowDown function (scroll the page)
  if (document.title === 'HI') {
    let arrowDown = document.querySelector('#arrowDown')
    arrowDown.addEventListener('click', () => {
      document.querySelector('.second-part').scrollIntoView()
    })
  }

  //Statistics change (depends of the date)
  if (statisticsForm) {
    const consumed = document.querySelector(
      '.statistics-consumed'
    ).firstElementChild
    const burnt = document.querySelector('.statistics-burnt').firstElementChild
    const fats = document.querySelector('.statistics-fats').firstElementChild
    const carbs = document.querySelector('.statistics-carbs').firstElementChild
    const proteins = document.querySelector(
      '.statistics-proteins'
    ).firstElementChild
    document.querySelectorAll('.button-date').forEach((btn) => {
      btn.addEventListener('click', () => {
        console.log('Date is chosen')
        const fetchDay = async () => {
          let respond = await renderDay(btn.id)
          if (respond) {
            consumed.innerHTML = respond.calories
            burnt.innerHTML = respond.burnt
            fats.innerHTML = respond.fats
            proteins.innerHTML = respond.proteins
            carbs.innerHTML = respond.carbs
          }
        }
        fetchDay()
      })
    })
  }

  //Checks user's authentication status
  if (logoutButton) {
    console.log('User has been authenticated')
  } else {
    console.log('User is not authenticated')
    //Register form animation
    registerForm.addEventListener('click', (e) => {
      e.preventDefault()
      float(registerWrapper, registerClicked)
      if (registerClicked === 0) {
        registerClicked = 1
      } else {
        registerClicked = 0
      }
    })

    //Login form animation
    loginForm.addEventListener('click', (e) => {
      e.preventDefault()
      float(loginWrapper, loginClicked)
      if (loginClicked === 0) {
        loginClicked = 1
      } else {
        loginClicked = 0
      }
    })
  }
})

//Functions
function float(el, clicked) {
  console.log(clicked)
  el.style.animation = 'none'
  el.offsetHeight /* trigger reflow */
  el.style.animation = null
  if (clicked === 0) {
    el.style.display = 'flex'
    el.style.animationDirection = 'normal'
    console.log(el.style.animationPlayState)
    el.style.animationPlayState = 'running'
    el.addEventListener('animationend', () => {
      console.log('ENDEd')
    })
    clicked = 1
  } else {
    el.style.animationDirection = 'reverse'
    console.log(el.style.animationDirection)
    el.style.animationPlayState = 'running'
    clicked = 0
  }
}

function renderDay(day) {
  return fetch(`http://127.0.0.1:8000/render_day/${day}`)
    .then((response) => response.json())
    .then((answer) => {
      return answer[0]
    })
}

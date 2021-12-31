registerClicked = 0
loginClicked = 0
document.addEventListener('DOMContentLoaded', () => {
  //Initial variables
  let registerWrapper = document.querySelector('.wrapper-register1')
  let loginWrapper = document.querySelector('.wrapper-register2')
  let registerForm = document.querySelector('#button-register')
  let loginForm = document.querySelector('#button-login')

  //ArrowDown function (scroll the page)
  if (document.title === 'HI') {
    let arrowDown = document.querySelector('#arrowDown')
    arrowDown.addEventListener('click', () => {
      document.querySelector('.second-part').scrollIntoView()
    })
  }

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

function changeDay(day) {}

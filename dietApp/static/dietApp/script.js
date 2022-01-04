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
  let plansBody = document.querySelectorAll('.plans-body')

  //ArrowDown function (scroll the page)
  if (document.title === 'HI') {
    let arrowDown = document.querySelector('#arrowDown')
    arrowDown.addEventListener('click', () => {
      document.querySelector('.second-part').scrollIntoView()
    })
  }

  //Statistics change (depends of the date)
  if (statisticsForm) {
    const historyBtn = document.querySelector('#button-history')
    const updateBtn = document.querySelector('#button-update')
    const consumed = document.querySelector(
      '.statistics-consumed'
    ).firstElementChild
    const burnt = document.querySelector('.statistics-burnt').firstElementChild
    const fats = document.querySelector('.statistics-fats').firstElementChild
    const carbs = document.querySelector('.statistics-carbs').firstElementChild
    const proteins = document.querySelector(
      '.statistics-proteins'
    ).firstElementChild
    const history2 = document.querySelector('.history-2')
    const historyPart = document.querySelector('.part-history')
    const updatePart = document.querySelector('.part-update')
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
        history2.style.animationPlayState = 'running'
      })
    })
    //Floating animation for the history and update bodies
    historyBtn.addEventListener('click', () => {
      historyPart.style.display = 'block'
      updatePart.style.display = 'none'
      historyPart.style.animationPlayState = 'running'
    })
    updateBtn.addEventListener('click', () => {
      updatePart.style.display = 'flex'
      historyPart.style.display = 'none'
      updatePart.style.animationPlayState = 'running'
    })
  }

  //Checks if it's a plans' page
  if (plansBody) {
    //Animations for the diet plans element
    document.querySelectorAll('.plan').forEach((el) => {
      el.firstElementChild.addEventListener('click', () => {
        planDeploy(el.lastElementChild)
      })
    })
    document.querySelectorAll('.btn').forEach((el) => {
      el.addEventListener('click', () => {
        let planDescription = el.previousElementSibling.innerText
        let planName =
          el.parentElement.parentElement.previousElementSibling.innerHTML
        console.log(planDescription)
        console.log(planName)
        addPlan(planName, planDescription)
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

function planDeploy(el) {
  let emptySpace = document.querySelector('.empty-space')
  el.style.animationPlayState = 'running'
  el.addEventListener('animationend', () => {
    el.parentElement.style.animationPlayState = 'running'
    el.firstElementChild.style.animationPlayState = 'running'
    emptySpace.style.height = '20vh'
    el.firstElementChild.lastElementChild.addEventListener('click', () => {
      el.firstElementChild.lastElementChild.style.animationPlayState = 'running'
      el.firstElementChild.lastElementChild.innerText = 'Done'
    })
    console.log('Ended')
  })
}

function renderDay(day) {
  return fetch(`http://127.0.0.1:8000/render_day/${day}`)
    .then((response) => response.json())
    .then((answer) => {
      return answer[0]
    })
}

function addPlan(planName, planDescription) {
  return fetch(`http://127.0.0.1:8000/addPlan/`, {
    method: 'POST',
    body: JSON.stringify({
      name: planName,
      description: planDescription,
    }),
  })
    .then((response) => response.json())
    .then((answer) => {
      console.log(answer)
    })
}

const menu = document.querySelector('.menu')
const close = document.querySelector('.close')
const mobileNav = document.querySelector('.mobile-nav')
const navLinks = document.querySelectorAll('.mobile-nav a')

menu.addEventListener('click', () => {
  mobileNav.classList.add('active')
})

close.addEventListener('click', () => {
  mobileNav.classList.remove('active')
})

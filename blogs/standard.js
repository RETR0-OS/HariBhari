const sections = document.querySelectorAll("section");
const navLi = document.querySelectorAll("nav .container-fluid .collapse .nav li");
window.addEventListener('scroll', () => {
  let current = "";

  sections.forEach((section) => {
    const sectionTop = section.offsetTop;
    if (pageYOffset >= (sectionTop - 60)) {
      current = section.getAttribute('id');
    }
  })
  navLi.forEach( li => {
    li.classList.remove("active");
    if (li.classList.contains(current)){
      li.classList.add("active");
    }
  })
})

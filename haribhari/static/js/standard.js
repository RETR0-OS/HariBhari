const sections = document.querySelectorAll("section");
const navLi = document.querySelectorAll("nav .container-fluid .collapse .navbar-nav li");
window.onload = (event) => {
  let current = "";

  sections.forEach((section) => {
    const sectionTop = section.offsetTop;
    if (pageYOffset >= (sectionTop - 400)) {
      current = section.getAttribute('id');
    }
  })
  navLi.forEach((li) => {
    li.classList.remove("active");
    if (li.classList.contains(current)){
      li.classList.add("active");
    }
    else
    {
      li.classList.remove("active");
    }
  })
};
window.addEventListener('scroll', () => {
  let current = "";
  sections.forEach((section) => {
    const sectionTop = section.offsetTop;
    if (pageYOffset >= (sectionTop - 700)) {
      current = section.getAttribute('id');
    }
  })
  navLi.forEach((li) => {
    li.classList.remove("active");
    if (li.classList.contains(current)){
      li.classList.add("active");
    }
    else
    {
      li.classList.remove("active");
    }
  })
})

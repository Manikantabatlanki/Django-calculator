window.onload=function(){
    console.log("Portifolio Loaded Successfully");
};

document.querySelectorAll('nav a').forEach(anchor =>{
    anchor.addEventListener('click',function(e){
        e.preventDefault();
document.querySelector(this.getAttribute('href')).scrollIntoView({behavior: 'smooth'});
    });
});
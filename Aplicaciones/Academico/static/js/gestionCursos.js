(function(){
    const btnEliminacion = document.querySelectorAll(".btnEliminacion");
btnEliminacion.forEach(btn=>{
    btn.addEventListener('click', (e)=>{
        const confirmacion = confirm('¿Seguro de Cancelar el Curso?')
        if(!confirmacion){
            e.preventDefault();
        }
    })
})
})();
const download=document.querySelector('.download')
const body = document.querySelector('body')
const getlink=()=>{
    try {
    $.ajax({
        type:'POST',
        url:'/link',
        data:{
            'url':document.querySelector('.input').value
        },
    })
    .done((e)=>{
        if(e=="Internel Server Error"){
            document.querySelector('body').innerHTML="<h2>Error!<h2>"
        }
        else{
        let newelem=document.createElement("div")
        newelem.classList.add('newelem')
        body.appendChild(newelem);
        const elem=document.querySelector('.newelem')
        elem.innerHTML=`<a href="${e} id="fgfuytyfy" download"></a>`
        document.querySelector(".newelem a").click()
        console.log(e)}
    })}
    catch{
        document.querySelector('body').innerHTML="<h2>Error!<h2>"
    }

}
download.addEventListener('click',getlink)
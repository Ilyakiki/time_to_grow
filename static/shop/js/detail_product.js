const description = document.getElementById('menu_text_left')
const structure = document.getElementById('menu_text_central')
const application=document.getElementById('menu_text_right')

const description_content=document.getElementsByClassName('description')[0]
const structure_content=document.getElementsByClassName('structure')[0]
const application_content=document.getElementsByClassName('method_of_application')[0]


description.addEventListener('click',function (){

    description.style.color='#409393'
    structure.style.color='#58CBCB'
    application.style.color='#58CBCB'
    description_content.style.display=''
    structure_content.style.display='none'
    application_content.style.display='none'

})

structure.addEventListener('click',function (){

    description.style.color='#58CBCB'
    structure.style.color='#409393'
    application.style.color='#58CBCB'
    description_content.style.display='none'
    structure_content.style.display=''
    application_content.style.display='none'
})

application.addEventListener('click',function (){

    description.style.color='#58CBCB'
    structure.style.color='#58CBCB'
    application.style.color='#409393'
    description_content.style.display='none'
    structure_content.style.display='none'
    application_content.style.display=''
})
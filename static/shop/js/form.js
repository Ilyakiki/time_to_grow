const next_step = document.getElementsByClassName('next')
const second_step= document.getElementsByClassName('second_step')[0]
const first_step=document.getElementsByClassName('first_step')[0]

next_step[0].addEventListener('click',function (){
    console.log('hi')
    second_step.style.display=''
    first_step.style.display='none'
})

const next_step = document.getElementsByClassName('next')[0]
const next_step_second=document.getElementsByClassName('next_step_second')[0]
const second_step= document.getElementsByClassName('second_step')[0]
const first_step=document.getElementsByClassName('first_step')[0]
const second_step_nav=document.getElementsByClassName('second_step_nav')[0]
const third_step_nav=document.getElementsByClassName('third_step_nav')[0]

const to_order=document.getElementsByClassName('to_order')[0]


sdek_map=document.getElementById('forpvz')
const method_of_delivery=document.getElementById('id_delivery_method_0')

method_of_delivery.addEventListener('click',function (){
    sdek_map.style.display=''
})

next_step.addEventListener('click',function (){
    second_step_nav.style.backgroundColor='white'
    third_step_nav.style.backgroundColor='#6478BD'

    first_step.style.display='none'
    second_step.style.display=''
})

next_step_second.addEventListener('click',function (){
    third_step_nav.style.backgroundColor='white'

    next_step_second.style.display='none'
    first_step.style.display=''
    next_step.style.display='none'
    to_order.style.display=''
})
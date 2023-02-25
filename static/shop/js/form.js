const next_step = document.getElementsByClassName('next')[0]
const next_step_second=document.getElementsByClassName('next_step_second')[0]
const second_step= document.getElementsByClassName('second_step')[0]
const first_step=document.getElementsByClassName('first_step')[0]
const second_step_nav=document.getElementsByClassName('second_step_nav')[0]
const third_step_nav=document.getElementsByClassName('third_step_nav')[0]

const to_order=document.getElementsByClassName('to_order')[0]


const sdek_map=document.getElementById('forpvz')
const method_of_delivery_PVZ=document.getElementById('id_delivery_method_0')
const method_of_delivery_CURIER=document.getElementById('id_delivery_method_1')

const adress_field=document.getElementsByClassName('adress')[0]

const card_pay=document.getElementById('id_method_of_payment_0')
card_pay.addEventListener('click',function (){
    alert('После оплаты обязательно нажмите "Вернуться в магазин"')
})
console.log(adress_field.style.display)

method_of_delivery_PVZ.addEventListener('click',function (){
    sdek_map.style.display=''
    adress_field.style.display='block'
})
method_of_delivery_CURIER.addEventListener('click',function (){
    sdek_map.style.display='none'
    adress_field.style.display='block'
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
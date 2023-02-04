console.log('Hi')
window.addEventListener('click',function (event){


    if (event.target.dataset.action === 'plus'){
        const CountWrapper = event.target.closest('.item_count_wrapper')
        const counter = CountWrapper.querySelector("input[type=number]")

        if (parseInt(counter.value)<20){
        counter.value= ++counter.value
        console.log(counter.value)}
    }

    if (event.target.dataset.action === 'minus'){
        const CountWrapper = event.target.closest('.item_count_wrapper')
        const counter = CountWrapper.querySelector("input[type=number]")
        if (parseInt(counter.value)>1){
        counter.value= --counter.value
        console.log(counter.value)}
    }
})

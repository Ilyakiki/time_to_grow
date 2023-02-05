
window.addEventListener('click',function (event){
    console.log(event.target)

    if (event.target.dataset.action === 'plus'){
        const CountWrapper = event.target.closest('.item_count_wrapper')
        const counter = CountWrapper.querySelector("input[type=number]")

        if (parseInt(counter.value)<20){
        counter.value= ++counter.value
        }
    }

    if (event.target.dataset.action === 'minus'){
        const CountWrapper = event.target.closest('.item_count_wrapper')
        const counter = CountWrapper.querySelector("input[type=number]")
        if (parseInt(counter.value)>1){
        counter.value= --counter.value
        }
    }
})

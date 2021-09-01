const url = window.location.href
const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const list = document.getElementById('list')
const listTitle = document.getElementById('list-title')
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
const listItem = document.createElement('div')
const b = document.createElement('b')
// const 
const divA = document.createElement('a')
const divP = document.createElement('p')

const sendSearchData = (post) => {
    $.ajax({
        type: 'POST',
        url: 'search',
        data: {
            'csrfmiddlewaretoken': csrf,
            'post': post,
        },
        success: (res)=> {
            console.log(res.data)
            const data = res.data
            if (Array.isArray(data)){
                console.log("We have array")
                console.log(data)
                list.innerHTML = ''
                if (searchInput.value.length > 0) {
                    data.forEach(e => {
                        var title = e.title
                        var text = e.text
                        var loc = e.pk
                        // divA.innerHTML = title 
                        // divP.innerHTML = text
                        // console.log(divP)
                        // listItem.appendChild = divA
                        // listItem.appendChild = divP
                        list.innerHTML += `<li><a href="${url}${loc}">${title}</a><br />${text}</li>`
                    }) 
                
                }
            }else{
                
                list.innerHTML = `<li><b>${data}</b></li>`
            };

        },
        error: (err)=> {
            console.log(err)
        }
    })
};

document.addEventListener("keyup", e=>{
    if (e.target.value != '') {
        listTitle.innerHTML = 'Search Results'
        sendSearchData(e.target.value)
    } else if (e.target.value == '') {
        listTitle.innerHTML = 'Popular Posts'
        list.innerHTML = '' 
        console.log(ata)
        const rdata = JSON.parse(ata.replace(/&quot;/g, '"'))
        console.log(rdata)
        rdata.forEach(d => {if (d) {
            var title = d.fields.title
            var text = d.fields.text 
            // divA.innerHTML = title 
            // divP.innerHTML = text
            // console.log(divP)
            // listItem.appendChild = divA
            // listItem.appendChild = divP
            list.innerHTML += `<li>${title}<br />${text}</li>`}
            else{
                list.innerHTML = 'No posts...'
            }
        });
    }

});
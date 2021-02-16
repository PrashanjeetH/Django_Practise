var className = document.getElementsByClassName('fetchClass')

function fetchData(){
  console.log('Requesting for resources...')

  var url = '/fetch/'

  fetch(url, {
    method: 'POST',
    headers:{
      'Content-Type':'application/json',
    },
    body:JSON.stringify({'PrashanjeetData in body'})
  })

  .then((response) =>{
    return response.json()
  })

  .then((data) =>{
    console.log('data:', data)
  })
}

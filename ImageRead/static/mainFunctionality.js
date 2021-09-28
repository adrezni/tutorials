

function fetchImage(){
    let url = "/getImage";
    postImageRequest(url)
        .then(serializedImage => displayImageHTML(serializedImage))
        .catch(error => console.error(error))
}
async function postImageRequest(url, formData){
    return fetch(url,{method: 'GET', body: formData})
        .then((response) => response.text());
}

function displayImageHTML(serializedImage){
    let imageContainerObj = document.getElementById("imageDivContainer");
    imageContainerObj.style.display = "block";
    let imageHTML = "<img src='data:image/png;base64, " + serializedImage +
        "' class='imgSize'/>"
    imageContainerObj.innerHTML = imageHTML;
}
const displayImageBtnObj = document.getElementById("displayImageBtn");
displayImageBtnObj.addEventListener("click", fetchImage);
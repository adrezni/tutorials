
// This function is activated when the user clicks on one of the radio buttons.  The
// param graphType identifies the type of graph.  Based on the param graphType
// the function shows/hides the appropriate input tags in the inputDiv
function refreshInputDiv(graphType){
    let inputDivObj = document.getElementById("inputDiv");
    inputDivObj.style.display = "block";
    let startSpanObj = document.getElementById("startSpan");
    let widthSpanObj = document.getElementById("widthSpan");
    let locSpanObj = document.getElementById("locSpan");
    let stdevSpanObj = document.getElementById("stdevSpan");
    let shapeSpanObj = document.getElementById("shapeSpan");

    startSpanObj.style.display = 'none';
    widthSpanObj.style.display = 'none';
    locSpanObj.style.display = 'none';
    stdevSpanObj.style.display = "none";
    shapeSpanObj.style.display = "none";

    switch(graphType){
        case "1":
            startSpanObj.style.display = "block";
            widthSpanObj.style.display = "block";
            break;
        case "2":
            locSpanObj.style.display =  "block";
            stdevSpanObj.style.display = "block";
            break;
        case "3":
            shapeSpanObj.style.display = "block";
            break;
        case "4":
            shapeSpanObj.style.display = "block";
    }
}

// This is an async call initiated by a click of the "Make Graph" button.  It makes an async call
// to the endpoint, /getDistributionGraph.  Once the response from the endpoint is received,
// the returned serialized image is placed into the UI by the displayGraphHTML() function
function makeGraph(){
    let url = "/getDistributionGraph";
    let formObj = document.getElementById("mainForm");
    let formData = new FormData(formObj);
    postGraphRequest(url, formData)
        .then(serializedImage => displayGraphHTML(serializedImage))
        .catch(error => console.error(error))
}
// Does the HTTPRequest to the endpoint given by the param, url.  The
// param formData is a dictionary that contains the values of all the input tags
// in the user interface.
async function postGraphRequest(url, formData){
    return fetch(url,{
        method: 'POST',
        body: formData
        })
        .then((response) => response.text());
}
// Takes the response from the param, serializedImage, builds an <img>
// tag that contains the serialized image, and assigns that <img>
// to the innerHTML attribute of the destination div.
function displayGraphHTML(serializedImage){
    let graphContainerObj = document.getElementById("graphContainer");
    graphContainerObj.style.display = "block";
    let graphHTML =  "<img src='data:image/png;base64, " + serializedImage +
        "' class='imgSize'/>" ;
    graphContainerObj.innerHTML = graphHTML;
}
// Add event listeners to radio buttons and to "Make Graph" button.

// Add EventListener to button.  The event is "click" and the listener is the
// function, makeGraph:
const makeGraphBtnObj = document.getElementById("makeGraphBtn");
makeGraphBtnObj.addEventListener("click", makeGraph);

// click event for radio buttons
// Listener for each radio buttons is the function refreshInputDiv(graphType)
const radioBtnsListObj = document.querySelectorAll('input[type=radio][name="graphType"]');
radioBtnsListObj.forEach(radio =>
                radio.addEventListener('click', () => refreshInputDiv(radio.value)));
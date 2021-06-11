const contentsList = document.getElementById("contentsList");
const searchTerm = document.getElementById("searchTerm");
const searchButton = document.getElementById("searchButton");
const loadWrapper = document.getElementById("loadWrapper");
const elasticPass = "FE0Yrg2pU5jxf0Ea7V7a5d5l";
const cloud_id = "";
let hpCharacters = [];
let loadFlag = false;
let emptyFlag = false;
let errorFlag = true;

searchTerm.addEventListener("keyup", (e) => {
    e.preventDefault();
    if (e.code === "Enter") {
        searchButton.click();
    }
});

searchButton.onclick = () => {
    contentsList.innerHTML = "";
    displayLoad();
    searchQuery(searchTerm.value)
        .then((data) => {
            console.log(data);
            console.log(resultFormatter(data));
            let results = resultFormatter(data);
            if (results) {
                loadWrapper.innerHTML = "";
                displayContents(results);
            } else {
                loadWrapper.innerHTML = "";
                displayEmpty();
            }
        })
        .catch((err) => {
            loadWrapper.innerHTML = "";
            displayError(err);
        });
};

const displayLoad = () => {
    const loadHtmlString = `<div class="lds-ripple"><div></div><div></div></div>`;
    loadWrapper.innerHTML = loadHtmlString;
};

const displayEmpty = () => {
    const emptyHtmlString = `<li class="contentBox">
                <h2 class="titleLink">No Result</h2>
                <h5 class="urlLink"></h5>
                <p class="description"></p>
            </li>`;
    contentsList.innerHTML = emptyHtmlString;
};

const displayError = (err) => {
    console.log(err);
    const errorHtmlString = `<li class="contentBox" class="errorBox">
    <h2 class="titleLink">Error while searching</h2>
    <h5 class="urlLink"></h5>
    <p class="description">${err}</p>
    </li>`;
    contentsList.innerHTML = errorHtmlString;
};

const displayContents = (contents) => {
    const htmlString = contents
        .map((content) => {
            return `
            <li class="contentBox">
                <h2 class="titleLink"><a href=${content.url}>${
                content["page_title"]
            }</a></h2>
                <h5 class="urlLink">${content.url}</h5>
                <p class="description">${content.text.substr(
                    content.text.indexOf(searchTerm.value),
                    400
                )}</p>
            </li>
        `;
        })
        .join("");
    contentsList.innerHTML = htmlString;
};

const resultFormatter = (result) => {
    let tempArr = [];
    if (!result) {
        return false;
    }
    if (result.hits.hits.length) {
        result.hits.hits.map((item) => {
            tempArr.push(item["_source"]);
        });
        return tempArr;
    } else {
        return null;
    }
};

async function searchQuery(query) {
    const response = await fetch(
        "https://cs172-project-ad1cfb.es.eastus2.azure.elastic-cloud.com:9243/edusite/_search",
        {
            method: "POST",
            // mode: "no-cors",
            headers: {
                "Content-Type": "application/json",
                Authorization:
                    "Basic ZWxhc3RpYzpGRTBZcmcycFU1anhmMEVhN1Y3YTVkNWw=",
            },
            body: JSON.stringify({
                query: {
                    match: { text: query },
                },
            }),
        }
    );
    return response.json();
}

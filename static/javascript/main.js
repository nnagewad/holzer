const cityRefresh = refresh();
const countryRefresh = refresh();

function refresh() {
    return Math.floor(Math.random() * 10000) + 1;
}

setInterval(randomCity, cityRefresh);

setInterval(randomCountry, countryRefresh);

function randomCity() {
    document.getElementById("city").innerHTML = randomGenerator(cities);
}

function randomCountry() {
    document.getElementById("country").innerHTML = randomGenerator(countries);
}

function randomGenerator(x) {
    return x[Math.floor(Math.random()*x.length)];
}
//Initalize variables and shop
let rats = 10000000000;
let killmulti = 1;
let cash = 0;
let cashmulti = 1;
let clickmulti = 1;
let shop = {
    "citizen": { lvl: 0, price: 10, factor: 1.5, rate: 1, id: 1 },
    "boot": { lvl: 0, price: 50, factor: 1.5, rate: 5, id: 2, },
    "dennis": { lvl: 0, price: 250, factor: 1.5, rate: 25, id: 3 },
    "rpg": { lvl: 0, price: 1000, factor: 1.75, rate: 100, id: 4 },
    "basic": {lvl: 0, price: 10000, factor: 2, rate: 1000, id: 5},
    "cool": { lvl: 0, price: 50000, factor: 2.25, rate: 2500, id: 6 },
    "great": { lvl: 0, price: 100000, factor: 2.25, rate: 10000, id: 7 },
    "amazing": { lvl: 0, price: 500000, factor: 2.25, rate: 25000, id: 8 },
    "bigger": { lvl: 0, price: 1000, factor: 5, id: 9 },
    "fearmon": { lvl: 0, price: 500, factor: 5, id: 10 },
    "click": { lvl: 0, price: 1000, factor: 10, id: 11, max: 3 },
    "humon": { lvl: 0, price: 1000000, factor: 100, id: 12, max: 2 }
};

//Function for calculating how many rats should be subtracted and how much cash should be added
function subtractrats(manual, specrate) {
    if (rats <= 0) {
        window.location.replace("winner.html");
    }
    if (manual == false) {
        rats -= specrate * killmulti;
        cash += specrate * cashmulti * killmulti;
    }
    else {
        rats -= clickmulti * killmulti;
        cash += clickmulti * cashmulti * killmulti;
        playratnoise();
    }
    document.getElementById('ratcount').innerHTML = 'Rats: ' + numberWithCommas(rats)
    document.getElementById('cashcount').innerHTML = 'Cash: $' + numberWithCommas(cash)

}

//Formats inputted numbers with commas
function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

//Rolls a random number and plays that sound
function playratnoise() {
    let rarechance = 15;
    let soundchoose = Math.floor((Math.random() * rarechance) + 1);
    if (soundchoose <= rarechance - 1) {
        soundchoose = Math.floor((Math.random() * 15) + 1);
        var ratnoise = new Audio(src = 'sounds/rat' + soundchoose + '.mp3');
    }
    else {
        soundchoose = Math.floor((Math.random() * 2) + 16);
        var ratnoise = new Audio(src = 'sounds/rat' + soundchoose + '.mp3');
    }
    ratnoise.play();
}

// When the user attempts to buy an upgrade, this updates all corresponding values and changes the HTML
function upgrade(purchase) {
    if (cash >= purchase['price']) {
        let id = purchase['id']
        purchase['lvl']++;
        cash -= purchase['price'];
        purchase['price'] = scaleprice(purchase['factor'], purchase['price']);
        document.getElementById('level' + id).innerHTML = 'Own: ' + purchase['lvl']
        document.getElementById('cost' + id).innerHTML = '$' + numberWithCommas(purchase['price'])
        document.getElementById('cashcount').innerHTML = 'Cash: $' + numberWithCommas(cash)
        if (id <= 8) {
            var helpers = setInterval(subtractrats, 1000, false, purchase['rate']);
        }
        else {
            if (id == 9) {
                killmulti++;
            }
            if (id == 10) {
                cashmulti++;
            }
            if (id == 11) {
                clickmulti = clickmulti * 10;
            }
            if (id == 12) {
                killmulti = killmulti * 10;
            }
        }
        if (purchase['lvl'] >= purchase['max']) {
            document.getElementById('cost' + id).innerHTML = '\0'
            document.getElementById('level' + id).innerHTML = 'MAX!'
            const element = document.getElementById('btn' + id);
            element.remove();
        }
    }
}

// After a purchase, this calculates the new price of the upgrade
function scaleprice(factor, current) {
    current = current * factor;
    current = (Math.floor(current / 5) * 5);
    return current;
}

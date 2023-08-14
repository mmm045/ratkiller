let rats = 10000000000;
            let killmulti = 1;
            let cash = 0;
            let cashmulti = 1;
            let shop = {
                "ratkill": {lvl: 1, price: 1, id: 'raki'},
                "fearmon": {lvl: 1, price: 1, id: 'fear'}
            };
            function subtractrats()
            {
	            rats -= 1 * killmulti;
                cash += 1 * cashmulti * killmulti;
	            document.getElementById('ratcount').innerHTML = 'Rats: ' + numberWithCommas(rats)
                document.getElementById('cashcount').innerHTML = 'Cash: $' + numberWithCommas(cash)
                playratnoise();
            }

            function numberWithCommas(x) 
            {
                return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
            }
            
            function playratnoise()
            {
                let soundchoose = Math.floor((Math.random() * 7) + 1);
                var ratnoise = new Audio(src='rat' + soundchoose + '.mp3');
                ratnoise.play();
            }

            function ratkilup()
            {
                if (cash >= 5)
                {
                    killmulti++;
                    cash -= 5;
                    document.getElementById('cashcount').innerHTML = 'Cash: $' + numberWithCommas(cash)
                }
            }
            
            function cashup()
            {
                cashmulti++;
                document.getElementById('cashcount').innerHTML = 'Cash: $' + numberWithCommas(cash)
            }

            function upgrade(purchase)
            {
                let id = purchase['id']
                if (cash >= purchase['price'])
                {
                    purchase['lvl']++;
                    cash -= purchase['price'];
                    document.getElementById('level').innerHTML = 'Lvl: ' + purchase['lvl']
                    document.getElementById('cost').innerHTML = '$' + purchase['price']
                    document.getElementById('cashcount').innerHTML = 'Cash: $' + numberWithCommas(cash)
                    if (id == 'raki'){
                        killmulti++;
                    }
                    if (id == 'fear'){
                        cashmulti++;
                    }
                }
            }
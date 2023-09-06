var playerValue = 0;
var dealerValue = 0;
var cardIdList = [];
var gameOver = false;
var dealerAceCount = 0;
var playerAceCount = 0;
var cardIdToCard = {
    1: {
        cardName: "2 of Clubs",
        cardValue: 2,
        cardImagePath: "/static/2_of_clubs.png"
    },

    2: {
        cardName: "2 of Diamonds",
        cardValue: 2,
        cardImagePath: "/static/2_of_diamonds.png"
    },

    3: {
        cardName: "2 of Hearts",
        cardValue: 2,
        cardImagePath: "/static/2_of_hearts.png"
    },

    4: {
        cardName: "2 of Spades",
        cardValue: 2,
        cardImagePath: "/static/2_of_spades.png"
    },

    5: {
        cardName: "3 of Clubs",
        cardValue: 3,
        cardImagePath: "/static/3_of_clubs.png"
    },

    6: {
        cardName: "3 of Diamonds",
        cardValue: 3,
        cardImagePath: "/static/3_of_diamonds.png"
    },

    7: {
        cardName: "3 of Hearts",
        cardValue: 3,
        cardImagePath: "/static/3_of_hearts.png"
    },

    8: {
        cardName: "3 of Spades",
        cardValue: 3,
        cardImagePath: "/static/3_of_spades.png"
    },

    9: {
        cardName: "4 of Clubs",
        cardValue: 4,
        cardImagePath: "/static/4_of_clubs.png"
    },

    10: {
        cardName: "4 of Diamonds",
        cardValue: 4,
        cardImagePath: "/static/4_of_diamonds.png"
    },

    11: {
        cardName: "4 of Hearts",
        cardValue: 4,
        cardImagePath: "/static/4_of_hearts.png"
    },

    12: {
        cardName: "4 of Spades",
        cardValue: 4,
        cardImagePath: "/static/4_of_spades.png"
    },

    13: {
        cardName: "5 of Clubs",
        cardValue: 5,
        cardImagePath: "/static/5_of_clubs.png"
    },

    14: {
        cardName: "5 of Diamonds",
        cardValue: 5,
        cardImagePath: "/static/5_of_diamonds.png"
    },

    15: {
        cardName: "5 of Hearts",
        cardValue: 5,
        cardImagePath: "/static/5_of_hearts.png"
    },

    16: {
        cardName: "5 of Spades",
        cardValue: 5,
        cardImagePath: "/static/5_of_spades.png"
    },

    17: {
        cardName: "6 of Clubs",
        cardValue: 6,
        cardImagePath: "/static/6_of_clubs.png"
    },

    18: {
        cardName: "6 of Diamonds",
        cardValue: 6,
        cardImagePath: "/static/6_of_diamonds.png"
    },

    19: {
        cardName: "6 of Hearts",
        cardValue: 6,
        cardImagePath: "/static/6_of_hearts.png"
    },

    20: {
        cardName: "6 of Spades",
        cardValue: 6,
        cardImagePath: "/static/6_of_spades.png"
    },

    21: {
        cardName: "7 of Clubs",
        cardValue: 7,
        cardImagePath: "/static/7_of_clubs.png"
    },

    22: {
        cardName: "7 of Diamonds",
        cardValue: 7,
        cardImagePath: "/static/7_of_diamonds.png"
    },

    23: {
        cardName: "7 of Hearts",
        cardValue: 7,
        cardImagePath: "/static/7_of_hearts.png"
    },

    24: {
        cardName: "7 of Spades",
        cardValue: 7,
        cardImagePath: "/static/7_of_spades.png"
    },

    25: {
        cardName: "8 of Clubs",
        cardValue: 8,
        cardImagePath: "/static/8_of_clubs.png"
    },

    26: {
        cardName: "8 of Diamonds",
        cardValue: 8,
        cardImagePath: "/static/8_of_diamonds.png"
    },

    27: {
        cardName: "8 of Hearts",
        cardValue: 8,
        cardImagePath: "/static/8_of_hearts.png"
    },

    28: {
        cardName: "8 of Spades",
        cardValue: 8,
        cardImagePath: "/static/8_of_spades.png"
    },

    29: {
        cardName: "9 of Clubs",
        cardValue: 9,
        cardImagePath: "/static/9_of_clubs.png"
    },

    30: {
        cardName: "9 of Diamonds",
        cardValue: 9,
        cardImagePath: "/static/9_of_diamonds.png"
    },

    31: {
        cardName: "9 of Hearts",
        cardValue: 9,
        cardImagePath: "/static/9_of_hearts.png"
    },

    32: {
        cardName: "9 of Spades",
        cardValue: 9,
        cardImagePath: "/static/9_of_spades.png"
    },

    33: {
        cardName: "10 of Clubs",
        cardValue: 10,
        cardImagePath: "/static/10_of_clubs.png"
    },

    34: {
        cardName: "10 of Diamonds",
        cardValue: 10,
        cardImagePath: "/static/10_of_diamonds.png"
    },

    35: {
        cardName: "10 of Hearts",
        cardValue: 10,
        cardImagePath: "/static/10_of_hearts.png"
    },

    36: {
        cardName: "10 of Spades",
        cardValue: 10,
        cardImagePath: "/static/10_of_spades.png"
    },

    37: {
        cardName: "Ace of Clubs",
        cardValue: 11,
        cardImagePath: "/static/ace_of_clubs.png"
    },

    38: {
        cardName: "Ace of Diamonds",
        cardValue: 11,
        cardImagePath: "/static/ace_of_diamonds.png"
    },

    39: {
        cardName: "Ace of Hearts",
        cardValue: 11,
        cardImagePath: "/static/ace_of_hearts.png"
    },

    40: {
        cardName: "Ace of Spades",
        cardValue: 11,
        cardImagePath: "/static/ace_of_spades.png"
    },

    41: {
        cardName: "Jack of Clubs",
        cardValue: 10,
        cardImagePath: "/static/jack_of_clubs.png"
    },

    42: {
        cardName: "Jack of Diamonds",
        cardValue: 10,
        cardImagePath: "/static/jack_of_diamonds.png"
    },

    43: {
        cardName: "Jack of Hearts",
        cardValue: 10,
        cardImagePath: "/static/jack_of_hearts.png"
    },

    44: {
        cardName: "Jack of Spades",
        cardValue: 10,
        cardImagePath: "/static/jack_of_spades.png"
    },

    45: {
        cardName: "King of Clubs",
        cardValue: 10,
        cardImagePath: "/static/king_of_clubs.png"
    },

    46: {
        cardName: "King of Diamonds",
        cardValue: 10,
        cardImagePath: "/static/king_of_diamonds.png"
    },

    47: {
        cardName: "King of Hearts",
        cardValue: 10,
        cardImagePath: "/static/king_of_hearts.png"
    },

    48: {
        cardName: "King of Spades",
        cardValue: 10,
        cardImagePath: "/static/king_of_spades.png"
    },

    49: {
        cardName: "Queen of Clubs",
        cardValue: 10,
        cardImagePath: "/static/queen_of_clubs.png"
    },

    50: {
        cardName: "Queen of Diamonds",
        cardValue: 10,
        cardImagePath: "/static/queen_of_diamonds.png"
    },

    51: {
        cardName: "Queen of Heats",
        cardValue: 10,
        cardImagePath: "/static/queen_of_hearts.png"
    },

    52: {
        cardName: "Queen of Spades",
        cardValue: 10,
        cardImagePath: "/static/queen_of_spades.png"
    }
}
var card_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
var index = 0
var dealerBlackJack = false
var playerBlackJack = false

document.getElementById("hit-button").addEventListener('click', function () {
    displayCard("playingArea")
});

document.getElementById("stand-button").addEventListener('click', function () {
    dealer()
});
document.getElementById("restart-button").addEventListener('click', function () {
    initializeGame()
});
document.getElementById("hint-button").addEventListener('click', function () {
    hint()
});


function hint(){
    // send player total and dealer card backto here, then find index, then go through model table and find 0 or 1. If 1, recommend hit. If 0, recommend stand.
    alert("Here's your hint!")
    return;
}   


function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array
}
function displayCard(area, firstCard) {
    if (gameOver) {
        return
    }
    current_card = card_list[index]
    index += 1
    const newCard = document.createElement("img");
    newCard.src = cardIdToCard[current_card].cardImagePath
    newCard.setAttribute("data-src", "/static/back_of_card.png")
    newCard.width = 200
    document.getElementById(area).appendChild(newCard);
    if (area == "dealerArea") {
        dealerValue += cardIdToCard[current_card].cardValue
        if (cardIdToCard[current_card].cardValue === 11) {
            dealerAceCount += 1
        }
        if (dealerValue > 21) {
            if (dealerAceCount > 0) {
                dealerValue -= 10
                dealerAceCount -= 1
            }
            else {
                stopGame()
            }
        }
    }
    if (area == "playingArea") {
        playerValue += cardIdToCard[current_card].cardValue
        if (cardIdToCard[current_card].cardValue === 11) {
            playerAceCount += 1
        }
        if (playerValue > 21) {
            if (playerAceCount > 0) {
                playerValue -= 10
                playerAceCount -= 1

            }
            else {
                stopGame()
            }
        }
    }
    if (firstCard) {
        newCard.id = "firstCard"
        flip()
    }
    return current_card
}
async function stopGame() {
    gameOver = true;
    document.getElementById("hit-button").disabled = true;
    document.getElementById("stand-button").disabled = true;
    await new Promise(r => setTimeout(r, 1000))
    document.getElementById("restart-button").classList.remove("no-display");
    if (playerBlackJack && dealerBlackJack) {
        alert("Player and dealer blackjack! It's a tie!")
        return;
    }

    if (playerBlackJack && !dealerBlackJack) {
        alert("Black Jack! You Win!")
        return;
    }

    if (dealerBlackJack && !playerBlackJack) {
        alert("Dealer has BlackJack. You lose!!!")
        return;
    }

    if (playerValue > 21) {
        flip()
        await new Promise(r => setTimeout(r, 1000))
        alert("YOU BUST!!!!!! YOU LOSE!!")
        return;
    }

    if (dealerValue > 21) {
        alert("Dealer Bust! YOU WIN!!!")
        return;
    }

    if (playerValue > dealerValue) {
        alert("YOU WINNNN!!!")
        return;
    }

    if (dealerValue === playerValue) {
        alert("YOU TIE!!!!")
        return;
    }

    if (dealerValue > playerValue) {
        alert("YOU LOSEEEE!")
        return;
    }

}
async function initializeGame() {
    document.getElementById("restart-button").classList.add("no-display");
    playerValue = 0;
    dealerValue = 0;
    dealerAceCount = 0;
    playerAceCount = 0;
    gameOver = false;
    playerBlackJack = false
    dealerBlackJack = false
    document.getElementById("dealerArea").innerHTML = "";
    document.getElementById("playingArea").innerHTML = "";
    index = 0
    card_list = shuffle(card_list)
    for (let i = 0; i < 2; i++) {
        await new Promise(r => setTimeout(r, 200))
        displayCard("dealerArea", i === 0)
        console.log(i);
        console.log('dealerArea')
    }
    for (let i = 0; i < 2; i++) {
        await new Promise(r => setTimeout(r, 200))
        displayCard("playingArea")
    }

    setTimeout(function () {
        document.getElementById("playButtons").classList.remove("hidden");
    }, 800)

    if (playerValue === 21 || dealerValue === 21) {
        if (playerValue === 21) {
            playerBlackJack = true
        }
    
        if (dealerValue === 21) {
            await new Promise(r => setTimeout(r, 200))
            dealerBlackJack = true
        }
        flip()
        stopGame()
        return;
    }

    document.getElementById("hit-button").disabled = false;
    document.getElementById("stand-button").disabled = false;

}
function flip() {
    var original_src = document.getElementById("firstCard").src
    document.getElementById("firstCard").src = document.getElementById("firstCard").getAttribute("data-src")
    document.getElementById("firstCard").setAttribute("data-src", original_src)
}
async function dealer() {
    document.getElementById("hit-button").disabled = true;
    document.getElementById("stand-button").disabled = true;
    flip()
    await new Promise(r => setTimeout(r, 1000))
    while (dealerValue < 17) {
        displayCard("dealerArea", false)
        await new Promise(r => setTimeout(r, 1000))
    }
    if (dealerValue <= 21) {
        stopGame()
    }
}

initializeGame()


// if player blackjacks dealer should check blackjack but not get anymore cards
var playerValue = 0;
var dealerValue = 0;
var cardIdList = [];
var gameOver = false;
var dealerAceCount = 0;
var playerAceCount = 0;
var dealerCard = 0;
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
var preDealer = true

document.getElementById("hit-button").addEventListener('click', function () {
    displayCard("playingArea")
});

document.getElementById("stand-button").addEventListener('click', function () {
    dealer()
});
document.getElementById("restart-button").addEventListener('click', function () {
    initializeGame()
    updateDealerTotalElement(preDealer)
    updatePlayerTotalElement()
});
document.getElementById("hint-button").addEventListener('click', function () {
    hint(playerValue, playerAceCount, dealerCard)
});

document.getElementById("counter-button").addEventListener('click', function () {
    var playerTotalElement = document.getElementById("player-total");
    var dealerTotalElement = document.getElementById("dealer-total");
    if (playerTotalElement.style.visibility == "hidden") {
        playerTotalElement.style.visibility = "";
        dealerTotalElement.style.visibility = "";
        document.getElementById("counter-button").innerText = "Hide Card Totals"
        updatePlayerTotalElement();
        updateDealerTotalElement(preDealer);
    } else {
        playerTotalElement.style.visibility = "hidden";
        dealerTotalElement.style.visibility = "hidden";
        document.getElementById("counter-button").innerText = "Show Card Totals"
    }

});

function updatePlayerTotalElement() {
    var playerTotalElement = document.getElementById("player-total");
    playerTotalElement.innerHTML = "Player Total: " + playerValue;
}

function updateDealerTotalElement(preDealer){
    var dealerTotalElement = document.getElementById("dealer-total");
    console.log('ooga booga')
    if (preDealer){
        dealerTotalElement.innerHTML = "Dealer Total: " + dealerCard;
    }
    else{
        dealerTotalElement.innerHTML = "Dealer Total: " + dealerValue;
    }
    

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
        updateDealerTotalElement(preDealer)
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
        updatePlayerTotalElement()
    }
    if (firstCard) {
        newCard.id = "firstCard"
        flip()
    }
    else if (!firstCard && area == "dealerArea"){
        updateDealerTotalElement(preDealer)
    }
    return cardIdToCard[current_card].cardValue
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
        preDealer = false
        updateDealerTotalElement(preDealer)
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
    preDealer = true
    document.getElementById("hint-button").disabled = true;
    document.getElementById("restart-button").classList.add("no-display");
    playerValue = 0;
    dealerValue = 0;
    dealerCard = 0;
    dealerAceCount = 0;
    playerAceCount = 0;
    gameOver = false;
    playerBlackJack = false
    dealerBlackJack = false
    document.getElementById("dealerArea").innerHTML = "";
    document.getElementById("playingArea").innerHTML = "";
    index = 0
    card_list = shuffle(card_list)
    // for (let i = 0; i < 2; i++) {
    await new Promise(r => setTimeout(r, 800))
    displayCard("dealerArea", true)
    await new Promise(r => setTimeout(r, 800))
    dealerCard = displayCard("dealerArea", false)
    updateDealerTotalElement(preDealer)
    // console.log(i);
    // console.log('dealerArea')
    // }
    for (let i = 0; i < 2; i++) {
        await new Promise(r => setTimeout(r, 800))
        displayCard("playingArea")
    }

    setTimeout(function () {
        document.getElementById("playButtons").classList.remove("hidden");
    }, 800)

    document.getElementById("hit-button").disabled = false;
    document.getElementById("stand-button").disabled = false;
    document.getElementById("hint-button").disabled = false;

    if (playerValue === 21 || dealerValue === 21) {
        if (playerValue === 21) {
            playerBlackJack = true
        }
    
        if (dealerValue === 21) {
            dealerBlackJack = true
        }
        flip()
        preDealer = false
        updateDealerTotalElement(preDealer)
        stopGame()
    }
    

    return dealerCard;
}
function hint(playerValue, playerAceCount, dealerCard) {
    // send player total and dealer card backto here, then find index, then go through model table and find 0 or 1. If 1, recommend hit. If 0, recommend stand.
    scenarioID = [1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    //dealerCard = initializeGame()
    scenarioIDToScenarioNoAce = {
        0: {'playerTotal': 4, 'dealerCard': 2},
        1: {'playerTotal': 4, 'dealerCard': 3},
        2: {'playerTotal': 4, 'dealerCard': 4},
        3: {'playerTotal': 4, 'dealerCard': 5},
        4: {'playerTotal': 4, 'dealerCard': 6},
        5: {'playerTotal': 4, 'dealerCard': 7},
        6: {'playerTotal': 4, 'dealerCard': 8},
        7: {'playerTotal': 4, 'dealerCard': 9},
        8: {'playerTotal': 4, 'dealerCard': 10},
        9: {'playerTotal': 4, 'dealerCard': 11},
        10: {'playerTotal': 5, 'dealerCard': 2},
        11: {'playerTotal': 5, 'dealerCard': 3},
        12: {'playerTotal': 5, 'dealerCard': 4},
        13: {'playerTotal': 5, 'dealerCard': 5},
        14: {'playerTotal': 5, 'dealerCard': 6},
        15: {'playerTotal': 5, 'dealerCard': 7},
        16: {'playerTotal': 5, 'dealerCard': 8},
        17: {'playerTotal': 5, 'dealerCard': 9},
        18: {'playerTotal': 5, 'dealerCard': 10},
        19: {'playerTotal': 5, 'dealerCard': 11},
        20: {'playerTotal': 6, 'dealerCard': 2},
        21: {'playerTotal': 6, 'dealerCard': 3},
        22: {'playerTotal': 6, 'dealerCard': 4},
        23: {'playerTotal': 6, 'dealerCard': 5},
        24: {'playerTotal': 6, 'dealerCard': 6},
        25: {'playerTotal': 6, 'dealerCard': 7},
        26: {'playerTotal': 6, 'dealerCard': 8},
        27: {'playerTotal': 6, 'dealerCard': 9},
        28: {'playerTotal': 6, 'dealerCard': 10},
        29: {'playerTotal': 6, 'dealerCard': 11},
        30: {'playerTotal': 7, 'dealerCard': 2},
        31: {'playerTotal': 7, 'dealerCard': 3},
        32: {'playerTotal': 7, 'dealerCard': 4},
        33: {'playerTotal': 7, 'dealerCard': 5},
        34: {'playerTotal': 7, 'dealerCard': 6},
        35: {'playerTotal': 7, 'dealerCard': 7},
        36: {'playerTotal': 7, 'dealerCard': 8},
        37: {'playerTotal': 7, 'dealerCard': 9},
        38: {'playerTotal': 7, 'dealerCard': 10},
        39: {'playerTotal': 7, 'dealerCard': 11},
        40: {'playerTotal': 8, 'dealerCard': 2},
        41: {'playerTotal': 8, 'dealerCard': 3},
        42: {'playerTotal': 8, 'dealerCard': 4},
        43: {'playerTotal': 8, 'dealerCard': 5},
        44: {'playerTotal': 8, 'dealerCard': 6},
        45: {'playerTotal': 8, 'dealerCard': 7},
        46: {'playerTotal': 8, 'dealerCard': 8},
        47: {'playerTotal': 8, 'dealerCard': 9},
        48: {'playerTotal': 8, 'dealerCard': 10},
        49: {'playerTotal': 8, 'dealerCard': 11},
        50: {'playerTotal': 9, 'dealerCard': 2},
        51: {'playerTotal': 9, 'dealerCard': 3},
        52: {'playerTotal': 9, 'dealerCard': 4},
        53: {'playerTotal': 9, 'dealerCard': 5},
        54: {'playerTotal': 9, 'dealerCard': 6},
        55: {'playerTotal': 9, 'dealerCard': 7},
        56: {'playerTotal': 9, 'dealerCard': 8},
        57: {'playerTotal': 9, 'dealerCard': 9},
        58: {'playerTotal': 9, 'dealerCard': 10},
        59: {'playerTotal': 9, 'dealerCard': 11},
        60: {'playerTotal': 10, 'dealerCard': 2},
        61: {'playerTotal': 10, 'dealerCard': 3},
        62: {'playerTotal': 10, 'dealerCard': 4},
        63: {'playerTotal': 10, 'dealerCard': 5},
        64: {'playerTotal': 10, 'dealerCard': 6},
        65: {'playerTotal': 10, 'dealerCard': 7},
        66: {'playerTotal': 10, 'dealerCard': 8},
        67: {'playerTotal': 10, 'dealerCard': 9},
        68: {'playerTotal': 10, 'dealerCard': 10},
        69: {'playerTotal': 10, 'dealerCard': 11},
        70: {'playerTotal': 11, 'dealerCard': 2},
        71: {'playerTotal': 11, 'dealerCard': 3},
        72: {'playerTotal': 11, 'dealerCard': 4},
        73: {'playerTotal': 11, 'dealerCard': 5},
        74: {'playerTotal': 11, 'dealerCard': 6},
        75: {'playerTotal': 11, 'dealerCard': 7},
        76: {'playerTotal': 11, 'dealerCard': 8},
        77: {'playerTotal': 11, 'dealerCard': 9},
        78: {'playerTotal': 11, 'dealerCard': 10},
        79: {'playerTotal': 11, 'dealerCard': 11},
        80: {'playerTotal': 12, 'dealerCard': 2},
        81: {'playerTotal': 12, 'dealerCard': 3},
        82: {'playerTotal': 12, 'dealerCard': 4},
        83: {'playerTotal': 12, 'dealerCard': 5},
        84: {'playerTotal': 12, 'dealerCard': 6},
        85: {'playerTotal': 12, 'dealerCard': 7},
        86: {'playerTotal': 12, 'dealerCard': 8},
        87: {'playerTotal': 12, 'dealerCard': 9},
        88: {'playerTotal': 12, 'dealerCard': 10},
        89: {'playerTotal': 12, 'dealerCard': 11},
        90: {'playerTotal': 13, 'dealerCard': 2},
        91: {'playerTotal': 13, 'dealerCard': 3},
        92: {'playerTotal': 13, 'dealerCard': 4},
        93: {'playerTotal': 13, 'dealerCard': 5},
        94: {'playerTotal': 13, 'dealerCard': 6},
        95: {'playerTotal': 13, 'dealerCard': 7},
        96: {'playerTotal': 13, 'dealerCard': 8},
        97: {'playerTotal': 13, 'dealerCard': 9},
        98: {'playerTotal': 13, 'dealerCard': 10},
        99: {'playerTotal': 13, 'dealerCard': 11},
        100: {'playerTotal': 14, 'dealerCard': 2},
        101: {'playerTotal': 14, 'dealerCard': 3},
        102: {'playerTotal': 14, 'dealerCard': 4},
        103: {'playerTotal': 14, 'dealerCard': 5},
        104: {'playerTotal': 14, 'dealerCard': 6},
        105: {'playerTotal': 14, 'dealerCard': 7},
        106: {'playerTotal': 14, 'dealerCard': 8},
        107: {'playerTotal': 14, 'dealerCard': 9},
        108: {'playerTotal': 14, 'dealerCard': 10},
        109: {'playerTotal': 14, 'dealerCard': 11},
        110: {'playerTotal': 15, 'dealerCard': 2},
        111: {'playerTotal': 15, 'dealerCard': 3},
        112: {'playerTotal': 15, 'dealerCard': 4},
        113: {'playerTotal': 15, 'dealerCard': 5},
        114: {'playerTotal': 15, 'dealerCard': 6},
        115: {'playerTotal': 15, 'dealerCard': 7},
        116: {'playerTotal': 15, 'dealerCard': 8},
        117: {'playerTotal': 15, 'dealerCard': 9},
        118: {'playerTotal': 15, 'dealerCard': 10},
        119: {'playerTotal': 15, 'dealerCard': 11},
        120: {'playerTotal': 16, 'dealerCard': 2},
        121: {'playerTotal': 16, 'dealerCard': 3},
        122: {'playerTotal': 16, 'dealerCard': 4},
        123: {'playerTotal': 16, 'dealerCard': 5},
        124: {'playerTotal': 16, 'dealerCard': 6},
        125: {'playerTotal': 16, 'dealerCard': 7},
        126: {'playerTotal': 16, 'dealerCard': 8},
        127: {'playerTotal': 16, 'dealerCard': 9},
        128: {'playerTotal': 16, 'dealerCard': 10},
        129: {'playerTotal': 16, 'dealerCard': 11},
        130: {'playerTotal': 17, 'dealerCard': 2},
        131: {'playerTotal': 17, 'dealerCard': 3},
        132: {'playerTotal': 17, 'dealerCard': 4},
        133: {'playerTotal': 17, 'dealerCard': 5},
        134: {'playerTotal': 17, 'dealerCard': 6},
        135: {'playerTotal': 17, 'dealerCard': 7},
        136: {'playerTotal': 17, 'dealerCard': 8},
        137: {'playerTotal': 17, 'dealerCard': 9},
        138: {'playerTotal': 17, 'dealerCard': 10},
        139: {'playerTotal': 17, 'dealerCard': 11},
        140: {'playerTotal': 18, 'dealerCard': 2},
        141: {'playerTotal': 18, 'dealerCard': 3},
        142: {'playerTotal': 18, 'dealerCard': 4},
        143: {'playerTotal': 18, 'dealerCard': 5},
        144: {'playerTotal': 18, 'dealerCard': 6},
        145: {'playerTotal': 18, 'dealerCard': 7},
        146: {'playerTotal': 18, 'dealerCard': 8},
        147: {'playerTotal': 18, 'dealerCard': 9},
        148: {'playerTotal': 18, 'dealerCard': 10},
        149: {'playerTotal': 18, 'dealerCard': 11},
        150: {'playerTotal': 19, 'dealerCard': 2},
        151: {'playerTotal': 19, 'dealerCard': 3},
        152: {'playerTotal': 19, 'dealerCard': 4},
        153: {'playerTotal': 19, 'dealerCard': 5},
        154: {'playerTotal': 19, 'dealerCard': 6},
        155: {'playerTotal': 19, 'dealerCard': 7},
        156: {'playerTotal': 19, 'dealerCard': 8},
        157: {'playerTotal': 19, 'dealerCard': 9},
        158: {'playerTotal': 19, 'dealerCard': 10},
        159: {'playerTotal': 19, 'dealerCard': 11},
        160: {'playerTotal': 20, 'dealerCard': 2},
        161: {'playerTotal': 20, 'dealerCard': 3},
        162: {'playerTotal': 20, 'dealerCard': 4},
        163: {'playerTotal': 20, 'dealerCard': 5},
        164: {'playerTotal': 20, 'dealerCard': 6},
        165: {'playerTotal': 20, 'dealerCard': 7},
        166: {'playerTotal': 20, 'dealerCard': 8},
        167: {'playerTotal': 20, 'dealerCard': 9},
        168: {'playerTotal': 20, 'dealerCard': 10},
        169: {'playerTotal': 20, 'dealerCard': 11}
    }
    scenarioIDToScenarioWithAce = {
         170: {"playerTotal": 13, "dealerCard": 2},
        171: {"playerTotal": 13, "dealerCard": 3},
        172: {"playerTotal": 13, "dealerCard": 4},
        173: {"playerTotal": 13, "dealerCard": 5},
        174: {"playerTotal": 13, "dealerCard": 6},
        175: {"playerTotal": 13, "dealerCard": 7},
        176: {"playerTotal": 13, "dealerCard": 8},
        177: {"playerTotal": 13, "dealerCard": 9},
        178: {"playerTotal": 13, "dealerCard": 10},
        179: {"playerTotal": 13, "dealerCard": 11},
        180: {"playerTotal": 14, "dealerCard": 2},
        181: {"playerTotal": 14, "dealerCard": 3},
        182: {"playerTotal": 14, "dealerCard": 4},
        183: {"playerTotal": 14, "dealerCard": 5},
        184: {"playerTotal": 14, "dealerCard": 6},
        185: {"playerTotal": 14, "dealerCard": 7},
        186: {"playerTotal": 14, "dealerCard": 8},
        187: {"playerTotal": 14, "dealerCard": 9},
        188: {"playerTotal": 14, "dealerCard": 10},
        189: {"playerTotal": 14, "dealerCard": 11},
        190: {"playerTotal": 15, "dealerCard": 2},
        191: {"playerTotal": 15, "dealerCard": 3},
        192: {"playerTotal": 15, "dealerCard": 4},
        193: {"playerTotal": 15, "dealerCard": 5},
        194: {"playerTotal": 15, "dealerCard": 6},
        195: {"playerTotal": 15, "dealerCard": 7},
        196: {"playerTotal": 15, "dealerCard": 8},
        197: {"playerTotal": 15, "dealerCard": 9},
        198: {"playerTotal": 15, "dealerCard": 10},
        199: {"playerTotal": 15, "dealerCard": 11},
        200: {"playerTotal": 16, "dealerCard": 2},
        201: {"playerTotal": 16, "dealerCard": 3},
        202: {"playerTotal": 16, "dealerCard": 4},
        203: {"playerTotal": 16, "dealerCard": 5},
        204: {"playerTotal": 16, "dealerCard": 6},
        205: {"playerTotal": 16, "dealerCard": 7},
        206: {"playerTotal": 16, "dealerCard": 8},
        207: {"playerTotal": 16, "dealerCard": 9},
        208: {"playerTotal": 16, "dealerCard": 10},
        209: {"playerTotal": 16, "dealerCard": 11},
        210: {"playerTotal": 17, "dealerCard": 2},
        211: {"playerTotal": 17, "dealerCard": 3},
        212: {"playerTotal": 17,"dealerCard": 4},
        213: {"playerTotal": 17,"dealerCard": 5},
        214: {"playerTotal": 17, "dealerCard": 6},
        215: {"playerTotal": 17, "dealerCard": 7},
        216: {"playerTotal": 17, "dealerCard": 8},
        217: {"playerTotal": 17, "dealerCard": 9},
        218: {"playerTotal": 17, "dealerCard": 10},
        219: {"playerTotal": 17, "dealerCard": 11},
        220: {"playerTotal": 18, "dealerCard": 2},
        221: {"playerTotal": 18, "dealerCard": 3},
        222: {"playerTotal": 18, "dealerCard": 4},
        223: {"playerTotal": 18, "dealerCard": 5},
        224: {"playerTotal": 18, "dealerCard": 6},
        225: {"playerTotal": 18, "dealerCard": 7},
        226: {"playerTotal": 18, "dealerCard": 8},
        227: {"playerTotal": 18, "dealerCard": 9},
        228: {"playerTotal": 18, "dealerCard": 10},
        229: {"playerTotal": 18, "dealerCard": 11},
        230: {"playerTotal": 19, "dealerCard": 2},
        231: {"playerTotal": 19, "dealerCard": 3},
        232: {"playerTotal": 19, "dealerCard": 4},
        233: {"playerTotal": 19, "dealerCard": 5},
        234: {"playerTotal": 19, "dealerCard": 6},
        235: {"playerTotal": 19, "dealerCard": 7},
        236: {"playerTotal": 19, "dealerCard": 8},
        237: {"playerTotal": 19, "dealerCard": 9},
        238: {"playerTotal": 19, "dealerCard": 10},
        239: {"playerTotal": 19, "dealerCard": 11},
        240: {"playerTotal": 20, "dealerCard": 2},
        241: {"playerTotal": 20, "dealerCard": 3},
        242: {"playerTotal": 20, "dealerCard": 4},
        243: {"playerTotal": 20, "dealerCard": 5},
        244: {"playerTotal": 20, "dealerCard": 6},
        245: {"playerTotal": 20, "dealerCard": 7},
        246: {"playerTotal": 20, "dealerCard": 8},
        247: {"playerTotal": 20, "dealerCard": 9},
        248: {"playerTotal": 20,"dealerCard": 10},
        249: {"playerTotal": 20, "dealerCard": 11}
    }
    if (playerAceCount != 0){
        for (element in scenarioIDToScenarioWithAce){
            if (playerValue == scenarioIDToScenarioWithAce[element]["playerTotal"]){
                if (dealerCard == scenarioIDToScenarioWithAce[element]["dealerCard"]){
                    decision =  scenarioID[element]
                    if (decision == 1){
                        alert("You should hit!")
                    }
                    else{
                        alert("You should stand!")
                    }
                }
                    
            }
        }
    }
    else{
        for (element in scenarioIDToScenarioNoAce) {
            if (playerValue == scenarioIDToScenarioNoAce[element]["playerTotal"]){
                if (dealerCard == scenarioIDToScenarioNoAce[element]["dealerCard"]){
                    decision = scenarioID[element]
                    if (decision == 1){
                        alert("You should hit!")
                    }
                    else{
                        alert("You should stand!")
                    }
                    
                }
            }
        }
            
    }
        
    return;
}   
function flip() {
    var original_src = document.getElementById("firstCard").src
    document.getElementById("firstCard").src = document.getElementById("firstCard").getAttribute("data-src")
    document.getElementById("firstCard").setAttribute("data-src", original_src)
}
async function dealer() {
    document.getElementById("hit-button").disabled = true;
    document.getElementById("stand-button").disabled = true;
    document.getElementById("hint-button").disabled = true;
    flip()
    preDealer = false
    updateDealerTotalElement(preDealer)
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

// calling hint instead of initialize game
// calling initialize game in hint to get dealer card
// changed for loop to two calls and in display card we now return dealer card

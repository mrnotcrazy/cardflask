class Deck{
    constructor(){
        this.deck = [];
        this.deck_all = [];
    }

    shuffle() {
    const { deck } = this;
    let m = deck.length, i;

  while (m) {
    i = Math.floor(Math.random() * m--);

    [deck[m], deck[i]] = [deck[i], deck[m]];
    }

  return this;
    }

    deal() {

    return this.deck.pop();


    }

    reset() {
    this.deck = this.deck_all;
    }

    removeCard(card) {
    const { deck_all } = this;
    const index = deck_all.indexOf(card);

    if (index === -1) {
      return null;
          }
    else {

    deck_all.splice(index,1);
    this.deck = deck_all;
    }
    }
    addCard(card) {
    this.deck_all.push(card);
    this.deck = this.deck_all;
    }
    clear(){
    this.deck = [];
    this.deck_all = [];}

}

class Pile{
    constructor(){
        this.pile = [];
    }

    addCard(card){
    console.log(card);
        this.pile.push(card);
    }

    removeCard(card){
        const { pile } = this;
        const index = pile.indexOf(card);

        if (index === -1) {
            return null;
        }
        else {
            pile.remove(index);
        }
    }

    drawCard(){
        return this.pile.slice(-1)[0]
        this.pile.pop();
    }
    clearPile(){
        this.pile = [];
    }
}


function updateDeckView(currentDeck){
    var deckView = document.getElementById("deck");
    deckView.innerHTML = "";
    for (let each of currentDeck.deck_all){
        deckView.innerHTML +="<input type=\"image\" id="+ each +" src="+each+ " name=\"saveForm\" class=\'img\' onclick=\"deck.removeCard(this.id);updateDeckView(deck)\">";
    }
}

function saveFile(){
var text = "";
for (let each of deck.deck_all){
    text += each + "\n";
}
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', "deck.save");

    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);


}
//a function to upload a file from the client and itterate over the lines to add the cards to the deck
function loadFile(){
    // Get the file object from the event
  var file = event.target.files[0];

  // Create a new FileReader object
  var reader = new FileReader();

  // Set the onload handler for the FileReader object
    reader.onload = function(event) {
    // Get the contents of the file as a string
    var contents = event.target.result;

    // Split the contents into an array of lines
    var lines = contents.split("\n");

    // Iterate over the lines
    for (let each of lines) {

      console.log(each);
    }
  }

  // Read the file as a text file
  reader.readAsText(file);
}


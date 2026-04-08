const name_input = document.querySelector("#name_input");
const name_btn = document.querySelector("#name_button");
const name_message = document.querySelector("#name_message");

const teams = document.querySelector("#teams");
const team_btn = document.querySelector("#team_button");
const team_message = document.querySelector("#team_message");

const food_form = document.querySelector("#food_form");
const food_btn = document.querySelector("#food_button");
const food_message = document.querySelector("#food_message");

//Getting values from a simple input field.
name_btn.addEventListener("click", function(e){
    let name = name_input.value;
    name_message.innerHTML = "Thank you " + name + "! I appreciate you entering your name!";
})

//Getting a value from an isolated select element.
function getTeam(e){
    team_message.innerHTML = "I hope the " + teams.value + " wins the match!"
}

team_btn.addEventListener("click", getTeam);

//Getting a value from linked radio buttons within a form.
function getFood(e){
    let fav_food = food_form.fav_food;
    food_message.innerHTML = "I'd really love a " + fav_food.value + " too!";
}

food_btn.addEventListener("click", getFood);

const color_form = document.querySelector("#color_form");
const color_btn = document.querySelector("#color_btn");
const color_message = document.querySelector("#color_message");

const birthday_input = document.querySelector("#birthday_input");
const birthday_message = document.querySelector("#birthday_message");

const color_input = document.querySelector("#color_input");
const main = document.querySelector("main");

//Getting values from linked checkboxes within a form.
function getColor(e){
    let fav_colors = [];
    for (let i=0; i < color_form.length; i++){
        if (color_form[i].checked){
            fav_colors.push(color_form[i].value);
        }
    }
    color_message.innerHTML = "You like the following colors: " + fav_colors;
}

color_btn.addEventListener("click", getColor);

//Getting values on the change of an input field
birthday_input.addEventListener("change", function(e){
    birthday_message.innerHTML = "Your birthday is recorded as " + this.value;
})

color_input.addEventListener("change", function(e){
    main.style.backgroundColor = this.value;
})

const my_main = document.querySelector("main");
 
const new_heading = document.createElement("h3");
const new_paragraph = document.createElement("p");
my_main.append(new_heading);
my_main.append(new_paragraph);

new_heading.innerHTML = "This is my new heading!";
new_paragraph.innerHTML = "This is my new paragraph!";

//Using query selectors we can grab elements by their id (#).
const original_heading = document.querySelector("#my_h2");
original_heading.innerHTML = "We are using querySelector!";

// We can select elements that are nested
const div_paragraph = document.querySelector("div p");
div_paragraph.setAttribute("style", "background:purple; color:white")

/*
    We can use pseudo classes to target various elements.
    However, note that querySelector will ONLY return the first html element
    That meets the selection criteria!
*/
const odd_paragraph = document.querySelector(".query_p:nth-of-type(2n-1)");
odd_paragraph.innerHTML = "This is a single odd paragraph grabbed using querySelector()!"

/*
    To select ALL elements that meet the search criteia we can use querySelectorAll().
    This will return an array we can loop over.
*/
const even_paragraphs = document.querySelectorAll(".query_p:nth-of-type(2n)");
for (even_paragraph of even_paragraphs){
    even_paragraph.innerHTML = "This is an even paragraph that we grabbed using querySelectorAll()!";
    even_paragraph.style.color = "red";
}

